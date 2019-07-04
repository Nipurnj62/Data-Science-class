#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

number=int(input("enter a number"))

output={i:i*i for i in range(1,number+1)}
print(output)