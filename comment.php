<h2>Комментарии</h2>

<form id="comment-form">
    <div>
        <label for="name">Имя:</label>
        <input type="text" id="name" required>
    </div>
    <div>
        <label for="comment">Комментарий:</label>
        <textarea id="comment" required></textarea>
    </div>
    <div>
        <button type="submit">Отправить</button>
    </div>
</form>

<div id="comments"></div>

<script>
    var commentForm = document.getElementById("comment-form");
    var commentsDiv = document.getElementById("comments");

    commentForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Отменяем отправку формы по умолчанию

        var name = document.getElementById("name").value;
        var comment = document.getElementById("comment").value;

        // Отправляем данные на сервер с помощью AJAX-запроса
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/submit-comment");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                var response = JSON.parse(xhr.responseText);

                if (response.success) {
                    var commentDiv = document.createElement("div");
                    commentDiv.innerHTML = "<strong>" + name + "</strong>: " + comment;
                    commentsDiv.appendChild(commentDiv);

                    // Очищаем форму
                    document.getElementById("name").value = "";
                    document.getElementById("comment").value = "";
                } else {
                    alert("Ошибка при отправке комментария");
                }
            }
        };
        xhr.send(JSON.stringify({ name: name, comment: comment }));
    });
</script>
