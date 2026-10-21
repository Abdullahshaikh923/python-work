day = input("what is day")
weather = input("what is weather")
homework = input("is homeword is done")
if day == "monday":
    print("first day")
elif day== "friday":
    print("last day of school")
elif day== "tuesday":
    print("regular school day")
elif day =="wednesday and thursday":
    print("boring day")
else:
    print("funday")
if weather=="sunny"and homework=="yes":
    print("full releif")
if weather=="rainy"or "cloudy":
    print("trip plan")
if not homework=="yes":
    print("incomplte")

     

