## *args and *kwargs
- In Python, *args and **kwargs are special syntax used in function definitions to allow a variable number of arguments to be passed to a function.

### *args
- The *args syntax allows a function to accept any number of positional arguments. 
- When *args is used in a function definition, it collects any additional positional arguments passed to the function into a tuple.

### *kwargs
- The **kwargs syntax allows a function to accept any number of keyword arguments. 
- When **kwargs is used in a function definition, it collects any additional keyword arguments passed to the function into a dictionary

* Both *args and **kwargs can be used together in a function definition to accept a combination of positional and keyword arguments. 
* The order of parameters should be *args followed by **kwargs
