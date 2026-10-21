m1 = 90
m2 = 80
m3 = 70
avg = int(m1+m2+m3)/3
ValidRange = range(0,101)
if(avg not in ValidRange):
    print("invalid input")
elif avg in range (91,101):
    print("grade is A1")
elif avg in range (81,91):
    print("grade is A")
else:
    print("there is other grade")