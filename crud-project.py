
contents = "Hello World" + "\n" + "\n" + "..." + "\n" + "\n" + "Goodbye"
print(contents)

with open("my_message.txt", "w") as f:
    f.write(contents)
