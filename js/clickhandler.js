const button = document.querySelector(".btn");

async function handleBtn() {
  let url = "localhost:8000/api/create";

  await fetch(url)
    .then((response) => response.json()) // Декодируем ответ в формате json
    .then((data) => console.log(data)); // Выводим ответ в консоль
}

button.addEventListener("click", handleBtn);
