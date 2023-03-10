

for _ in range(3):
    try:
        age = int(input("Age: "))
    except ValueError:

        continue
    if age==int(age):
        if age >= 18:
            print("You are a grown up!")
        else:
            print("You are a child!")
    else:
        print("No more attemps")






