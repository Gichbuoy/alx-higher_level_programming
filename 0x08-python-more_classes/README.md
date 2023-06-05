### Classes
- Formal description on how an object is designed(Attributes and methods)

### Object
- Instance of a class
- Defined by a class


### First Class Everything
* Everything is a class in python
* Everything is treated the same way
* All objects are 'first classs'


### Attributes
* Variables that belong to an object
* Accessed and modified using dot . notation (object.attribute)

### getattr()
- Built-in function that allows you to get value of an attribute from an object
- Takes 2 arguments:
	* Object from which you want to retrieve the attribute value
	* Name of attribute as a string
	- eg: getattr(object, attr_name, default_value)

### Data Encapsulation
- Bundling of data with the methods that operate on that data
- Combining attributes & methods
- Uses Getters and Setters
	* Getters - Retrives/Accesses values of attributes
		- Just returns the values. Doesn't modify
	* Setters - Changes values of attributes
- get_name()
- set_name()


### Information Hiding
- Provide controlled access through well defined interfaces
- Impelemented using access modifiers
	* Private
	* Protected
	* Public

### Data Abstraction
- process of representing the essential features of an object while hiding impelemention details
- present if both data hiding and encapsulation is used
* Data Abstraction = Data Encapsulation + Data Hiding

- 
