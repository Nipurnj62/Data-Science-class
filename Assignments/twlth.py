empylist=[]

for i in range(1000,3000):
 string_conversion=str(i)

 if (int(string_conversion[0])%2==0) and (int(string_conversion[1])%2==0) and (int(string_conversion[2])%2==0) and (int(string_conversion[3])%2==0):
          empylist.append(string_conversion)


print(' ,'.join(empylist))

