#car_brands=['BMW', 'AUDI', 'MERCEDES-BENZ', 'VOLKSWAGEN']
#for x in car_brands:
   # print(x)
#i = 30
#while i < 50:
  #print(i)
 # i += 1
name=input('Enter youre name:  ')
age=input('Enter youre age: ')
height=input('Enter youre  height: ')

try:
      age=int(age)
      height=int(height)
except ValueError as e:
    print(e)
    print(f"You inserted '{age,height}' which is not a valid number!")

print(f"Hello {name} , from our questions it was found that you are {age} years old and {height} cm")



