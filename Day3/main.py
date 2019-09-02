print("Python Exercise - Day 3")

# EXERCISE 1: Print the all characters between two positions of a string


class Exercise1:
    def __init__(self, start, end, string):
        print("\nExercise 1: ")
        print("The all characters between two positions of a string: ", end='')
        for char in string[start:end]:
            print(char, end='')


Exercise1(5, 15, "Print the all characters")


# EXERCISE 2: Reverse vowels in a given string
'''
=> Replace the character from the index in the string
def change_char(string, index, character):
    return string[:index] + character + string[index+1:]
'''


class Exercise2:
    def __init__(self, string):
        print("\n\nExercise 2: ")
        string_vowel = ""
        for char in string:
            c = char.lower()
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                string_vowel += char
        j = len(string_vowel) - 1
        for i in range(len(string)):
            c = string[i].lower()
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                string = string[:i] + string_vowel[j] + string[(i+1):]
                j -= 1
        print(string)


Exercise2("Reverse vowels in a given string.")


# EXERCISE 3: Convert all characters of a string into Lower case


text = 'abcdefg'
print(text)
text = text[:1] + 'Z' + text[2:]
print(text)
