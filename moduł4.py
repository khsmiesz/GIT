#zadanie1
def dodawanie():
    a=2+3
    print(a)
dodawanie()

#zadanie2
a=1
def scope_demo():
    a=2
    print(a)

scope_demo()
print(a)

#zadanie3
def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

print(shopping())

def no_result_function():
    print("I am just printing I love you")
    print("and returning nothing to you!")
    return
type(no_result_function())

def day_times():
    return "morning", "afternoon", "evening", "night"
times=day_times()
print(times)
print(type(times))

first, second, third, fourth = day_times()
print("Trzeci element to %s" % third)