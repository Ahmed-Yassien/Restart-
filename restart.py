
def main(n):
    l = double(len(n))
    return l
def double(l):
    l = l * 2
    return l
print("hello, \"friend\"")
while True:
    try:
        x = input("what is your name?").strip().title()
        first , last = x.split(" ")
        print(f"hello, {first}")
    except ValueError:
        print("plz insrt f & l names")
    else:
        break
i = input(f"{last}, can u jump for " + str(main(first)) + " times?  ")

#! Conditions
# وانت بتكتب الشروط خلي بالك انك متخليش شرط ياخد نتيجة اللي بعده
# مثال قسم الداتا لرجالة وحريم وقسم الحريم حسب اسم ابوهم
# if match while for assert pytest
if i == "y":
    print("good")
elif i in ["n"]:
    print("oh, that's too bad")
else:
    import sys
    sys.exit("plz, answer with y or n")    
    
match first.lower():
        case "ahmed" | "mohammed" | "ali":
            print("Muslim")
        case "peter":
            print("Not a muslim")
        case _:
            print("unknown")

lst =first, last, i
file = open("file.txt", "a")
file.write(str(lst) + "\n")

with open("file.txt", "r") as file:
    lines = file.readlines()
    lines.sort()
    for line in lines:
        line= list(line.split(","))
        print(line[1])
with open("file.txt", "r + w") as file:
 for index, line in enumerate(lines):
 #   lines = file.writelines(lines)
    if line == "['ahmed', __ , _ _]\n":
        lines[index] = "['ahmed', __, 'n']\n"
               
file.close()

#sorted = 
