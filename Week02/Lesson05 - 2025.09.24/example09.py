foods = {
    "Soups": ["with meat", "with legumes", "with vegetables"],
    "Kebabs": ["spicy", "w/o spices", "durums"],
    "Drinks": ["tea", "coffee"],
}

print(foods)

for category in foods:
    print(category)
    for item in foods[category]:
        print("\t", item)

foods = {
    "Soups": {
        "with meat": ["iskembe", "kelle paca"],
        "with legumes": ["mercimek", "ezogelin"],
        "with vegetables": ["mantar", "brokoli"],
    },
    "Kebabs": {
        "spicy": ["Adana", "Mardin"],
        "w/o spices": ["urfa", "antep"],
        "durums": ["adana durum", "urfa durum"],
    },
    "Drinks": ["Tea", "Coffee"],
}

for main_category in foods:
    print(main_category)
    if type(foods[main_category]) is dict:
        for category in foods[main_category]:
            print("\t", category)
            if type(foods[main_category][category]) is dict:
                for subcategory in foods[main_category][category]:
                    print("\t\t", subcategory)
                    for subcategory2 in foods[main_category][category][subcategory]:
                        print("\t\t\t", subcategory2)
            else:
                print("\t\t", foods[main_category][category])
    else:
        print("\t", foods[main_category])
