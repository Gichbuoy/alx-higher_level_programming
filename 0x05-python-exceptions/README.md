# Errors and Exeptions
- They  are used to handle unexpected or exceptional situations that occur during the execution of a program.
- When an error occurs, Python raises an exception, which is an object representing the error.

	* Syntax
		try:
    		# Code that might raise an exception
		except ExceptionType:
    		# Code to handle the exception

### Common Errors and Exceptions
- SyntaxError: This error occurs when there is a syntax mistake in your code, such as missing a closing parenthesis or using an invalid keyword.

- NameError: This error occurs when you try to use a variable or name that hasn't been defined.

- TypeError: This error occurs when an operation is performed on incompatible data types, or when a function receives arguments of the wrong type.

- IndexError: This error occurs when you try to access an element in a sequence (e.g., list, tuple) using an invalid index.

- KeyError: This error occurs when you try to access a dictionary using a key that doesn't exist.

- ValueError: This error occurs when a function receives an argument of the correct type but with an invalid value.

- IOError: This error occurs when there's an issue with input/output operations, such as when a file cannot be opened or read.

