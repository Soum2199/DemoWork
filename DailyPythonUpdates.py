'''
#Pythoons
The time required to learn Python from a basic understanding to an advanced level varies significantly based on several factors, including: 

• Prior Programming Experience: Individuals with previous coding experience tend to learn faster due to transferable concepts and familiarity with logical thinking. 
• Learning Goals: The depth of learning required depends on whether the goal is basic scripting, web development, data science, machine learning, or advanced framework development. 
• Time Commitment: The amount of dedicated study and practice time per day or week directly impacts the learning pace. Consistent, focused effort yields quicker results. 
• Learning Style and Resources: The effectiveness of learning resources (courses, tutorials, books) and the individual's learning style (visual, auditory, kinesthetic) influence progress. 
• Project-Based Learning: Actively working on projects helps solidify understanding and apply learned concepts, accelerating the learning process. 

Estimated Timelines: 

• Basic Syntax and Scripting: With a commitment of 5-7 hours per week, this could be achieved in approximately 3-6 weeks. This covers fundamental concepts like variables, data types, control flow, functions, and basic file operations. 
• Intermediate Level (e.g., Web Development Fundamentals): Dedicating 8-10 hours per week, reaching this stage might take 2-3 months. This would involve understanding web frameworks like Flask or Django, working with APIs, and database interactions. 
• Advanced Level (e.g., Data Science, Machine Learning, Advanced Frameworks): For more specialized areas requiring 10-15+ hours per week, the learning timeline extends to 4-6 months, or even 6-12 months or more for comprehensive mastery. This includes delving into libraries like NumPy, Pandas, Scikit-learn, or advanced topics in specific frameworks. 

In summary, while the basics of Python can be grasped in a few months, achieving advanced proficiency and applying it effectively in complex domains is an ongoing process that can take a year or more of dedicated learning and practice. 

AI responses may include mistakes.

----------------------------------------------------------------- v/s -------------------------------------------------------



The time required to learn Python from a basic understanding to an advanced level varies significantly based on several factors, including:

    Prior Programming Experience:
    Individuals with previous coding experience tend to learn faster due to transferable concepts and familiarity with logical thinking.
    Learning Goals:
    The depth of learning required depends on whether the goal is basic scripting, web development, data science, machine learning, or advanced framework development.
    Time Commitment:
    The amount of dedicated study and practice time per day or week directly impacts the learning pace. Consistent, focused effort yields quicker results.
    Learning Style and Resources:
    The effectiveness of learning resources (courses, tutorials, books) and the individual's learning style (visual, auditory, kinesthetic) influence progress.
    Project-Based Learning:
    Actively working on projects helps solidify understanding and apply learned concepts, accelerating the learning process. 

Estimated Timelines:

    Basic Syntax and Scripting:
    With a commitment of 5-7 hours per week, this could be achieved in approximately 3-6 weeks. This covers fundamental concepts like variables, data types, control flow, functions, and basic file operations.
    Intermediate Level (e.g., Web Development Fundamentals):
    Dedicating 8-10 hours per week, reaching this stage might take 2-3 months. This would involve understanding web frameworks like Flask or Django, working with APIs, and database interactions.
    Advanced Level (e.g., Data Science, Machine Learning, Advanced Frameworks):
    For more specialized areas requiring 10-15+ hours per week, the learning timeline extends to 4-6 months, or even 6-12 months or more for comprehensive mastery. This includes delving into libraries like NumPy, Pandas, Scikit-learn, or advanced topics in specific frameworks.

In summary, while the basics of Python can be grasped in a few months, achieving advanced proficiency and applying it effectively in complex domains is an ongoing process that can take a year or more of dedicated learning and practice.

-------------------------------------------------------- my part --------------------------------------------------------------------


You're welcome! Here's a compact yet powerful **Python Cheatsheet** to help you become proficient in **1–2 weeks** if you're consistent.

---

## 🐍 Python Cheatsheet — **From Beginner to Expert**

---
'''

### 🧱 **Basics**

