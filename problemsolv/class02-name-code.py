name = input("Enter your name: ").strip()
a= 5
b= 10
text = input("Enter a word for your banner:") .strip()
width = len(text) + 14 
print(f" the sum of {a} and {b} is {a+b}.")
print(f"Nice to meet you, {name}.")
       # the "f" is called f-string
print("*" * width) 
print(f"*{text}*")
print("*" * width) 
