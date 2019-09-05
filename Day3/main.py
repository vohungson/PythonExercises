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
                string = string[:i] + string_vowel[j] + string[(i + 1):]
                j -= 1
        print(string)


Exercise2("Reverse vowels in a given string.")


# EXERCISE 3: Convert all characters of a string into Lower case


class Exercise3:
    def __init__(self, string):
        print("\nExercise 3: ")
        print(string.lower())


Exercise3("CONVERT ALL CHARACTERS OF A STRING")


# EXERCISE 4: Find the k largest elements in a given array.
# Elements in the array can be in any order


class Exercise4:
    def __init__(self):
        print("\nExercise 4: Find the k largest elements in a given array")
        numbers = [7, 3, 2, 10, 4, 9, 8, 6, 0, 10]
        largest_number = 0
        for x in numbers:
            if x > largest_number:
                largest_number = x
        print("The largest number is: ", largest_number)
        count = 0
        for x in numbers:
            if x == largest_number:
                count += 1
        if count == 1:
            print(count, "largest element", largest_number)
        else:
            print(count, "largest elements", largest_number)


Exercise4()


# EXERCISE 5: Find the numbers greater than
# the average of the numbers of a given array


class Exercise5:
    def __init__(self, numbers):
        print("\nExercise 5: ")
        average = numbers[int(len(numbers) / 2)]
        for n in numbers:
            if n > average:
                print(n, end=' ')


Exercise5([7, 3, 2, 1, 9, 4, 8, 6, 0, 10])


# EXERCISE 6: Create the concatenation of the two strings
# except removing the first character of each string.
# The length of the strings must be 1 and above. 

class Exercise6:
    def __init__(self, string1, string2):
        print("\n\nExercise 6: ")
        string3 = string1[1:] + string2[1:]
        print("Output:")
        print(string3)


Exercise6("Python", "Tutorial")


# EXERCISE 7: Find the total number of continuous subarrays
# in a given array of integers whose sum equals to a given integer.


class Exercise7:
    def __init__(self, numbers, k):
        print("\nExercise 7: ")
        count = 0
        i = 0
        while i < len(numbers):
            sum_nums = 0
            j = 0
            for m in numbers[i:]:
                sum_nums += m
                if sum_nums == k:
                    count += 1
                    i += j
                    break
                j += 1
            i += 1
        print("Number of contiuous subarrays: ", count)


Exercise7([4, 2, 3, 3, 3, 7, 2, 4], 6)


# EXERCISE 8: Write a Java program to get the position
# of a prime number which is near to the given integer.

class Exercise8:
    def __init__(self, prime):
        print("\nExercise 8: ")
        print("List of prime numbers: ")
        position = 0
        for n in range(2, prime + 1):
            if Exercise8.check_prime(n):
                print(n, end=' ')
                position += 1
        print("\nPosition: ", position)

    @staticmethod
    def check_prime(number):
        check = True
        for n in range(2, number):
            if number % n == 0:
                check = False
                break
        return check


Exercise8(13)

# EXERCISE 9:
"""
Write a Java program to return the sum of the numbers 
(may form more than one digits), appearing in the string.
         Sample Output:
         The given string is: it 15 is25 a 20string
         The sum of numbers in the string is: 60
"""
import re


class Exercise9:
    def __init__(self, string):
        print("\nExercise 9:")
        x = re.findall("\d+", string)
        print(x)
        sum_num = 0
        for n in x:
            sum_num += int(n)
        print("The sum of numbers in the string is: ", sum_num)


Exercise9("it 15 is25 a 20string")

# EXERCISE 10:
"""
Write a Java program to count the number of words ending in 'm' or 'n' (not case sensitive).
         Sample Output:
         The given string is: mam is in the room
         The number of words ends either m or n is: 3
"""


class Exercise10:
    def __init__(self, string):
        print("\nExercise 10: ")
        x = re.findall("\w*[m|n]\W|\w+[m|n]$", string)
        print(x)
        print("The number of words:", len(x))


Exercise10("mam is in mo omo the room")


# EXERCISE 11:
"""
Write a Python program to find the longest substring appears at both ends of a given string. 
Sample Output:
The given string is: playersplay
The longest substring in the string is: play
"""

class Exercise11:
    def __init__(self, string):
        print("\nExercise  11: ")
        end = 0
        for i in range(int(len(string)/2)):
            if string[i] == string[len(string)-1]:
                end = i
                break
        start = 0
        for i in range(int(len(string)/2),len(string)):
            if string[i] == string[0]:
                start = i
                break
        print("len",len(string))
        print("end",end)
        print("start",start)
        if end == len(string) - 1 - start:
            print("Step if = ", Exercise11.check_substring(self, string, end, start))
            if Exercise11.check_substring(self, string, end, start):
                print("Result: ", string[:(end+1)])
            else:
                print("We can not find out the substring")
        elif end < len(string) - start:
            d = len(string) - 1 - start - end
            print("else if", d)
            if Exercise11.check_substring(self, string, end + d, start):
                print("Result1: ", string[:(end + d + 1)])
            elif Exercise11.check_substring(self, string, end, start + d):
                print("Result2: ", string[:(end + 1)])
            else:
                print("We can not find out the substring")
        else:
            print("We can not find out the substring")

    @staticmethod
    def check_substring(self, string, end, start):
        check = True
        i = 0
        while i <= end:
            if string[i] != string[start + i]:
                check = False
            print(string[i], string[start + i])
            i += 1
        print(check)
        return check


Exercise11("pplayerspplay")

# EXERCISE 12:
"""
Write a Python program to return the string after removing all 'z' 
(except the very first and last) from a given string.
Sample Output:
The given string is: zebrazone
The new string is: zebraone
"""
class Exercise12:
    def __init__(self, string):
        print("\nExercise 12: ")
        x = re.findall("[a-yA-Y\W]*", string)
        new_string = ""
        for s in x:
            new_string += s
        if string[0] == 'z' or string[0] == 'Z':
            new_string = string[0] + new_string
        if string[len(string)-1] == 'z' or string[len(string)-1] == 'Z':
            new_string = new_string + string[len(string)-1]
        print(new_string)


Exercise12("zebrazone")


# EXERCISE 13:
"""
Write a Python program to return a new string using every 
characters of even positions from a given string. Sample Output:
The given string is: w3resource.com
The new string is: wrsuc.o
"""


class Exercise13:
    def __init__(self, string):
        print("\nExercise 13: ")
        i = 0
        for s in string:
            if i % 2 == 0:
                print(s, end='')
            i += 1


Exercise13("w3resource.com")
