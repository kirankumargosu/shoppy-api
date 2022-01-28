from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from item import Item

app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://192.168.1.181:3000",
    "192.168.1.181:3000",
    "*"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

itemList = [
            {"name": "Milk",
             "quantity": "3",
             "notes": "filtered",
             "listtype": "p",
            },
            {"name": "Eggs",
             "quantity": "30",
             "notes": "",
             "listtype": "m",
            },
            {"name": "Chicken",
             "quantity": "2kg",
             "notes": "",
             "listtype": "m",
            }
           ]


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Shoppy-Root."}

itemInstance = Item.GetInstance()

#items
@app.get("/items", tags=["items"])
async def get_items() -> dict:
    itemList = itemInstance.GetItemList()
    # print("get", itemList)
    return {
        "data" : itemList
    }

@app.post("/items", tags=["items"])
async def update_items(newList: list) -> dict:
    itemInstance.SetItemList(newList)
    itemList = itemInstance.GetItemList()
    return{
        "data" : itemList
    }

@app.post("/additem", tags=["items"])
async def add_item(newItem: list) -> dict:
    itemList = itemInstance.AddItem(newItem)
    return{
        "data" : itemList
    }