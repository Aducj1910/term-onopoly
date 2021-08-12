# {"color": "brown", "name": "Old Kent Road", "price": 60, "rent": 2, "rent_with_house": {1: 10, 2: 30, 3: 90, 4: 160, 5: 250}, "house_cost": 50}

list = []

for i in range(22):
	color = input("color ")
	name = input("name ")
	price = int(input("price "))
	rent = int(input("rent "))
	h1 = int(input("... "))

	h2 = int(input("... "))

	h3 = int(input("... "))

	h4 = int(input("... "))

	h5 = int(input("... "))
	housecost = int(input("house cost "))

	dict = {"color": color, "name": name, "price": price, "rent": rent, "rent_with_house": {1: h1, 2: h2, 3: h3, 4: h4, 5: h5}, "house_cost": housecost}
	list.append(dict)


print(list)