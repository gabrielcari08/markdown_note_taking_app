from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from app.services import grammar, markdown_handler
from pathlib import Path

router = APIRouter()

#Endpoint de prueba
@router.get("/")
async def hello_router():
    return {"mesagge": "Hello router!"}

#Endpoint para verificar gramatica
@router.post("/check_grammar")
async def check_grammar(text: str = Form(...)): # Form indica que es un campo obligatorio.
    result = grammar.check_text(text)
    # Retorno del texto con correcciones.
    return {"correciones": result}

#Endpoint para guardar una nota.
@router.post("/save_note")
async def save_note(file: UploadFile = File(...)):
    contents = await file.read()
    note_path = Path(f"app/storage/notes/{file.filename}")
    note_path.write_text(contents.decode('utf-8'))
    return {"mensaje": f"Nota '{file.filename}' guardada correctamente."}

#Endpoint para listar notas
@router.get("/notes")
async def list_notes():
    notes_dir = Path("app/storage/notes")
    files = [file.name for file in notes_dir.glob("*.md")]
    return {"notas": files}

#Endpoint para renderizar nota como HTML.
@router.get("/render-note/{filename}", response_class=HTMLResponse)
async def render_note(filename: str):
    note_path = Path(f"app/storage/notes/{filename}")
    if not note_path.exists():
        return HTMLResponse(content="Nota no encontrada", status_code=404)
    md_content = note_path.read_text()
    html_content = markdown_handler.render_markdown(md_content)
    return HTMLResponse(content=html_content)