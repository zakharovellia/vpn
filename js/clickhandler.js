const button = document.querySelector(".btn");

async function handleBtn() {
  const url = "/api/create";
  const response = await fetch(url);

  if (response.ok) {

    const file = await response.blob();
    const downloadUrl = window.URL.createObjectURL(file);
    const link = document.createElement("a");
    link.href = downloadUrl;
    link.download = "your.conf";
    document.body.appendChild(link);
    link.click();
    link.remove();

  } else {
    alert("Ошибка HTTP: " + response.status);
  }
}

button.addEventListener("click", handleBtn);
