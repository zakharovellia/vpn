const button = document.querySelector(".btn");

async function handleBtn() {
  let url = "/api/create";

  let response = await fetch(url);

  if (response.ok) {
    var a = document.createElement("a");
    let file = await response.blob()
    a.href = URL.createObjectURL(file);
    a.setAttribute("download", "your.conf");
    a.click();
  } else {
    alert("Ошибка HTTP: " + response.status);
  }
}

button.addEventListener("click", handleBtn);
