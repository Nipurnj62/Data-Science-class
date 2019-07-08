new_list=input("enter some  numbers")


outputlist=[i for i in new_list.split(',') if (int(i)%2!=0)]
print(' '.join(outputlist))