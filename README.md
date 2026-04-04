# Network 
### Project 4

A full-stack social media web application where users can create posts, follow other users, like posts, and interact with a dynamic feed.

This web app is inspired by platforms like Twitter, built to explore real-time interactions using AJAX and dynamic UI updates.

This project was built as part of Harvard’s CS50W (Web Programming with Python and JavaScript) course.


## Features

* Create Posts
  Users can create and publish text-based posts.

* All Posts Feed
  View posts from all users with pagination.

* User Profiles
  -Each user has a profile page showing:
    * Their posts
    * Followers and following count

* Follow / Unfollow
  Users can follow and unfollow others.

* Like / Unlike (AJAX)
  - Like posts without reloading the page
  - Real-time update of like counts

* Edit Posts (AJAX)
  * Users can edit their own posts
  * Changes update instantly without page reload

* Following Feed
  * View posts only from users you follow.

* Pagination
  * Efficient navigation through posts.


## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite (default Django DB)
* **AJAX:** Fetch API


## Key Concepts

* Working with Django models and relationships (including Many-to-Many)
* Implementing user authentication and authorization
* Building REST-like endpoints for AJAX interactions
* Dynamic DOM manipulation using JavaScript
* Handling frontend state during user interactions
* Designing interactive UI without full page reloads


## Installation & Setup

1. Clone the repository:

   ```bash
   git clone (https://github.com/AA24107/CS50W-Network)
   cd network
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Open in your browser


## What I Learned

* Designing interactive applications with asynchronous frontend logic
* Managing relationships between users (followers, likes)
* Building REST-like endpoints in Django
* Handling UI updates without full page reloads


## Notes

* Only authenticated users can create, edit, like, and follow.
* Users can only edit their own posts.
* Like and edit actions are handled asynchronously using JavaScript.


## Acknowledgment

This project was completed as part of CS50W — Web Programming with Python and JavaScript by Harvard University.


## Demo

[![Watch the demo](https://img.youtube.com/vi/TSLEWjfygzg/0.jpg)](https://youtu.be/TSLEWjfygzg)