```python
# Comments
# Single-line comment
''' Multi-line 
    comment '''
#codes

# print("Try programiz.pro")

# n = 5
# for i in range (1,n+1):
#     print(i*2)
    
# --------------------------------------------------------
def sumNum(num):
    if num <= 1:
        return num
    return num + sumNum(num-1)

print(sumNum(3))

# --------------------------------------------------------
class Person:
    a = 21
    b = "Sweety"
    # a = int(input("Enter age: "))
    # b = input("Enter Name: ")
    
    def showy(self):
        print("Hi, my name is %s and I am now %d years old." % (self.b,self.a) )
        
        
p = Person()
p.showy()
print("-------------------------------")

p1 = Person()
p1.showy()
p1.a = 20
p1.b = "Priyanka"

del p1.b
del p1.a
print(p1.a)
print(p1.b)

a = 5
b = 0.63
c = "hello"
print("a is : %d, b is %0.4f,c is %s" % (a,b,c))
#output:  a is : 5, b is 0.6300,c is hello

a = [1,2,3,4,5]
for hi in a:
    if hi%2 == 0:
        print("Evens %d" % (hi))
    print(hi)
else:
    print("Almost done")

print("-----------------------------\n",len(a))

# Variables
x = 10
name = "Alice"
is_active = True

# Data Types
int, float, str, bool, list, tuple, dict, set, None
```

### 🔁 **Control Flow**

```python
# If/Else
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# While Loop
while x > 0:
    print(x)
    x -= 1

# For Loop
for i in range(5):  # 0 to 4
    print(i)

# Loop Control
break, continue, pass
```

---

### 📦 **Data Structures**

```python
# List
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits[1]  # 'banana'

# Tuple
coords = (10, 20)

# Set
nums = {1, 2, 3}

# Dictionary
user = {"name": "Alice", "age": 25}
user["name"]  # 'Alice'

# Unpacking
a, b = coords  # a=10, b=20
```

---

### 🧮 **Functions**

```python
def greet(name="User"):
    return f"Hello, {name}"

# Lambda
square = lambda x: x ** 2
```

---

### 🧰 **Modules & Imports**

```python
import math
from datetime import datetime

math.sqrt(25)
datetime.now()
```

---

### 📁 **File I/O**

```python
# Writing
with open("file.txt", "w") as f:
    f.write("Hello!")

# Reading
with open("file.txt", "r") as f:
    content = f.read()
```

---

### 🧪 **Exception Handling**

```python
try:
    1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Always runs")
```

---

### 🎯 **Object-Oriented Programming (OOP)**

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I'm {self.name}"

p = Person("Alice")
p.greet()
```

---

### ⚙️ **Advanced Tools (for later in week 2)**

* **List Comprehensions**:

  ```python
  squares = [x**2 for x in range(5)]
  ```

* **Generators**:

  ```python
  def gen():
      yield 1
      yield 2
  ```

* **Decorators**:

  ```python
  def decorator(fn):
      def wrapper():
          print("Before")
          fn()
          print("After")
      return wrapper
  ```

* **Context Managers**, **Virtual Environments**, **Packages (pip)**

---

## ⏱️ How Long to Learn Python?

### ✅ If you're consistent:

| Level                                            | Estimated Time |
| ------------------------------------------------ | ---------------|
| **Basic** (syntax, loops, lists)                 | 3–5 days       |
| **Intermediate** (functions, files, OOP)         | 5–7 more days  |
| **Advanced** (decorators, generators, libraries) | 7–14 more days |

⏳ With **1–2 hours per day**, you can become job-ready in **2–3 weeks** for scripting and automation.

---

## 🔗 Free Resources

* [Python Docs](https://docs.python.org/3/)
* [W3Schools Python](https://www.w3schools.com/python/)
* [Real Python](https://realpython.com/)
* [LeetCode](https://leetcode.com/) for coding practice

---

Would you like this cheatsheet as a downloadable PDF or want a 7-day learning plan?

----------------------  Also, wanna say something like....-----------------------------------

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Earth"))
# print(greet("Grey"))

# age = -63
# name = "Snake"
# is_student = False

# print("Name:", name)
# print("Age:", age)
# print("Student?", is_student)

name = "Alex"
age = 30

print(f"{name} is {age} years old.")
#  the f ones is working right
# print("{name} is {age} years old.")
# Output: {name} is {age} years old.    not correct ❌

Awesome, Subrata! Let’s take this to the next level. Since you’re comfortable with descriptors, metaclasses, and closures, how about we **simulate a mini ORM (Object-Relational Mapper)** using Python’s advanced features?

---

### 🏗️ **Mini ORM Blueprint (Using Metaclasses + Descriptors)**

We’ll build a system where you can define models like this:

```python
class User(Model):
    id = IntegerField()
    name = StringField()
