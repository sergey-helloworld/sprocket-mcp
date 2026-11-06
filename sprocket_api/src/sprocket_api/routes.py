from fastapi import FastAPI
from sprocket_api.controllers.file_controller import FileController

class Routes:
    def __init__(self, fast_api: FastAPI) -> None:
        self.fast_api: FastAPI = fast_api

    def register(self) -> None:
        self.fast_api.post("/files", response_model=None)(FileController().upload_file)