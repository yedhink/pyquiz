# Intro
Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare
their type. Every variable in Python is an object.
Unlike other programming languages, Python has no command for
declaring a variable. A variable is created the moment you first assign
a value to it.
A variable can have a short name (like x and y) or a more descriptive name
(age, carname, total_volume).  

## Rules for Python variables:  
* A variable name must start with a letter or the underscore character.  
* A variable name cannot start with a number.  
* A variable name can only contain alpha-numeric characters and underscores  
* Variable names are case-sensitive (age, Age and AGE are three different variables).each variable is assigned at a specific memory address  

```
|     | |     |
|     | |     |
|abhi | |62   |
|name | |roll |
|_____| |_____|
 1000    1001
```  


## data types -
* Numbers      :  
	* int     = 0-9 or any other comnination of 0-9 like 99,188,10 etc  
                    = cannot include numbers with decimal part  
	* float   = can hold any number with a decimal value  
	* complex = 1+2j  
* Strings      :  
	* str     = any combinations of valid characters  
                  = "Yedhin"  
                  = "123Yedhin@@@1"  
                  = "yedhin1998@gmail.com"  
                  = "ikigai@github.com"  
* Lists        :  
	1) list   = list is a data structure which can hold any data type  
                  = [1,2,3,'a',"abc",[4,5,6]]  
* Tuples       : (1,2) or 1,2,3  
* Sets  
* Dictionaries : key-value pairs  

## operators
Arithmetic Operators ( +   , -  , *  , /  , // , % , ** )  
Bitwise Operators    ( &   , |  , ^  , >> , << , ~      )  
Assignment Operators ( =   , += , -= , /= , //= etc.    )  
Comparison Operator  ( ==  , != , >  , <  , >= , <=     )  
Logical Operators    ( and , or , not                   )  
Identity Operators   ( is  , is not                     )  
Membership Operators ( in  , not in                     )  

### for more info :-
* lists - [click here](https://raw.githubusercontent.com/yedhink/pyquiz/master/lists.py)
* tuples - [click here](https://raw.githubusercontent.com/yedhink/pyquiz/master/tuples.py)
