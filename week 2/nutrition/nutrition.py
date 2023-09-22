

s = input("Enter the fruit name: ").strip().lower()
fruits_dict = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grape" : "90",
    "honeydew melon " : "50",
    "kiwifruit" : "90",
    "lemon" : "15",
    "lime" : "20",
    "nectarine" : "60",
    "orange" : "80",
    "peach" : "60" ,
    "pear" : "100" ,
    "pineapple" : "50" ,
    "plums" : "70" ,
    "strawberries" : "50" ,
    "sweet cherries" : "100" ,
    "tangerine" : "50" ,
    "watermelon" : "80" ,
}


if s in fruits_dict:
    print("Calories: " + fruits_dict[s])
else:
    print("", end="")