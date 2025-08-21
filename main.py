from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que React haga peticiones al backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción deberías poner el dominio de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz opcional
@app.get("/")
def read_root():
    return {"message": "API funcionando"}

# Endpoint para orders
@app.get("/api/orders")
def get_orders():
    return [
        {"id": 1, "item": "Camiseta"},
        {"id": 2, "item": "Pantalón"},
        {"id": 3, "item": "Zapatos"},
    ]
