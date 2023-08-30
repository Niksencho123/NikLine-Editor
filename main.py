import time
import os
ani = 0
start = time.time()
while time.time() - start < 2:
    if ani == 0:
        print("|                                                       |")
        print("|                                                       |")
        print("|           |" + " NikLine Editor is loading!                |")
        print("|                                                       |")
        print("|                                                       |")
        ani += 1
        time.sleep(0.1)
        os.system("cls")
    if ani == 1:
        print("|                                                       |")
        print("|                                                       |")
        print("|           /" + " NikLine Editor is loading!                |")
        print("|                                                       |")
        print("|                                                       |")
        ani += 1
        time.sleep(0.1)
        os.system("cls")
    if ani == 2:
        print("|                                                       |")
        print("|                                                       |")
        print("|           -" + " NikLine Editor is loading!                |")
        print("|                                                       |")
        print("|                                                       |")
        ani += 1
        time.sleep(0.1)
        os.system("cls")
    if ani == 3:
        print("|                                                       |")
        print("|                                                       |")
        print("|           \\" + " NikLine Editor is loading!                |")
        print("|                                                       |")
        print("|                                                       |")
        ani = 0
        time.sleep(0.1)
        os.system("cls")
os.system("cls")
lineNum = 1
file = input("Enter a files name: ")
try:
    text_file = open(file, "r")
    command: str = ""
    Lines = text_file.readlines()
except:
    print("The File doesn't exist! Exiting the program!")
    time.sleep(1)
    quit()
if len(Lines) > 0:
    for Line in Lines:
        print(f"{lineNum}| {Line}")
        lineNum += 1
else:
    print("The file is empty! Nothing to print!")
lineNum = 1
while command != "EXIT":
    command = input("~ ")
    if command.startswith("/change"):
        parts = command.split()  # Split the command into words
        if len(parts) == 2:
            changeline = int(parts[1])  # Get the line number to change
            if 1 <= changeline <= len(Lines):
                new_content = input(f"Change line {changeline}: ")
                Lines[changeline - 1] = new_content + "\n"
                print(f"Line {changeline} has been updated.")
            else:
                print("Invalid line number!")
        else:
            print("Invalid command format!")
        print("\n")
    elif command == "/show":
        for Line in Lines:
            Line = Line.replace("\n", "")
            print(f"{lineNum}| {Line}")
            lineNum += 1
        lineNum = 1
        print("\n")
    elif command == "/clear":
        os.system("cls")  # Clear the console
    elif command.startswith("/tab"):
        parts = command.split()
        if len(parts) == 2:
            changeline = int(parts[1])
            if 1 <= changeline <= len(Lines):
                Lines[changeline - 1] = "\t" + Lines[changeline - 1]
                print(f"Line {changeline} has been tabulated!")
            else:
                print("This line doesn't exist!")
        else:
            print("Invalid command format!")
        print("\n")
    elif command.startswith("/untab"):
        parts = command.split()
        if len(parts) == 2:
            changeline = int(parts[1])
            if 1 <= changeline <= len(Lines):
                Lines[changeline - 1] = Lines[changeline - 1].replace("\t", "")
                print(f"Line {changeline} has been tabulated!")
            else:
                print("This line doesn't exist!")
        else:
            print("Invalid command format!")
        print("\n")
    elif command.startswith("/del"):
        parts = command.split()
        if len(parts) == 2:
            changeline = int(parts[1])
            if 1 <= changeline <= len(Lines):
                Lines.pop(changeline - 1)
                print(f"Line {changeline} has been removed!")
            else:
                if changeline == -1:
                    Lines.clear()
                else:
                    print("Invalid line number!")
        else:
            print("Invalid line number!")
        print("\n")
    elif command.startswith("/file"):
        parts = command.split()
        if len(parts) == 2:
            try:
                with open(file, "w") as output:
                    output.writelines(Lines)
                    print("DEBUG: ", parts)
                    file = parts[1]
                    text_file = open(file, "r")
                    Lines = text_file.readlines()
            except:
                text_file = open(file, "r")
                Lines = text_file.readlines()
        print("\n")
    elif command.startswith("/help"):
        os.system("cls")
        print("/change lineNumber - Lets you change the content of a line of your choosing")
        print("/show - Shows you the contents of the currently opened file")
        print("/clear - Clears the terminal")
        print("/tab lineNumber - Lets you tabulate a line of your choosing")
        print("/untab lineNumber - Lets you untabulate a line of your choosing")
        print("/del lineNumber - Lets you delete a line of your choosing")
        print("/del -1 - Deletes the entire file's contents")
        print("/file fileName - Changes the current working file")
        print("/info - Shows you information")
        print("EXIT - Exists out of the editor")
        print("\n")
    elif command.startswith("/info"):
        print("NikLine Editor @ Version BETA 0.1")
        print("Creator: Nik @ Niksencho", end="", flush=True)
        print("\n")
        print(f"Currently opened file: " + file)
        print("\n")
        print("Files in directory:")
        os.system("dir")
        print("\n")
    else:
        if command != "EXIT":
            Lines.append(command + "\n")

# Write the modified lines back to the file
with open(file, "w") as output:
    output.writelines(Lines)

os.system("cls")  # Clear the console
print("Editor closed.") 