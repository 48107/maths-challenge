# Validity of Triangle given sides
from itertools import combinations
# Function definition to check validity
def is_valid_triangle(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False
comb = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 3)  
# Function call & making decision

for i in list(comb):
    side_a = i[0]
    side_b = i[1]
    side_c = i[2]
    if is_valid_triangle(side_a, side_b, side_c):
        print("%s", i, " is valid")
        with open("triangle.txt", "a") as text_file:
            print(f"{i}", file=text_file)

side_a = 0
side_b = 0
side_c = 0
if is_valid_triangle(side_a, side_b, side_c):
    print('Triangle is Valid.')
else:
    print('Triangle is Invalid.')