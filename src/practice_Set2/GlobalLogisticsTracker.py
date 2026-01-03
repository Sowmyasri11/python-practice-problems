
ships=[]

number_of_ships=int(input("Enter number of ships: "))

for s in range(number_of_ships):
    ship={"containers": [] }
    print(f"\n  ship { s + 1} ")

    number_of_containers=int(input("Enter number of containers: "))

    for c in range(number_of_containers):
        container={"items": [] }
        print(f"\n  container {c + 1} ")

        number_of_items=int(input("Enter number of items: "))

        for i  in range(number_of_items):
            print(f"\n  item {i + 1} ")

            name=input("Enter item name: ")
            item_type=input("Enter item type: ")
            weight=int(input("Enter item weight: "))
            destination=input("Enter destination code : ")


            container["items"].append({
                "name": name,
                "item_type": item_type,
                "weight": weight,
                "destination": destination
            })

        ship["containers"].append(container)
    ships.append(ship)


def flatten_items(ships):
    return [
        item
        for ship in ships
        for container in ship["containers"]
        for item in container["items"]
    ]


result=[
    item["name"]
    for item in flatten_items(ships)
    if item["item_type"]=="Fragile"
       and item["destination"]=="LON"
       and item["weight"] > 10

]
print(result)

