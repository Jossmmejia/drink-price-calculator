"""product = [
          {"product":"coffee","price":4000},
          {"product":"tea","price":3500},
          {"product":"juice","price":5000}
]

drink = input ("What do you want?")
cant = int(input("How many do you want?"))

if drink == "coffee" and cant >= 1:
    total = cant * product [0]["price"]

elif drink == "tea" and cant >= 1 :
    total = cant * product [1]["price"]

elif drink == "juice" and cant >= 1 :
    total =  cant *product [2]["price"] 

else: 
    print("not available")
    total = 0
print(f"total is: {total} ") """



product = [
    {"product": "coffee", "price": 4000},
    {"product": "tea", "price": 3500},
    {"product": "juice", "price": 5000}
]

drink = input("What do you want? ").lower()
cant = int(input("How many do you want? "))

for p in product:
    if drink == p["product"]:
        total = cant * p["price"]
        print(f"Total is: {total}")
        break
else:
    print("Not available")