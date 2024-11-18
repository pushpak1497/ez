from fastapi import FastAPI
from routes import ops, client, auth

app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(ops.router, prefix="/ops", tags=["Ops User"])
app.include_router(client.router, prefix="/client", tags=["Client User"])

@app.get("/")
def root():
    return {"message": "Welcome to the Secure File Sharing System"}
