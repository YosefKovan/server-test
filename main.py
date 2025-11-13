from fastapi import FastAPI
import uvicorn
from server_functions.file_writer import write_name
from pydantic import BaseModel
from server_functions.encryption import *
from server_functions.file_writer import *
from datetime import time


class Caesar(BaseModel):
    text : str
    offset : int
    mode : str

class FenceCipher(BaseModel):
    text : str

app = FastAPI()

@app.get("/test")
def test():
    print("test endpoint")
    #endpoint_increment_total_request("/test", "GET")
    return {"msg" : "hi from test"}

@app.get("/test/{name}")
def test_name(name : str):
     print("test_name endpoint")
     #endpoint_increment_total_request("/test/{name}", "GET")
     write_name(name)
     return {"msg" : "Saved User"}

@app.post("/caesar")
def caesar(body_data : Caesar):
    print("caesar endpoint")
    #endpoint_increment_total_request("/caesar", "GET")
    return handle_caesar(body_data)

@app.get("/fence/encrypt")
def encrypt_rail_fence_cipher_endpoint(text : str):
    print("encrypt_rail_fence_cipher_endpoint endpoint")
    #endpoint_increment_total_request("/fence/encrypt", "GET")
    return encrypt_fence_cipher(text)

@app.post("/fence/decrypt")
def decrypt_fence_cipher_endpoint(data : FenceCipher):
    print("decrypt_fence_cipher_endpoint endpoint")
    #endpoint_increment_total_request("/fence/decrypt", "POST")
    return decrypt_fence_cipher(data)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


