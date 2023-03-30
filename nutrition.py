def main():
    fruit = input("Item: ").lower()
    fruits_list = {
    "apple" : "130",
    "banana" : "110",
    "avocado" : "50",
    }
    if fruit in fruits_list:
        print("Calories:" , fruits_list[fruit])
main()