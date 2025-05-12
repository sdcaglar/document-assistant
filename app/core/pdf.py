from bson import ObjectId
from fastapi import HTTPException, UploadFile
from datetime import datetime
from typing import List
from app.core.mongo import db, fs
from pdfminer.high_level import extract_text
from io import BytesIO


class PDFCore:
    def _init_(self):
        pass

    def save_pdf(self, file: UploadFile, user_id: str):
        file_id = fs.put(file.file, filename=file.filename)
        metadata = {
            "user_id": user_id,
            "filename": file.filename,
            "upload_date": datetime.utcnow(),
            "file_id": file_id,
        }
        metadata_collection = db["pdf_metadata"]
        metadata_collection.insert_one(metadata)
        return metadata

    def get_user_pdfs(self, user_id: str) -> List[dict]:
        metadata_collection = db["pdf_metadata"]
        return list(metadata_collection.find({"user_id": user_id}))

    def select_pdf(self, pdf_id: str, user_id: str):
        metadata_collection = db["pdf_metadata"]
        pdf = metadata_collection.find_one(
            {"_id": ObjectId(pdf_id), "user_id": user_id}
        )
        if not pdf:
            raise HTTPException(status_code=404, detail="PDF not found")
        return pdf

    def extract_text_from_pdf(self, file_id: str, user_id: str):
        parsed_data_collection = db["parsed_data"]
        pdf_file = fs.get(ObjectId(file_id))
        if pdf_file is None:
            raise Exception("PDF file not found.")

        pdf_data = pdf_file.read()
        text = extract_text(BytesIO(pdf_data))
        parsed_data = {
            "user_id": user_id,
            "file_id": file_id,
            "text": text,
            "parsed_date": datetime.utcnow(),
        }
        parsed_data_collection.insert_one(parsed_data)
        return parsed_data


pdf_core = PDFCore()
