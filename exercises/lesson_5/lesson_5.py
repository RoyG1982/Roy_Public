## Leson 5 exercises: ###

## Exercise 1.1: ### 
x = 5
x += 4
print (x)

### Exercise 1.2: ### 
listy = [1, 5, "apples", 12.5]
listy.append ("bananas")
listy.remove (5)
print (listy)
print (len (listy)) 

## Exercise 1.3: ### 

car_dict = {
    "Toyota": ["camry", "avalon", "tacoma", "sequoia"],
    "Volvo": ["240", "850", "xc90", "s80"],
    "Mercedes": ["gle", "eqe", "eqs"]
}

print (car_dict["Toyota"])
car_dict["Subaru"] = ["dl", "forester", "ascent"]
print (car_dict)

## Exercise 3.1: ###

number1 = int (input ("enter number1: "))
number2 = int (input ("enter number2: "))
action = input ("enter add, subtract, multiply: ")

def math (number1, number2, action):

    if action == "add":
        print (number1 + number2)
    elif action == "subtract":
        print (number1 - number2)
    elif action == "multiply":
        print (number1 * number2)
    else:
        print ("error")

math(number1, number2, action)

## Exercise 3.2: ###

car_dict = {
    "Toyota": 
                {"camry": {"introduced": 1984, "seats": 5, "msrp": 24925}, 
               "avalon": {"introduced": 1987, "seats": 6, "msrp": 28925},
               "tacoma": {"introduced": 1967, "seats": 4, "msrp": 20925},
               },

    "Volvo": 
                {"240": {"introduced": 1974, "seats": 5, "msrp": 34925}, 
                "850": {"introduced": 1987, "seats": 5, "msrp": 48925},
                "xc90": {"introduced": 1999, "seats": 5, "msrp": 30925},
                },

    "Mercedes": 
                {"gle": {"introduced": 1974, "seats": 5, "msrp": 34925}, 
                "eqe": {"introduced": 1987, "seats": 5, "msrp": 48925},
                "eqs": {"introduced": 1999, "seats": 5, "msrp": 30925},
                }

            }

for make in car_dict:
    for model in car_dict[make]:
        if car_dict[make][model]["introduced"] > 1980:
            print(f" {model} was introduced after 1980")