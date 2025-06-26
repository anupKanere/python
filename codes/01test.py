class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))
print(issubclass(Parent, Child))
