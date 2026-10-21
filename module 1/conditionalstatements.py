temperature=int(input("Enter the temperature in celsius"))
if temperature <20:
    outfit="jacket"
    print("weather is cold")
else:
    outfit="T shirt"
    print("weather is hot")

is_raining= input("Is it raining yes/no")
if is_raining=="yes":
    print("bring a umbrella")
    
has_puddles=input("is there are puddles on ground")
if has_puddles=="yes":
    print("ground is wet")
else:
    print("ground is dry")
print(temperature)
print(outfit)
print(is_raining)


