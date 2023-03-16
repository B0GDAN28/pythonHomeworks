# for _ in range(3):
#     try:
#         age = int(input("Age: "))
#     except ValueError:
#         print("Try again, you didn't write a number correctly")
#
#         continue
#     if age == int(age):
#         if age >= 18:
#             print("You are a grown up!")
#         else:
#             print("You are a child!")
#
#     else:
#         print("No more attempts")

max_attempts = 3

for attempts in range(max_attempts):
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Try again, you didn't write a number correctly")

        continue
    if age == int(age):
        if age >= 18:
            print("You are a grown up!")
            break
        else:
            print("You are a child!")
            break

else:
    print("No more attempts")


