from fastapi import UploadFile, File, APIRouter


router = APIRouter()


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...), UPLOAD_DIR=None):
    return ""
