#08.07.2025
#day 2


a = 56
b = 65
print(bool(a>b))
print(isinstance(a,int))


#lists
thislist = ["apple","banana","cherry",78,True]
print(thislist[2:4])
print(len(thislist))
print(type(thislist))
if "apple" in thislist:
    print("Yes")
thislist[3:] = ["Dragon fruit","Emu berry"]
thislist.insert(5,"fig")
thislist.append("guava")
thatlist = ["honeydew","Ice apple"]
thislist.extend(thatlist)

for x in thislist:
    print(x)
    
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
newlist = [y for y in thislist if "a" in y]
newlist.sort()
mylist = list(newlist)

list1 = ["app","insta"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


#tuples
thistuple = ("ant", "bat", "camel")
y = list(thistuple)
y.append("deer")
thistuple = tuple(y)
(green, red, *blue) = thistuple
print(green)
print(red)
print(blue)
print(thistuple)


#sets
thisset = {"aeroplane", "ball", "car", True, 1}
thatset = ["data", "english", "fall"]
thisset.update(thatset)
thisset.discard(True)
thisset.discard(1)
print(thisset)

set1 = {"apple", "banana", "caviar"}
set2 = {"apple", "ball", "call"}
set3 = set1.intersection(set2)
print(set3)
set4 = set1 ^ set2


#dictionaries
thisdict = {
    "object"   : "apple",
    "color"    : "red",
    "category" : "vegetable",
    "category" : "fruit"
    }
x = thisdict.keys()
print(x)
print(thisdict)
print(thisdict["color"])
thisdict["year"] = 2025
print(x)

myfamily = {
    "father" : {
        "name"   :"Papa",
        "year"   : 1975
        },
    "mother" : {
        "name"   :"Mama",
        "year"   : 1978
        },
    "child1" : {
        "name"  :"Unnie",
        "year"  : 2000
        },
    "child2" : {
        "name"  : "Me",
        "year"  : 2004
        }
    }
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':',obj[y])


##if loops
a = 30
b = 90
c = 45
if a > b :
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
if a < b and c < b :
    print("True")
if not a > b:
    print("True")

x = 34
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("below 20.")

date = 6
month = 12
match date:
    case 7 if month == 12:
        print("Birthday")
    case _ if 1 <= date <= 31 and month in range(1,13):
        print("Not your birthday")
    case _:
        print("Don't know")



#while loops
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i = i + 1

j = 0
while j < 6:
    j = j + 1
    if j == 2:
        continue
    print(j)

k = 1
while k < 6:
    print(k)
    k = k + 1
else :
    print("k > 6")


#for loops
adj = ["red", "big", "tasty"]
frui = ["apple", "banana", "cherry"]
for x in adj:
    for y in frui:
        print(x, y)
