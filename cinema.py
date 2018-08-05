films = {
    "Finding Dory":[3,5],
    "Bourne":[19,5],
    "Tarzan":[15,5],
    "Ghost Busters": [12,5]
    }

while True:
    choice = input("What film do you want to watch?: ").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry! We are sold out!")
        else:
            print("Sorry, you are not old enough to watch that film.")
    else:
        print("We dont have that film...")
