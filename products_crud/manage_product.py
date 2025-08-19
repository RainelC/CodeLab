import database.data  as db

data = db.getData()

def get_products():
    return {k: v for k,v in data.items() if v['isActive'] is True}

def add_product(name: str, description: str, price: float):
    try:
        id = 1
        if data != {}:
            id = list(data.keys())[-1] + 1
        data[id] = {"name": name, "description": description, "price": price, "isActive": True}
        db.setData(data)
    except Exception as error:
        print(error)

def edit_product(Id: str, name: str, description: str, price: float): 
    if(data == {}):
        print("No hay productos disponibles")
    try:
        data[id] = {"name": name, "description": description, "price": price}
        db.setData(data)
    except KeyError:
        print(f'Product with id: {Id} was not found')

def delete_product(Id: str):
    if(data == {}):
        print("No hay productos disponibles")
    try:
        data[Id]['isActive'] = False
        db.setData(data)
    except KeyError:
        print(f'Product with id: {Id} was not found')
    
    