from fastapi import FastAPI

app=fastAPI()

@app.get("/")
def read_root():
    return{"Hello":"World"}

@app.get("/new-feature")
def read_new_feature():
    return{"New":"Feature"}
