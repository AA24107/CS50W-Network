import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .models import User, Post


def index(request):
    posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", {
        "page_obj": page_obj,
        "title": "All Posts",
    })

def following(request):
    followed = request.user.following.all()
    posts = Post.objects.filter(user__in = followed).order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        "page_obj": page_obj,
        "title": "Following",
    })

def profile(request, username):
    profile_user = User.objects.get(username = username)
    if request.method == "POST":
        if request.user.is_authenticated and request.user != profile_user:
            if profile_user in request.user.following.all():
                request.user.following.remove(profile_user)
            else:
                request.user.following.add(profile_user)

        return redirect("profile", username=username)

    posts = Post.objects.filter(user = profile_user).order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = profile_user.follower.filter(id=request.user.id).exists()
    return render(request, "network/profile.html", {
        "profile": profile_user,
        "page_obj": page_obj,
        "is_following": is_following
    })

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
@login_required
def post(request, post_id):

    if request.method == "PUT":
        data = json.loads(request.body)
        new_content = data.get("content")

        post = Post.objects.get(id=post_id)
        post.content = new_content
        post.save()

        return JsonResponse({"message": "Post updated"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required   
def new_post(request):
    if request.method == "POST":
        content = request.POST["content"]
        creator = request.user
        Post.objects.create(
            content = content,
            user = creator, 
        )

        return HttpResponseRedirect(reverse('index'))
    return render(request, "network/new_post.html")
