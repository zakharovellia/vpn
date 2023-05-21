from fastapi import FastAPI

app = FastAPI()
print("Приложень запущена")

@app.get("/")
async def root():
    return {"message": "Hello World"}

