from fastapi import FastAPI
from sprocket_api.routes import Routes
import uvicorn

app = FastAPI()
Routes(app).register()

if __name__ == "__main__":
    uvicorn.run("sprocket_api.server:app", host="0.0.0.0", port=8080, reload=True)