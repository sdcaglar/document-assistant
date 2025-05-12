from fastapi import FastAPI

from app.config import settings
from app.document import document

app = FastAPI()


app.mount("/document" + settings.API_VERSION_STR, document)
