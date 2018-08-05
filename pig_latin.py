# get sentence from user
user_sentence = input("Please enter a sentence to convert: ").strip().lower()

# split sentence into words
word_list = user_sentence.split()
print(word_list)

new_word_list = []
# loop through the words and convert to pig latin
for word in word_list:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_word_list.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        new_word = word[vowel_pos:] + word[:vowel_pos] + "ay"
        new_word_list.append(new_word)

# stick the words back together
new_sentence = ""
for new_word in new_word_list:
    new_sentence = new_sentence + " " + new_word

# output the sentence
print(new_sentence.strip())
