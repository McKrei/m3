import json



with open("data", encoding="UTF-8") as file:
   sting = file.read()
   data = json.loads(sting)


print(type(data))
print((data))
