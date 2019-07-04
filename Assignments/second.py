# Write a program which can compute the factorial of a given numbers The results should be printed in a comma-separated sequence on a single line.

first_number=int(input("enter a number"))
fact=1

for i in range(1,first_number):

    fact=(fact*i)

print(fact)


