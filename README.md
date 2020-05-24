# CSE3120-OOP1
Object Oriented Programming 1

##Definitions

__Objected Oriented Programming (OOP)__ is the process of
implementing object oriented design in a functional program.

__Object Oriented Design (OOD)__ is the process of converting 
identifiable objects and their interactions into a template
to construct any number of similar objects with similar properties
and interactions.

A ___class___ is a model of an object. Classes contain the
_attributes_ and _behaviour_ which are present in all objects
made from this model. A class can be thought of as a template or
blueprint for making an object.
```
    - An example of a class is a student
    
    - An attribute is a property or characteristic that the object
possesses. It is stored as a variables within the object
        -The student class has an attribute, student ID number
    
    -A behaviour is called a method and is something the object can
do. It is represented as a function with the object
        -The student class has a method, take notes
```

An ___object___ is a unique set of data and functions
_instantiated_ from a class. An object accesses attributes and
methods using _dot notation_, which identifies the object, then
calls the method within it.

## Why OOP?
1. __Abstraction__F is the process of setting the level of detail
and complexity to what is appropriate for the given task
   - EG. a student has many properties like height but only
   ones that relevant to the task, such as calculating an avg
   is needed (i.e Student ID)
   
2. __Aggregation And Composition__ is the process of creating
a complex object by collecting several other objects. Aggregates
have no relation between the collected objects. s
(I.E, the cards in a player's hands). Whereas, objects in a composite
are interacting to create a more complex object or function.
The removal of an object in a composite can compromise the functionality
of the composite object.
(I.E, a bike is composed of a frame, a chain, pedals wheels, e.t.c
if you loose one, you can't bike as well, maybe can still bike
though :)).

3. __Polymorphism__ is the ability to instantiate objects with
different values for class attributes.
    * for example, a honda civic is made from the civic class but
    can have different exterior colour attributes and interior finish
    material attributes
    * the advantage of polymorphism is that the program can
    construct many similar objects in less lines of code.

4. __encapsulation__ is the process of protecting or hiding
data and code so that other parts of the program can only interact
with the data in pre programmed pathways. Often times these
interactions are aggregated into an interface. The interface is a
collection of setter and getter methods. (These are sometimes called
modifier and accessor methods) These methods are the primary pathway
to modify or retrieve object attributes.
    * For example a protective case encapsulates the components of
    a computer and the only interaction is through the input and
    output ports (buttons???)
    * It is important to only create setter and getter methods
    for attributes that are needed outside of the object

5. __inheritance__ is when one class references and builds upon
another class. The class inherits all attributes and methods
of the referenced class which is called the *parent* class. The
class that does the referencing is called the *child* class
or subclass.

``` python5
class parent:
    def __init__(self, name):
        self.name = name
        
    def aMethod(self):
        pass
        
class child(parent):
    def __init__(self, name, age):
        parent.__init__(self, name)
        self.age = age
```
 Inheritance reduces the amount of copied attributes and methods
 between classes. python allows multiple inheritances, however; 
 many languages only allow one.

``` python4
class myClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        
        //setter methods (modifier)
    def setX(self, x):
        self.x = x
        self.position = (self.x, self.y)

    def setY(self, y):
        self.y = y
        self.position = (self.x, self.y)
        
        //getter method (accessor)
    def getPos(self):
        return self.pos

```




## Unified Modeling Language
A standardized modeling language that has the same notational system
when describing data management and software design. This language
is programming agnostic and does not require a programming 
background to utilize. It is composed of three diagram types:
structure, behaviour and interactions.

Note: while software devs use all three types, we will only
focus on structure.

A __class diagram__ contains the name of the class, the attributes
and the methods 

| Bank Account |  |
| --- | --- |
| _Attributes/Methods_ | _Value_ |
| - | - |
| Account# | Int |
| Balance$ | Float |
| - | - |
| Withdraw(val) | Float |
| Deposit(val) | Float |
| getBalance | Float |

##Special Variables And Magic Methods
__Special Variable__ found in classes and objects have properties 
that already built-in attributes within the programing
language.
    * A special variable in python is denoted with two __ before
    and after the variable name.
    * These variables can also be called double underscore variable
    or dunder variables

__Magic Methods__ are methods within a class that redefine
or manipulates special variables. 

```
class myClass:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return "The class name is " + self.name
        
```