```

And then do things like:

```python
user = User(id=1, name="Subrata")
print(user.save())  # Simulates saving to a database


def sumNum(num):
    if num <= 1:
        return num
    return num + sumNum(num-1)

print(sumNum(3))
```

---

### 🔧 Step-by-Step Breakdown

#### 1. **Field Descriptors**
```python
class Field:
    def __init__(self):
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class IntegerField(Field): pass
class StringField(Field): pass
```

#### 2. **Metaclass to Register Fields**
```python
class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {
            key: value for key, value in attrs.items()
            if isinstance(value, Field)
        }
        for key in fields:
            attrs[key].name = key
        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)
```

#### 3. **Base Model Class**
```python
class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for key in self._fields:
            setattr(self, key, kwargs.get(key))

    def save(self):
        data = {field: getattr(self, field) for field in self._fields}
        return f"Saving to DB: {data}"
```

---

### 🧪 Try It Out

```python
class User(Model):
    id = IntegerField()
    name = StringField()

u = User(id=101, name="Subrata")
print(u.save())  # Output: Saving to DB: {'id': 101, 'name': 'Subrata'}
```
---

Would you like to extend this with:
- Validation (e.g. type checking)?
- Default values?
- Simulated querying like `User.find(id=101)`?

Or maybe flip the script and build a **mini React-like component system in Python** using similar patterns?

You asked for Level 6, Subrata—so let’s crank up the difficulty. These questions dive into Python’s **internals**, **memory model**, **decorator mechanics**, **async behavior**, and **metaprogramming**. Ready to flex your brain?

---

### 🧠 **Python Level 6 Quiz – Expert Mode**

Answer each with the correct option (A–E). Some may have multiple correct answers.

---

**1. What does the following code print?**

```python
def f():
    try:
        return 1
    finally:
        raise Exception("Boom")

print(f())
```

A. `1`     B. `"Boom"`  
C. Raises `Exception: Boom`  
D. `None`   E. SyntaxError

---

**2. What is the output of this code?**

```python
def make_closure():
    funcs = []
    for i in range(3):
        def inner():
            return i
        funcs.append(inner)
    return [f() for f in funcs]

print(make_closure())
```

A. `[0, 1, 2]`    B. `[2, 2, 2]`  
C. `[None, None, None]`  
D. `[1, 2, 3]`    E. `[3, 3, 3]`

---

**3. Which of the following are true about Python’s GIL (Global Interpreter Lock)?**

A. It allows multiple threads to execute Python bytecode simultaneously  
B. It prevents race conditions in CPython  
C. It improves performance in multi-core systems  
D. It is present in PyPy and Jython  
E. It can be bypassed using multiprocessing

---

**4. What does this code print?**

```python
class A:
    def __init__(self):
        self.x = 5

    def __getattr__(self, name):
        return f"Missing: {name}"

a = A()
print(a.x)
print(a.y)
```

A. `5` then `AttributeError`  
B. `5` then `"Missing: y"`  
C. `"Missing: x"` then `"Missing: y"`  
D. `None` then `"Missing: y"`  
E. `"Missing: x"` then `AttributeError`

---

**5. What is the result of this async code?**

```python
import asyncio

async def foo():
    return 42

async def main():
    result = foo()
    print(result)

