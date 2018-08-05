known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    if(name in known_users):
        print("Hello {0}".format(name))
        want_to_be_removed = input("Do you want to be removed from the system?(y/n): ").strip().lower()
        if(want_to_be_removed == "y"):
            known_users.remove(name)
        elif(want_to_be_removed == "n"):
            print("No worries {}! I didn't want you to leave either!".format(name))
        else:
            print("Oops! Looks like you entered a wrong option.")
    else:
        print("Hmmmm, I dont think I have met you yet {0}!".format(name))
        want_to_be_added = input("Would you like to be added to the system?(y/n): ").strip().lower()
        if(want_to_be_added == "y"):
            known_users.append(name)
        elif(want_to_be_added == "n"):
            print("No worries {}! See you around!".format(name))
        else:
            print("Oops! Looks like you entered a wrong option.")
       
 
