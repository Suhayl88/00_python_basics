# Ask the user for their thier name
username = input("what is your name?")

#ask the user for their favourite integer
fav_num = int(input("favourite Number? "))

# Double, halve and square the nmber
double = fav_num * 2
half = fav_num / 2
squared = fav_num * fav_num

print()
# Greet the user
print("Hi {}, your favourite number is {}".format(username, fav_num))
print()
# Output the results of doubling, halving
# and squaring their favourite number
print("double {} is {}".format (fav_num, double))
print("half {} is {}".format(fav_num, half))
print("{} squared is {}".format(fav_num, squared))
print()

