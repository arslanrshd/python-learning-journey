a = {} # Empty dictionary
arslan_marks = {
    "key":"valve",
    "Arslan":"student",
    "marks":900
}
# print(type(arslan_marks))
# print(arslan_marks)

print(arslan_marks.items())
print(arslan_marks.keys())
print(arslan_marks.values())
print(arslan_marks.update({"marks":1000}))
print(arslan_marks.get("Arslan"))
# print(arslan_marks.clear())
remove = arslan_marks.pop("Arslan")
print(remove)
print(arslan_marks)