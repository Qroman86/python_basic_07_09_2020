items_list = []

properties_map = {"название": "str", "цена": "int", "количество": "int", "eд": "str"}

index = 1
while True:
    print(f"\n\nВведите данные о товаре №{index}")
    item_data = {}
    #to do - input data about items
    for property in properties_map.keys():
        property_value = ""
        if properties_map.get(property) == "str":
            property_value = input(f'Введите информацию о характеристике "{property}":\n')
        elif properties_map.get(property) == "int":
            while True:
                property_value = input(f'Введите информацию о характеристике "{property}"\n')
                if not property_value.isdigit():
                    continue
                else:
                    property_value = int(property_value)
                    break
        item_data[property]=property_value
    item_tuple = (index, item_data)
    items_list.append(item_tuple)

    is_next_item = input('Ввести данные о следующем товаре(y/n)?:\n')
    if is_next_item != "y":
        break
    index += 1

#print data about items
print("\nВведенная информация о товарах")
print(items_list)

#prepare analytics
analytics_data = {}
for property in properties_map.keys():
    property_values = set()
    for item_tuple in items_list:
        property_map = item_tuple[1]
        property_value = property_map[property]
        property_values.add(property_value)
    property_values_list = list(property_values)
    analytics_data[property] = property_values_list

print("\nСводная аналитика о товарах")
print(analytics_data)