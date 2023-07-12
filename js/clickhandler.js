const button = document.querySelector(".btn");

async function handleBtn() {
  const url = "/api/create";
  const response = await fetch(url);

  if (response.ok) {
    const file = await response.blob();
    const downloadUrl = window.URL.createObjectURL(file);
    const link = document.createElement("a");
    link.href = URL.createObjectURL(file);
    link.download = "your.conf";
    link.click();
    link.remove();
  } else {
    alert("Ошибка HTTP: " + response.status);
  }
}

button.addEventListener("click", handleBtn);
