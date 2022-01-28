import ast

class Item:
    __instance = None
    __itemList = []

    def __init__(self):
        if Item.__instance is not None:
            raise Exception("I'm Singleton")
        else:
            Item.__instance = self

    @staticmethod
    def GetInstance():
        if Item.__instance is None:
            Item.__instance = Item()
        
        with open("./data/itemList.txt") as f:
            data = ast.literal_eval(f.read())
        Item.__itemList = data
        
        # Item.__itemList = [
        #     {"name": "Milk",
        #      "quantity": "3",
        #      "notes": "filtered",
        #      "listtype": "m",
        #     },
        #     {"name": "Eggs",
        #      "quantity": "30",
        #      "notes": "",
        #      "listtype": "m",
        #     },
        #     {"name": "Chicken",
        #      "quantity": "2kg",
        #      "notes": "",
        #      "listtype": "m",
        #     }
        #    ]
        
        return Item.__instance

    @staticmethod
    def GetItemList():
        return Item.__itemList

    @staticmethod
    def SetItemList(newItemList):
        Item.__itemList = newItemList
        Item.__persistData()

    @staticmethod
    def AddItem(newItem):
        for item in Item.__itemList:
            if item["name"] == newItem[0]["name"]:
                return Item.__itemList
        Item.__itemList.append(newItem[0])
        Item.__persistData()
        return Item.__itemList

    @staticmethod
    def __persistData():
        content = "[" + (",".join(str(item) for item in Item.__itemList)) + "]"
        with open("./data/itemList.txt", "w") as dataFile:
            dataFile.write(content)
                
