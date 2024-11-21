current_name = "moshe"
while current_name != "quit":
    current_name = input("What is your name: ")
    if current_name == "eden":
        continue
    if current_name == "ronen":
        break
    print(f" hello {current_name}")
else:
    print("Thank you for playing")

i = 40

for i in range(5):
    print(i)

print("**************************")
print(i)
print("**************************")
