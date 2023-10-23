#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    maximum = max(a,b,c)
    print(maximum)
    return maximum

max_num(4,7,1)

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    total = 1
    for i in numbers:
        total *= i
    print(total)
    return total

mult_list([4,7,1])

#Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    reversed = string[::-1]
    print(reversed)
    return reversed

rev_string("Howdy Partner")
#Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(number, start, end):
    print(start <= number <= end)
    return start <= number <= end

num_within(3,2,4)
num_within(10,2,5)

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    def next_row(row):
        result = [1]
        for i in range(1, len(row)):
            result.append(row[i - 1] + row[i])
        result.append(1)
        return result

    row = [1]
    for x in range(n):
        print(row)
        row = next_row(row)

pascal(5)