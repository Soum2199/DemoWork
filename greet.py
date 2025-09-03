# Write Python 3 code to greet the person

def greet(names = "Guest"):
    return f'Hello, {names}!.'
    
print(greet("Sweety"))
print(greet("Soumya"))
print(greet())
print(greet("Sai"))

# f is important for evaluation purpose, otherwise the variable names would not be evaluated.