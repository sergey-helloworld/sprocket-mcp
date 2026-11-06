from fastapi import UploadFile, HTTPException
from typing import Final
from pathlib import Path
import uuid

class FileController:
    ALLOWED_EXTENSIONS: Final[list[str]] = [".xlsx", ".xls"]
    STORAGE_PATH: Final[str] = "storage"

    async def upload_file(self, file: UploadFile) -> dict[str, any]:
        extension = Path(file.filename or "").suffix.lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Only Excel files are allowed"
            )

        file_id = str(uuid.uuid4())
        file_path = Path(f"{self.STORAGE_PATH}/{file_id}{extension}")

        try:
            with file_path.open("wb") as buffer:
                while chunk := await file.read(1024 * 1024):
                    buffer.write(chunk)
        except Exception:
            file_path.unlink(missing_ok=True)
            raise HTTPException(
                status_code=500,
                detail="File upload failed"
            )
        finally:
            await file.close()

        return {
            "file_id": file_id,
            "filename": file.filename,
            "size": file_path.stat().st_size,
            "status": "uploaded"
        }