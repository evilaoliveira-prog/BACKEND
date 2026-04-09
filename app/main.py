from fastapi import FastAPI


app = FastAPI(title="Mercearia do João - Backend")


@app.get("/")
def root():
    return {"mensagem": "API rodando! 🎉 Bem-vindo à Mercearia do João"}
