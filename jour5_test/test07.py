def test07(name, age=18):
    
    print("Hello", name, "- you are", age)


test07("Alice", 22)
test07("Bob")
age = 20
name = "John"
test07(name)
test07(age, name)