inventory = [
    {'id': 'A001', 'name': 'Python Text Book', 'status': 'available'},
    {'id': 'A002', 'name': 'Laptop HP Spectre', 'status': 'borrowed'},
    {'id': 'A003', 'name': 'Samsung G S', 'status': 'availvable'},
]

def add():
    id = input("ID: ")
    name = input("Name: ")
    status = input("Status: ")

    item = {
        "id":id,
        "name":name,
        "status":status
    }
    inventory.append(item)

def view():
    for item in inventory:
        print(f"ID: {item["id"]} | Name: {item["name"]} | Status: {item["status"]}")



def menu():
    while True:
        data = int(input("Pick an action:\n1) View\n2)Add\n3)Exit\n"))
        if data == 1:
            view()
        elif data == 2:
            add()
        elif data == 3:
            break

menu()