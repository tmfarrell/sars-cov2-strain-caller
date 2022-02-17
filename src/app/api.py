from typing import Optional
import tempfile

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .utils import call_pangolin


class Fasta(BaseModel):
    name: str
    description: Optional[str] = None
    sequence: str


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to SARS-CoV-2 strains API."}


@app.post("/strain/")
async def call_strain(fasta: Fasta) -> dict:
    with tempfile.NamedTemporaryFile() as f:
        f.write(b'>' + fasta.name.encode() + b'\n')
        f.write(fasta.sequence.encode())
        results = call_pangolin(f.name)
    return results