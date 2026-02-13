# Chapter 1 – Encapsulation Using Polymorphism and Loose Coupling

## Overview

This project contains Python scripts demonstrating core Object-Oriented Programming (OOP) concepts based on Chapter 1 of *Mastering Python Design Patterns (3rd Edition)*.

The goal of this project is to demonstrate foundational design principles in Python, including:

- Encapsulation
- Polymorphism
- Abstract Classes
- Interfaces
- Duck Typing
- Composition
- Loose Coupling

Each script focuses on one specific concept and can be executed independently.

---

## Project Structure

```
.
├── abstractclass.py
├── composition.py
├── encapsulation.py
├── encapsulation_bis.py
├── interface.py
├── interface_bis.py
└── loose_coupling.py
```

---

## File Descriptions

### abstractclass.py
Demonstrates abstract base classes using the `abc` module.  
Shows how subclasses must implement abstract methods and how polymorphism works through a shared method.

### composition.py
Demonstrates composition (has-a relationship).  
A class contains another class instead of inheriting from it.

### encapsulation.py
Demonstrates encapsulation using private variables and getter/setter methods to control access to internal data.

### encapsulation_bis.py
Demonstrates encapsulation using `@property` and `@setter` decorators for cleaner attribute control.

### interface.py
Demonstrates how abstract classes can act as interfaces in Python by enforcing method implementation.

### interface_bis.py
Demonstrates duck typing.  
Objects are treated based on the methods they provide rather than their class type.

### loose_coupling.py
Demonstrates loose coupling by making a class depend on an abstraction instead of a concrete implementation.

---

## Tech Stack

Language:
- Python 3.x

Libraries Used:
- Python Standard Library
- `abc` module (for abstract base classes)

No external packages or frameworks are required.

---

## Requirements

- Python 3.8 or higher recommended
- Command Line / Terminal
- Optional: VS Code or any Python IDE

---

## Installation

1. Install Python from:
   https://www.python.org/downloads/

2. Verify installation:

   python --version

   or

   py --version

You should see Python 3.x installed.

---

## How to Run

1. Place all `.py` files inside one folder.

2. Open Command Prompt or Terminal.

3. Navigate to the project folder:

   cd path\to\your\folder

4. Run any script individually:

   python abstractclass.py

You may also run on terminal:

   python composition.py  
   python encapsulation.py  
   python encapsulation_bis.py  
   python interface.py  
   python interface_bis.py  
   python loose_coupling.py  

Each file runs independently and prints output in the console.

---

## Learning Outcomes

After completing this project, you should understand:

- How encapsulation protects internal data
- How polymorphism allows flexible behavior across different classes
- How abstract classes enforce design contracts
- How interfaces can be simulated in Python
- How duck typing works in dynamic typing
- Why composition can be preferred over inheritance
- Why loose coupling improves flexibility and maintainability

These principles serve as a foundation before moving into more advanced design patterns.
