const button = document.querySelector(".btn");

async function handleBtn() {
  let url = "/api/create";

  let response = await fetch(url);

  if (response.ok) {
    // если HTTP-статус в диапазоне 200-299
    // получаем тело ответа (см. про этот метод ниже)
    alert("ok!");
    window.open(response.blob());
  } else {
    alert("Ошибка HTTP: " + response.status);
  }
}

button.addEventListener("click", handleBtn);
