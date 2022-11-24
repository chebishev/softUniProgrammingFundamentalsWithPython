def legendary_item_obtained(key_material):
    legendary_item = ""
    if key_material == "shards":
        legendary_item = "Shadowmourne"
    elif key_material == "fragments":
        legendary_item = "Valanyr"
    elif key_material == "motes":
        legendary_item = "Dragonwrath"
    return f"{legendary_item} obtained!"


def check_for_key_material(key_material):
    if key_material == "shards" or \
            key_material == "fragments" or \
            key_material == "motes":
        return True


materials_list = input().split()
materials_collection = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while True:
    for index in range(0, len(materials_list), 2):
        quantity = int(materials_list[index])
        material = materials_list[index + 1].lower()
        if material not in materials_collection.keys():
            materials_collection[material] = 0
        materials_collection[material] += int(quantity)
        if check_for_key_material(material):
            if materials_collection[material] >= 250:
                print(legendary_item_obtained(material))
                materials_collection[material] -= 250
                obtained = True
                for key, value in materials_collection.items():
                    print(f"{key}: {value}")
                break
    if obtained:
        break
    materials_list = input().split()

# test inputs:

# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards

# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver


