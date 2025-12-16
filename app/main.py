from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Video Analytics API is running."}