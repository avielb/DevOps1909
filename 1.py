a = 4
b = "aviel"
c = True
d = ["aviel", "buskila", 34, True]
e = {"fname": "aviel",
     "lname": "buskila",
     "age": 34}
f = dict(fname="aviel", lname="buskila", age=34)
list_of_people = [e, f]
print(e["lname"])
print(f["lname"])
print(list_of_people)
print(d[2])
# this prints a
print(a)
# print("name is" + b)
r = 4 + 4
t = "aviel" * 4
u = "aviel" + str(4)
v = int(5.4)
s = "aviel" + "buskila"
fname = "aviel"
lname = "buskila"
first = fname + lname
second = "{} {}".format(lname, fname)
third = f"{fname} {lname}"
forth = "%s %s" % (lname, fname)
print(t)
print(u)
print(v)