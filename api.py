from fastapi import FastAPI
from pydantic import BaseModel
from main import cadastrar_tarefa

class NovaTarefa(BaseModel):
    descricao: str

app = FastAPI()

tarefas = [
    {
        "id": 1,
        "descricao": "Estudar Python",
        "concluida": False
    },
    {
        "id": 2,
        "descricao": "Desenvolver API",
        "concluida": False
    }
]

@app.get("/tarefas")
def obter_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(nova_tarefa: NovaTarefa):
    return {"descricao": nova_tarefa.descricao}