asyncio.run(main())
```

A. `42`  
B. `<coroutine object foo at ...>`  
C. `None`  
D. `RuntimeError`  
E. `TypeError`

---

**6. Which of the following are valid uses of decorators?**

A. Logging function calls  
B. Memoization  
C. Enforcing argument types  
D. Modifying return values  
E. All of the above

---

**7. What does this code do?**

```python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
```

A. `[1]` then `[1]`  
B. `[1]` then `[1, 1]`  
C. `[1]` then `[]`  
D. `[1]` then `[2]`  
E. Raises `TypeError`

---

**8. Which of the following are true about Python’s `__slots__`?**

A. Saves memory by avoiding `__dict__`  
B. Prevents adding new attributes not listed in `__slots__`  
C. Works with inheritance automatically  
D. Can be used with multiple inheritance without issues  
E. Improves attribute access speed

---

**9. What does this code output?**

```python
class A:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value + 1

a = A()
a.x = 10
print(a.x)
```

A. `10`  
B. `11`  
C. `0`  
D. `None`  
E. Raises `AttributeError`

---

**10. Which of the following are true about Python’s memory management?**

A. Uses reference counting  
B. Has a cyclic garbage collector  
C. `del` always frees memory immediately  
D. Objects can be finalized using `__del__`  
E. Memory leaks are impossible in Python

---

Let me know your answers and I’ll break down your score with full explanations. Ready when you are!


Subrata, you’ve got guts diving into Level 6—this round is where Python starts showing its teeth 🐍. Let’s dissect your answers and see how deep your mastery goes.

---

### 🧠 **Level 6 Python Quiz Results**

| # | Your Answer | Correct Answer | Explanation |
|---|-------------|----------------|-------------|
| 1 | C ✅ | C | `finally` overrides `return`; raises `Exception: Boom`. |
| 2 | B ✅ | B | Closures capture `i` by reference → `[2, 2, 2]`. |
| 3 | B ✅ | B & E | GIL prevents race conditions in CPython; multiprocessing bypasses it. |
| 4 | E ❌ | B | `a.x` exists → `5`; `a.y` triggers `__getattr__` → `"Missing: y"`. |
| 5 | A ❌ | B | `foo()` returns coroutine object; must `await` it to get `42`. |
| 6 | B ❌ | E | Decorators can log, memoize, enforce types, modify returns → all valid. |
| 7 | A or B ✅ | B | Default mutable arg persists across calls → `[1]`, then `[1, 1]`. |
| 8 | B ✅ | A & B | `__slots__` saves memory and restricts attributes. |
| 9 | A ❌ | B | Setter adds `1` → `a._x = 11`; `print(a.x)` → `11`. |
| 10 | E ❌ | A, B & D | Python uses ref counting, cyclic GC, and `__del__`; memory leaks *can* happen.

---

### 🏆 **Score: 5/10**

You nailed some of the trickiest concepts—closures, GIL, mutable defaults, and exception flow. But Python’s async quirks, decorators, and memory model tripped up a few answers. That’s totally normal at this level—these are the kinds of things even seasoned devs debate over.

---

### 🔍 Want to go deeper?

We could:
- Build a custom decorator that enforces type hints  
- Explore async/await with real-world examples  
- Simulate memory leaks using circular references and `__del__`  
- Or even write a metaclass that auto-generates `__repr__` and `__eq__`

Let’s keep pushing boundaries. What do you want to tackle next?


Perfect! Let’s take on something juicy and advanced: **building a decorator that enforces type hints at runtime**. This blends introspection, decorators, and function signatures—exactly the kind of Python wizardry that sets you apart.

---

### 🧙‍♂️ **Goal: Type-Enforcing Decorator**

We want to write a decorator like this:

```python
@enforce_types
def greet(name: str, age: int) -> str:
    return f"Hello {name}, age {age}"
```

And if someone calls `greet("Subrata", "25")`, it should raise a `TypeError` because `"25"` is a string, not an int.

---

### 🔧 Step-by-Step Implementation

#### 1. **Use `inspect` to get function signature**
```python
import inspect
from functools import wraps

