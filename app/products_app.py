import csv

#
#Checkpoint 2
#

##read

products = []

csv_file_path = "data\products.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        #print(row["id"], row["name"])
        products.append(row)

print(len(products))


##write

other_path = "data\other_products.csv"
with open(other_path, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)

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

def show_product():
    print("SHOWING A PRODUCT")

def create_product():
    print("CREATING A PRODUCT")

def update_product():
    print("UPDATING A PRODUCT")

def destroy_product():
    print("DESTROYING A PRODUCT")

if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")



#
#Checkpoint 2
#

##read









#contents = "Hello World" + "\n" + "\n" + "..." + "\n" + "\n" + "Goodbye"
#print(contents)

#with open("data\writing-stuff.csv", "w") as f:
#    f.write(contents)



#
#Checkpoint 3
#
