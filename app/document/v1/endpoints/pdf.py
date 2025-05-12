from fastapi import APIRouter, Depends, File, UploadFile
from app.core.pdf import pdf_core
from app.document.v1.dependencies import get_current_active_user
from app.helper.str_helper import convert_objectid_to_str
from app.models.user import User

router = APIRouter()


@router.post("/pdf-upload")
async def pdf_upload(
    file: UploadFile = File(...), user: User = Depends(get_current_active_user)
):
    result = pdf_core.save_pdf(file, user["user_id"])
    return {
        "message": "PDF successfully uploaded.",
        "data": convert_objectid_to_str(result),
    }


@router.get("/pdf-list")
async def pdf_list(user: User = Depends(get_current_active_user)):
    pdfs = pdf_core.get_user_pdfs(user["user_id"])
    return {"pdfs": convert_objectid_to_str(pdfs)}


@router.post("/pdf-select")
async def pdf_select(pdf_id: str, user: User = Depends(get_current_active_user)):
    pdf = pdf_core.select_pdf(pdf_id, user["user_id"])
    return {
        "message": "PDF selected successfully.",
        "data": convert_objectid_to_str(pdf),
    }


@router.post("/pdf-parse")
async def pdf_parse(pdf_id: str, user: User = Depends(get_current_active_user)):
    pdf = pdf_core.select_pdf(pdf_id, user["user_id"])
    result = pdf_core.extract_text_from_pdf(pdf["file_id"], user["user_id"])
    return {
        "message": "PDF parsed successfully.",
        "data": convert_objectid_to_str(result),
    }
