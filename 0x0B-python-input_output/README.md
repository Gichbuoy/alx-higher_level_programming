## Python - Input/Output

- In Python, input/output (I/O) operations are used for reading input from the user, writing output to the console or files, and interacting with external data sources. 
- Python provides several built-in functions and modules for performing I/O operations.
- some of the common methods for input and output in Python:

# Standard Input/Output:

* input(prompt): Reads input from the user as a string, displaying the optional prompt message. The input is terminated by pressing the Enter key. Example: name = input("Enter your name: ")

* print(*objects, sep=' ', end='\n'): Writes the string representation of objects to the standard output (console) with an optional separator sep between objects and an optional ending string end. Example: print("Hello, World!")

# File Input/Output:

- Opening and Closing Files:

* open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None): Opens a file and returns a file object. The mode parameter specifies the file mode ('r' for reading, 'w' for writing, 'a' for appending, etc.). Example: file = open("data.txt", "r")
* file.close(): Closes the file object, releasing system resources.

- Reading from Files:

* read(size=-1): Reads and returns the specified number of characters from the file, or the entire file if size is not specified. Example: content = file.read()
* readline(): Reads and returns the next line from the file. Example: line = file.readline()
* readlines(): Reads all lines from the file and returns them as a list of strings. Example: lines = file.readlines()

- Writing to Files:

* write(str): Writes the string str to the file. Example: file.write("Hello, World!")
* writelines(lines): Writes a list of strings (lines) to the file. Example: file.writelines(["Hello", "World"])


# Exception Handling for I/O:

- Exceptions such as FileNotFoundError, PermissionError, and IOError can occur when performing I/O operations. It's important to handle these exceptions using try-except blocks to handle errors gracefully.