def enforce_types(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected = sig.parameters[name].annotation
            if expected is not inspect.Parameter.empty and not isinstance(value, expected):
                raise TypeError(f"Argument '{name}' must be {expected}, got {type(value)}")

        return func(*args, **kwargs)

    return wrapper
```

---

### 🧪 Try It Out

```python
@enforce_types
def greet(name: str, age: int) -> str:
    return f"Hello {name}, age {age}"

print(greet("Subrata", 25))       # ✅ Works
print(greet("Subrata", "25"))     # ❌ Raises TypeError
```

---

### 🧠 Want to Extend It?

We could:
- Enforce return type too (`-> str`)
- Support nested types like `List[int]` or `Dict[str, Any]` using `typing` module
- Add logging or debugging info for mismatches

Or we could pivot to something wild like:
- Building a mini async task scheduler  
- Creating a Python class that mimics React’s component lifecycle  
- Writing a memory profiler using `gc` and `sys`

Love the enthusiasm, Subrata! Since you’re saying “yes” to the challenge, let’s level up this decorator into something truly powerful: **a runtime type checker that supports complex types** like `List[int]`, `Dict[str, Any]`, and even `Optional[str]`.

---

### 🧠 **Advanced Type-Enforcing Decorator (with `typing`)**

We’ll use the `typing` module and `get_type_hints()` to support:

- Basic types: `int`, `str`, `float`
- Containers: `List[int]`, `Dict[str, str]`
- Optional types: `Optional[str]`
- Any: `Any`

---

### 🔧 Full Implementation

```python
import inspect
from functools import wraps
from typing import get_type_hints, get_origin, get_args, Any

def enforce_types(func):
    hints = get_type_hints(func)
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected = hints.get(name)
            if expected:
                if not check_type(value, expected):
                    raise TypeError(f"Argument '{name}' must be {expected}, got {type(value)}")

        return func(*args, **kwargs)

    return wrapper

def check_type(value, expected):
    origin = get_origin(expected)
    args = get_args(expected)

    if expected is Any:
        return True
    elif origin is list:
        return isinstance(value, list) and all(check_type(v, args[0]) for v in value)
    elif origin is dict:
        return (
            isinstance(value, dict) and
            all(check_type(k, args[0]) and check_type(v, args[1]) for k, v in value.items())
        )
    elif origin is Union:
        return any(check_type(value, arg) for arg in args)
    else:
        return isinstance(value, expected)
```

---

### 🧪 Try It Out

```python
from typing import List, Dict, Optional

@enforce_types
def process(name: str, scores: List[int], meta: Dict[str, str], nickname: Optional[str] = None):
    return f"{name} ({nickname}) scored {scores} with meta {meta}"

print(process("Subrata", [90, 85], {"level": "6"}, nickname="S"))  # ✅
print(process("Subrata", [90, "oops"], {"level": "6"}))            # ❌ TypeError
```

### 🔮 What’s Next?

We could:
- Add **return type enforcement**
- Build a **custom DSL** for defining types
- Create a **debug mode** that logs mismatches instead of raising errors
- Or pivot to something wild like:
  - A **mini async job queue**
  - A **Python class that mimics React’s state and props**
  - A **SQL query builder using Python classes**

Pick your poison—or I’ll surprise you with something spicy.

Absolutely, Subrata! I’ve reshuffled your Level 7+ Python quiz to keep things fresh and unpredictable. Here’s your new lineup of brain-benders:

---

### 🧠 Advanced Python Quiz (Shuffled Edition)

1. **What does this code do?**
   ```python
   def f(x=[]):
       x.append(1)
       return x

   print(f())
   print(f())
   ```
   - [ ] [1] then [1]
   - [ ] [1] then [1, 1]
   - [ ] [1] then []
   - [ ] [1] then [2]

2. **What does this async code output?**
   ```python
   import asyncio

   async def foo():
       return 42

   async def main():
       result = foo()
       print(result)

   asyncio.run(main())
   ```
   - [ ] 42  
   - [ ] `<coroutine object foo at ...>`  
   - [ ] None  
   - [ ] RuntimeError  

3. **What does this code output?**
   ```python
   class A:
       def __init__(self):
           self._x = 0

       @property
       def x(self):
           return self._x

       @x.setter
       def x(self, value):
           self._x = value + 1

   a = A()
   a.x = 10
   print(a.x)
   ```
   - [ ] 10  
   - [ ] 11  
   - [ ] 0  
   - [ ] None  

4. **What is the purpose of the `__new__` method in Python?**
   - [ ] To initialize an instance of a class  
   - [ ] To create a new instance of a class  
   - [ ] To delete an instance of a class  
   - [ ] To override the default behavior of a class  

5. **What does this code output?**
   ```python
   class Meta(type):
       def __new__(cls, name, bases, dct):
           dct['greet'] = lambda self: f"Hello from {name}"
           return super().__new__(cls, name, bases, dct)

   class A(metaclass=Meta):
       pass

   a = A()
   print(a.greet())
   ```
   - [ ] Hello from A  
   - [ ] Hello from Meta  
   - [ ] AttributeError  
   - [ ] TypeError  

6. **What does the following code output?**
   ```python
   x = [1, 2, 3]
   y = x
   x.append(4)
   print(y)
   ```
   - [ ] [1, 2, 3]  
   - [ ] [1, 2, 3, 4]  
   - [ ] [4]  
   - [ ] None  

7. **What does the following code output?**
   ```python
   x = (1, 2, 3)
   y = x
   x += (4,)
   print(y)
   ```
   - [ ] (1, 2, 3)  
   - [ ] (1, 2, 3, 4)  
   - [ ] (4,)  
   - [ ] None  

8. **What does the following code output?**
   ```python
   x = [1, 2, 3]
   y = x[:]
   x.append(4)
   print(y)
   ```
   - [ ] [1, 2, 3]  
   - [ ] [1, 2, 3, 4]  
   - [ ] [4]  
   - [ ] None  

9. **What does the following code output?**
   ```python
   x = [1, 2, 3]
   y = x
   x += [4]
   print(y)
   ```
   - [ ] [1, 2, 3]  
   - [ ] [1, 2, 3, 4]  
   - [ ] [4]  
   - [ ] None  

10. **What does the following code output?**
    ```python
    x = [1, 2, 3]
    y = x
    x = x + [4]
    print(y)
    ```
    - [ ] [1, 2, 3]  
    - [ ] [1, 2, 3, 4]  
    - [ ] [4]  
    - [ ] None  

11. **What does the following code output?**
    ```python
    x = [1, 2, 3]
    y = x
    x = x * 2
    print(y)
    ```
    - [ ] [1, 2, 3]  
    - [ ] [1, 2, 3, 1, 2, 3]  
    - [ ] [2, 4, 6]  
    - [ ] None  

12. **What does the following code output?**
    ```python
    x = {1, 2, 3}
    y = x
    x.add(4)
    print(y)
    ```
    - [ ] {1, 2, 3}  
    - [ ] {1, 2, 3, 4}  
    - [ ] {4}  
    - [ ] None  

13. **What does the following code output?**
    ```python
    x = [1, 2, 3]
    y = x.copy()
    x.append(4)
    print(y)
    ```
    - [ ] [1, 2, 3]  
    - [ ] [1, 2, 3, 4]  
    - [ ] [4]  
    - [ ] None  

14. **What does this code output?**
    ```python
    class A:
        def __init__(self):
            self.x = 5

        def __getattr__(self, name):
            return f"Missing: {name}"

    a = A()
    print(a.x)
    print(a.y)
    ```
    - [ ] 5 then AttributeError  
    - [ ] 5 then 'Missing: y'  
    - [ ] 'Missing: x' then 'Missing: y'  
    - [ ] None then 'Missing: y'  

15. **What does the following code output?**
    ```python
    def gen():
        yield from ['a', 'b', 'c']
        yield 'd'

    print(list(gen()))
    ```
    - [ ] ['a', 'b', 'c']  
    - [ ] ['a', 'b', 'c', 'd']  
    - [ ] ['d', 'a', 'b', 'c']  
    - [ ] ['a', 'b', 'c', 'd', 'e']  


Let me know if you want to turn this into a timed challenge, get hints, or dive deeper into any of the concepts. You're crushing it at this level!

Your Python decorators quiz is being prepared and will be ready shortly! Here's a starting set of 15 questions to challenge your knowledge. If you'd like more, feel free to ask for additional quizzes.

🧠 Python Decorators Quiz

1. What is a decorator in Python?

A) A function that modifies another function
B) A type of loop
C) A class method
D) A built-in Python module 
Answer: A

2. Which symbol is used to apply a decorator to a function?

A) #   B) @  
C) &   D) *
Answer: B

3. True or False:

Decorators can only be used with functions, not classes. 
Answer: False

4. What will the following code output?

def decorator_func(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()

Answer: Before function call Hello! After function call

5. Fill in the blank:

A decorator is a ______ that takes another function as an argument and returns a new function.
Answer: Function

6. Which of the following is a valid use case for decorators?

A) Logging B) Authentication C) Timing execution D) All of the above
Answer: D

7. What does functools.wraps do in a decorator?

A) Adds logging
B) Preserves metadata of the original function
C) Executes the function twice
D) Converts the function to a class
Answer: B

8. True or False:

You can apply multiple decorators to a single function.
Answer: True

9. What is the output of this code?

def outer(func):
    def inner():
        print("Inner function")
    return inner

@outer
def greet():
    print("Hello!")

greet()

Answer: Inner function

10. Which module provides built-in decorators like @staticmethod and @classmethod?

A) functools   B) types
C) builtins   D) None (they're part of Python's core syntax)
Answer: D

11. What is the purpose of @property decorator?

A) To define a class method
B) To make a method behave like an attribute
C) To hide a method
D) To create a static method
Answer: B

12. Fill in the blank:

The @classmethod decorator requires the first argument of the method to be ______.
Answer: cls

13. Which of the following decorators is used to cache function results?

A) @wrapsB) @lru_cacheC) @staticmethodD) @property
Answer: B

14. What is the output of this code?

def repeat(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat
def say_hi():
    print("Hi!")

say_hi()

Answer: Hi! Hi!

15. True or False:

Decorators can be used to modify the behavior of functions at runtime.
Answer: True


You got it, Subrata! The 14th question is about understanding how a decorator modifies a function’s behavior. Here's the code again for clarity:

```python
def repeat(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat
def say_hi():
    print("Hi!")

say_hi()
```

### ✅ **Answer:**
```
Hi!
Hi!
```

### 💡 Why?
The `repeat` decorator wraps the `say_hi` function so that it gets called twice whenever `say_hi()` is invoked. The decorator replaces the original function with `wrapper`, which calls `func()` (i.e., `say_hi`) two times.

If you want to take this further, I can show you how to make a decorator that repeats a function *n* times using arguments. Want to try that next?

-======================================-------------------=======================--------------------------------------===================---


## 🌱 Want to try one tiny Python example right now?

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))

# -----------------------------------------------------------------------
def sumNum(num):
    if num <= 1:
        return num
    return num + sumNum(num-1)

print(sumNum(3))

# --------------------------------------------------------------------
class Person:
    a = 21
    b = "Sweety"
    # a = int(input("Enter age: "))
    # b = input("Enter Name: ")
    
    def showy(self):
        print("Hi, my name is %s and I am now %d years old." % (self.b,self.a) )
        
        
p = Person()
p.showy()
print("-----------------------------------")

p1 = Person()
p1.showy()
p1.a = 20
p1.b = "Priyanka"

del p1.b
del p1.a
print(p1.a)
print(p1.b)

a = 5
b = 0.63
c = "hello"
print("a is : %d, b is %0.4f,c is %s" % (a,b,c))
#output:  a is : 5, b is 0.6300,c is hello

a = [1,2,3,4,5]
for hi in a:
    if hi%2 == 0:
        print("Evens %d" % (hi))
    print(hi)
else:
    print("Almost done")

print("-----------------------------------\n",len(a))

def summy(a, b):
    return a+b
    
print(summy(2,3))
print(summy(5,8))

def greet(names = "Guest"):
    return f'Hello, {names}!.'
    
print(greet("Sweety"))
print(greet("Soumya"))
print(greet())
print(greet("Sai"))

def summy2(*args):
    suum = sum(args)
    return f'The sum: {suum}'
    
print(summy2(1,2))
print(summy2(1,2,3,4))

def displaying(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}: {v}.\n")
        

# displaying(username: "Sweety", age: 25, city: "Mumbai")
displaying(username= "Sweety", age= 25, city= "Mumbai")
#Note: here = sign is helping to evaluate the entered value and not colon symbol.

def vary(s, *args):
    print("First one: ",s)
    for item in args:
        print("Followed by: ",item)
        
vary('G','O','O','D',' ','D','A','Y')

ar = [10,20,30]
# print(ar)
# ar.push(4)  #it gives an error as its not a property
ar.append(40)
print(ar)
ar.pop(0)  # it will look for index values having any digits
print(ar)

print(3**2)
print(3*2)
print(3**3)
print(3*3)
print("-------------------------\n")
s = "Python Singh"
print(s)
print(len(s))

def squared(word, size):
    i=0
    row = ""
    while i < size ** 2:
        if i>0 and i % size == 0:
            print(row)
            row = ""
        row = row + word[i % len(word)]
        i = i+1
    print(row)
    
squared("yatch", 3)
squared("tysvm", 6)

import calendar
yy = 2025
mm = 9
print(calendar.month(yy,mm))
# print(calendar.mon(yy,mm))  #errror
print(calendar.calendar(yy))

# x = [12, 24, 36]
# y = x
# y.append(48)
# # print(y)
# print(x)

# https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1?page=1&category=Strings&sortBy=submissions
class Solution:
    def reverseWords(self, s):
        # code here
        par = s.split(".")
        word = [w for w in par if w]
        word.reverse()
        return ".".join(word)
        
# https://www.geeksforgeeks.org/problems/binary-search-1587115620/1
class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        l,r = 0, len(arr) - 1
        res = -1
        
        while l <= r:
            # mid = (l+r)//2
            mid = l+(r-l)//2
            if arr[mid] == k:
                res = mid
                r = mid-1
                # return mid
                
            elif arr[mid] > k:
                r = mid-1
                
            else:
                l = mid+1
                
        return res
        # return -1
        
class Parent:
     def greet(self):
         print("Hello Parent")

class Child(Parent):
    def greet2(self):
        print("hello chilldren")
        
c = Child()
c.greet()
c.greet2()

a = [1,2 ,3]
print(a)
# a.extend([4])   # o/p: [1, 2, 3, 4]
a.append(4)
print(a)

a = 3+2
b = "String"
print(b)
print(True if a%2 == 0 else False)

s = "GoodEveningsHere"
# s = "interpretersing"
print(s[1:7])
print(s[2:])
print(s[:8])
print(s[:-1])
print(s[-1:])
print(s[::])

s = "Sweety"
print(s[::-1])

i=1
while True:
  if i%3 == 0:
    break
  print(i)
  # i += 1
  i = i+1

def genie():
  yield 1
  yield 2
  yield 3
  
gen = genie()
print(next(gen))

#x = "nilesh"
x = "soumya"
print(x[2:5])
#---------------------
a= [1,2,3]
b = a[:]
b.append(4)
#print(b)
print(a)

#print("Try programiz.pro"[-5:])
print("Python"[-5:])
print("DataScience"[-5:])
print("DataScience"[6:])

a=5
b=2
c = 5*2+3
a += 13-2
print("answer is " , a)
#answer is 16

rows = int(input ('Enter the number '))
#print(rows)
for i in range(rows):
    for j in range(i):
        print(i, end=" ")
        
    print(' ')

rows = int(input ('Enter the number '))
b =0
#print(rows)

for i in range(rows, 0, -1):
    b += 1
    for j in range(1,i+1):
        #print(i, end=" ")
        print(b, end=" ")
        
    print('\r')

#leetcode problem no 2351, link:  https://leetcode.com/problems/first-letter-to-appear-twice/
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seel = []
        for c in s:
            # return c
            if c in seel:
                return c
            else:
                seel.append(c)


count = 0
for i in range (5):
    if i % 2 == 0:
        count += i
        
print(count)
# o/p : 6

```

