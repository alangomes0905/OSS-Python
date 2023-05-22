with open("greeting.txt", "w") as file:
    file.write("hello world")


with open("greeting.txt", "r") as file:
    file_contents = file.read()

exec(file_contents)