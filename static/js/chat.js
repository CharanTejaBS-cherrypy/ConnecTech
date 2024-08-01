document.addEventListener("DOMContentLoaded", function () {
  const messageForm = document.getElementById("message-form");
  const messageContent = document.getElementById("message-content");
  const chat = document.getElementById("chat");

  messageForm.addEventListener("submit", function (event) {
    event.preventDefault();
    fetch(window.location.href + "send_message/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
      body: `content=${messageContent.value}`,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "ok") {
          chat.innerHTML += `<p><strong>You:</strong> ${messageContent.value}</p>`;
          messageContent.value = "";
        }
      });
  });
});
