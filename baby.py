from random import choice

questions = ["Why is the sky blue?: ","Why is blood red?: ","Why is earth round?: "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("But why???: ").strip().lower()

print("Ok! Please dont be mad.")
