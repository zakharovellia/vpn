const button = document.querySelector(".btn");

function handleBtn() {
  console.log("Yo! It's me, JS!");
  let url = "http://0.0.0.0:8080";

  fetch(url)
    .then((response) => response.json()) // Декодируем ответ в формате json
    .then((data) => console.log(data)); // Выводим ответ в консоль
}

button.addEventListener("click", handleBtn);
