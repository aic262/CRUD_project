import csv

#
#Checkpoint 2
#

##reading

products = []

csv_file_path = "data\products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        #print(row["id"], row["name"])
        products.append(row)

print(len(products))



#
#Checkpoint 1
#

menu = """

    Hi.

    Welcome to the products app.

    There are {0} products.

    Available operations: 'List', 'Show', 'Create', 'Update', 'Destroy'

    Please choose an operation:

""".format(len(products))



chosen_operation = input(menu)
chosen_operation = chosen_operation.title()

def list_products():
    print("LISTING PRODUCTS")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])


def show_product():
    print("SHOWING A PRODUCT")
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("READING PRODUCT HERE:", " + #" + str(product["id"]) + ": " + product["name"] +  ", " + product["aisle"] +  ", " + product["department"] +  ", " + product["price"])
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product)




def create_product():
    print("CREATING A PRODUCT")
    product_name = input("New Product Name: ")
    product_aisle = input("New Product Aisle: ")
    product_department = input("New Product Department: ")
    product_price = input("New Product Price: ")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)



def update_product():
    print("UPDATING A PRODUCT")
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in ["name","aisle","department","price"]:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)




def destroy_product():
    print("DESTROYING A PRODUCT")
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)





if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")



##writing

#contents = "Hello World" + "\n" + "\n" + "..." + "\n" + "\n" + "Goodbye"
#print(contents)

#with open("data\writing-stuff.csv", "w") as f:
#    f.write(contents)


other_path = "data\other_products.csv"
with open(other_path, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)
