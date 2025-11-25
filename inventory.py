# this below is an example of a dictionary, used for recording the existing items, their id and their availability
inventory = [
    {'id': 'A001', 'name': 'Python Text Book', 'status': 'available'},
    {'id': 'A002', 'name': 'Laptop HP Spectre', 'status': 'borrowed'},
    {'id': 'A003', 'name': 'Samsung G S', 'status': 'availvable'},
]

array = ["item1", "item2", "item3"]
for pos, item in enumerate(array):
    print(f"Position: {pos} | Item: {item}")

# this is the first function, to ask user to add a new item to the dictionary above
def add():
    id = input("ID: ")
    name = input("Name: ")
    status = input("Status: ")

    # this is to have the user's input recorded into the dictionary
    item = {
        "id":id,
        "name":name,
        "status":status
    }
    inventory.append(item)

# this funtion is used to view all the items in the list
def view():
    for item in inventory:
        print(f"ID: {item["id"]} | Name: {item["name"]} | Status: {item["status"]}")

# this funtion is used to search for an item from the dictionary
def search():
    search_thing = input("Enter the name of the item:\n")
    for item in inventory:
        if search_thing.lower() in item["name"].lower():
            print(item)

# this is to update the item, to change it, in case you have a typo or a mistake           
def update():
    id = input("ID: ")
   
    # this is to replace the old values with the new ones that the user inputs
    for item in inventory:
        if item["id"] == id:
            new_id = input("New ID:\n")
            item["id"] = new_id
            
      
            new_name = input("New name:\n")
            item["name"] = new_name
            
       
            new_status = input("New status:\n")
            item["status"] = new_status
            
            print(item)


# this is to sort the data based on the id number
def sort_inv():
    def get_sort_key(item):
        return item["id"]
    sorted_data = sorted(inventory, key=get_sort_key)
    print(sorted_data)

# this is to delete an item from the inventory
def delete():
    value_of_user = input("Please enter the id of the item you wish to delete:\n")
    for i, item in enumerate(inventory):
        if item["id"] == value_of_user:
            confirm = input(f"Delete this item? (yes/no)\n{item}\n")
            if confirm.lower() in ("y", "yes"):
                inventory.pop(i)
                print("Deleted.")
            else:
                print("Cancelled.")
            return
    print("Item not found.")


    """
    for item in inventory:
        if item["id"] == value_of_user:
            yes_or_no = input(f"is this the file you wish to delete?/nOnce it is deleted, this action cannot be reversed\n {item}\n")
            if yes_or_no == "no":
                print("ok")
    """

# this is the starting question that the user sees, used to chose the action they want to do with the inventory
def menu():
    # while true to make this happens always unless closed 
    while True:
        data = int(input("Pick an action:\n1) View\n2) Add\n3) Search\n4) Exit\n5) Update\n6) Sort\n"))
        if data == 1:
            view()
        elif data == 2:
            add()
        elif data == 3:
            search()
        elif data == 4:
            break
        elif data == 5:
            update()
        elif data == 6:
            sort_inv()
        elif data == 7:
            delete()

# this is to call the funtion
menu()
