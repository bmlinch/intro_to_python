user_input = float(input("How many kilometers did you run today? \n"))

if user_input<50:
    print(f"You ran {user_input} kilometers which is .. {round(user_input * .621,2)} miles!")
else:
    print(f"You ran {user_input}, seriously that many?? \n Beast mode activated! {round(user_input * .621,2)} miles!? You're an animal!")
