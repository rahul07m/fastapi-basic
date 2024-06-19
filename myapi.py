#pip install fastapi uvicorn
#uvicorn myapi:app --reload
#http://127.0.0.1:8000/docs  to see all the endpoints
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

data = {
    1: {"name": "Rahul",
        "Partner": "Sap",
        "Age": 23

    },
    2: {"name": "John",
        "Partner": "zedd",
        "Age": 24

    },
    3: {"name": "Bapi",
        "Partner": "Ramu",
        "Age": 21

    }
}
class new_Datas(BaseModel):
    name:str
    Partner:str
    Age:int

class update_data(BaseModel):
    name : Optional[str] = None
    Partner: Optional[str] = None
    Age: Optional[int] = None

@app.get("/")
def base():
    return {"Name":"This is the first data"}

@app.get("/get-data/{data_id}")
def get_data(data_id:int):
    if data_id not in data:
        return {"Error":"Data doesn't exists"}
    return data[data_id]

@app.get("/get-name/{data_id}")
def get_data(data_id: int):
    return data[data_id]["name"]

@app.get("/get-by-name")
def get_by_name(name: str):
    for student_id in data:
        if data[student_id]["name"] == name:
            return data[student_id]
    return {"Name":"Not Found"}

@app.post("/create-data/{data_id}")
def create_data(data_id: int, datas : new_Datas ): #previous one was data , New one is new_Datas , and the object is datas with s in the end
    if data_id in data:                             #datas in the argument to take data
        return {"Error":"Data already exists"}
    data[data_id] = datas 
    return data[data_id]
@app.put("/update-data/{data_id}")
def update_data(data_id:int, datas : update_data):
    if data_id not in data:
        return {"Error":"Data doesn't exists"}

    if datas.name != None:
        data[data_id].name = datas.name
    if datas.name != None:
        data[data_id].Partner = datas.Partner
    if datas.name != None:
        data[data_id].Age = datas.Age
    
    return data[data_id]


@app.delete("/delete-data/{data_id}")
def delete_data(data_id : int):
    if data_id not in data:
        return {"Error":"Data doesn't exists"}
    del data[data_id]
    return {"Message":"Deleted successfully"}