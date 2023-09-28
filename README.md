# Object Oriented Programming
 Basics of object oriented programming


# OBJECTS

**Identity, attributes and behaviours** are the three things that describe objects in OOP. Every object is sel-contained and has its own identity, attriburtes and behaviour.
Can objects represent non phisical things? YES. Everything that has identity, attributes and behaviour can be represented as an object. To answer this question you can try to answer a simple questioo , is it a **noun?**
If the answer is yes probably it can be an **object**.

## CLASS
Is the definition, template of what an object will be. It defines how the object will behave and what attributes will it have. 

A class will always have:
- **Name**
- **Attributes/propertoes**
- **Behaviour/operations/methods** they are procedures that perform a certain action and return a value. Methods are defined as part of a class.

The object as created throuh **instantiation** so an instance of the object is created. To create an object we need a class at first. Strings, dates etc are already classes in most progrmaming languages. 

## FUNDAMENTALS (APIE)

- **Abstractions:** we focus on the essential qualities of something and we do not focus on specifics. It manas that we are spearating from a specific instance. 
For example each person has a name, height, color, etnicity etc. I do not need to provide for example a material attribute as it wil not be needed. the same goes if for example my program is meant to calculate the BMI of a person i will just need height and weight and not the color of the skin.
- **Encapsulation:** in the same class we will place/ bundle the class identity, methods and attributes. the methods will opeerate just on the data contained in that particulat class.
One reason to do thta is to restric access to that object component. An object should not make anything about itself available. This is to assure stability and safety. 
In this way we can recue dependencies between various parts of the application to make changes more managable.
- **Inheritance:** if i need to create a new class i can inherite the attributes or methods of another existing class in this way i can avoid to to rewrite the code entirely each time. So i can inherite the attributes and methods and add new ones as well. makes everything easier as i can change code in just one place. 
Mlutipla inheritance can be used but in general single inheritance is prefereble.
- **Polymorphism:**(havind multiple forms). It is just a way to say that we can obtain a class in different way. 
Method overwriting and method overloading are the two types od implementin the polymorphism that we may encouter. 

How **overloading** works?
We assing a method with the same name but with a different set of parameters. This gives us flexibility to assign parameters.



#  GENERAL PROCEDURE
- 1. Gather requirements
- 2. Describe the application
- 3. Identify the main objects
- 4. Describe the interactions
- 5. **Create a class diagram**


## 1.REQUIREMENTS

**Functional** requirement: decribe the features that an application should have 
Typically such requirements are desined by answering listing all the things that **the application must do...**
**Non-functional** requirements: describe required characteristics of the applications. 
Usability, affordability, availability etc. But here we have to place just the absolute minimum requirements.

## FURPS
In software engineering, the FURPS model is a framework for categorizing and organizing software requirements. FURPS stands for:

1. **Functionality:** This category focuses on the features and capabilities that the software should provide. It includes requirements related to the primary functions of the software, user interactions, and system behavior. In the context of Object-Oriented Programming (OOP), this often translates into defining classes, methods, and objects that encapsulate the required functionality.

2. **Usability:** Usability requirements pertain to how user-friendly and intuitive the software should be. It encompasses aspects like user interfaces, accessibility, and user experience. In OOP, this may involve designing classes and methods that facilitate a user-friendly interaction with the software.

3. **Reliability:** Reliability requirements address the software's ability to perform consistently and correctly. It includes aspects like error handling, fault tolerance, and system stability. In OOP, this might mean creating classes that handle exceptions gracefully or ensuring that critical functionality is robust and dependable.

4. **Performance:** Performance requirements deal with the software's speed, responsiveness, and efficiency. It covers factors like response times, throughput, and resource utilization. In OOP, optimizing algorithms and data structures within classes can help meet performance goals.

5. **Supportability:** Supportability requirements focus on the software's ease of maintenance, manageability, and extensibility. It includes aspects like documentation, modularity, and adaptability. OOP principles, such as encapsulation and abstraction, can facilitate supportability by isolating changes to specific classes and modules.

Additionally we cam add four more cathegories:
- **Implementations**
- **Design**
- **Interface**
- **Physical requirements**


NOT ALL THE REQUIREMENTS WILL BE USEFULL FOR OUR APPLICATION, IT IS TOTALLY NORAML TO LEAVE SOME OF THESE REQUIREMENTS FREE WHEN PLANNING.

## 2.USE CASES/APPLICATION

The usa cases are basically a short description of what our application should do. In general it is good to write usa cases as paragraphs with title and a description of what should happen., the scenario. The scenario typically has an actor.

- Title:
- Actor:
- Scenario:

In use cases we can also add alternative flows in order to take into accouint when something does not work.

It is good to spend some time to identify the actors as in some cases we may have more than one actor.

## 3. IDENTIFYING THE OBJECTS

We shoudld write a conceptual model in order to identify the objects. To identify the objects we shpuld go through our use cases and find the nouns.

To apply Object-Oriented Programming principles to address FURPS requirements, you can:

- **Use Classes:** Design classes that encapsulate related functionality and attributes. This supports the modularity and organization required to meet FURPS objectives.

- **Leverage Inheritance:** Inheritance can help in reusing and extending functionality while maintaining consistency. For example, you can create subclasses that inherit features from a base class and add specialized behavior.

- **Encapsulate Data:** Use encapsulation to hide implementation details and protect data integrity. This aligns with reliability and usability requirements by ensuring that data is handled correctly and safely.

- **Implement Interfaces:** Implementing interfaces and defining clear method signatures can enhance usability and supportability. This allows clients to interact with objects in a standardized way.

- **Optimize Algorithms:** In cases where performance is a concern, design efficient algorithms within your classes. Consider data structures and algorithms that meet performance requirements.

- **Document and Comment:** Proper documentation of classes, methods, and code comments supports supportability. It helps developers understand and maintain the software.

Remember that FURPS requirements can vary greatly depending on the specific project and its context. Your application of Object-Oriented Programming should align with the particular FURPS requirements of your software project to ensure that the resulting software meets its goals effectively and efficiently.


## 4. RESPONSAVILITIES


# SOLID PRINCIPLES

1. **S ingle responsability principle** NO God Objects
2. **O pen/Closed principle**
3. **L iskov substitution method**
4. **I nterfave segregation principle**
5. **D ependency inversion principle**