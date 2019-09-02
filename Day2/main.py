print("Python Exercise - Day 2")


# EXERCISE 1: Print the character from an index of a string


class Exercise1:
    def __init__(self, index, string):
        print("\nExercise 1: ")
        if index < len(string):
            print("character from an index is:", string[index])
        else:
            print("Error! The index is greater than length of the string")


Exercise1(16, "Print the character from an index of a string")


# EXERCISE 2: Convert a string in reverse order


class Exercise2:
    def __init__(self, string):
        print("\nExercise 2: ")
        testlist = list(string)
        testlist.reverse()
        print("The reverse order is:", end=" ")
        for i in testlist:
            print(i, end="")


Exercise2("Convert a string in reverse order")


# EXERCISE 3: Convert all characters of a string into Upper case


class Exercise3:
    def __init__(self, string):
        print("\n\nExercise 3: ")
        string = string.upper()
        print("The new string is: ", string)


Exercise3("Convert all characters of a string into Upper case")


# EXERCISE 4:  Count all vowels in a string


class Exercise4:
    def __init__(self, string):
        print("\nExercise 4: ")
        count = 0
        string = string.lower()
        for s in string:
            if s == 'a' or s == 'e' or s == 'o' or s == 'u' or s == 'i':
                count += 1
        print("Number of vowels in the string: ", count)


Exercise4("Count All Vowels In A string")


# EXERCISE 5: Compute the sum of the digits in an integer


class Exercise5:
    def __init__(self, number):
        print("\nExercise 5: ")
        sum = 0
        while number > 0:
            sum += number % 10
            number = int(number / 10)
        print("The sum of digits: ", sum)


Exercise5(12345)


# EXERCISE 6: Print characters between two characters (i.e. A to P )


class Exercise6:
    def __init__(self, start, end, string):
        print("\nExercise 6: ")
        new_string = ""
        check = False
        for i in string:
            if check:
                new_string += i
            if i == start:
                check = True
            elif i == end:
                if check:
                    check = False
                    new_string += ','
        print(new_string.__contains__(','))
        getlist = new_string.split(',')
        print(getlist)
        if not new_string.__contains__(','):  # length = 0 or length = 1
            print("No result")
        else:  # length > 1
            for string in getlist:
                if len(string) > 1 and string[len(string) - 1] == 'n':
                    print(string[0:(len(string) - 1)])


Exercise6("h", "n", "Print characters between two characterns")


# EXERCISE 7: Print the first 100 Fibonacci values

def fibonacci(i, j, count, number):
    if count < number:
        print(i, end=' ')
        count += 1
        fibonacci(j, j + i, count, number)


print("\nExercise 7: ")
fibonacci(1, 1, 0, 100)


# EXERCISE 8: Print all prime numbers less than a given positive number


def check_prime_number(number):
    check = True
    i = 2
    while i < number:
        if number % i == 0:
            check = False
            break
        i += 1
    return check


class Exercise8:
    def __init__(self, number):
        print("\n\nExercise 8: ")
        if number >= 2:
            print(2, end=' ')
            for num in range(3, number):
                if check_prime_number(num):
                    print(num, end=' ')
        else:
            print("The given positive number isn't correct!")


Exercise8(100)
