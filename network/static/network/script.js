document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".edit-btn").forEach(button => {
        button.addEventListener("click", function() {
            edit(this.dataset.id);
        });
    });
    document.querySelectorAll(".like-btn").forEach(button => {
        button.addEventListener("click", function() {
            like(this.dataset.id);
        });
    });
});

function like (post_id) {
    fetch(`/posts/${post_id}/like`, {
        method: "PUT",
    })
    .then(response => response.json())
    .then(data => {
        const button = document.querySelector(`.like-btn[data-id="${post_id}"]`);
        const count = document.querySelector(`#likes-${post_id}`);

        count.textContent = `${data.likes_count} likes`;

        if (data.liked) {
            button.textContent = "Unlike";
        } else {
            button.textContent = "Like";
        }
    })
}

function edit (post_id) {
    const original = document.querySelector(`#content-${post_id}`).innerHTML;
    document.querySelector(`#content-${post_id}`).innerHTML = `
        <textarea id="edit">${original}</textarea>
        <br>
        <button class="edit-btn" onclick="save(${post_id})">Save</button>`
}

function save (post_id) {
    const new_text = document.querySelector("#edit").value;
    fetch(`/posts/${post_id}`, {
        method: "PUT",
        body: JSON.stringify({
            content: new_text,
        })
    })
    .then(response => response.json())
    .then(data => {
        document.querySelector(`#content-${post_id}`).innerHTML = new_text;
    });
}