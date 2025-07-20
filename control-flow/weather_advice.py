weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
    print(f"The weather is {weather}, Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print(f"The weather is {weather}, Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print(f"The weather is {weather}, Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for '{weather}' weather.")
