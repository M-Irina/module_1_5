mutable_list = [3, 7, "apple", "cherri"]
print(mutable_list)
print(mutable_list[3])
mutable_list[2] = 303
print(mutable_list)
mutable_list.append("peach")
print(mutable_list)
mutable_list.extend("bird")
print(mutable_list)
mutable_list.extend(["bird", 3])
print(mutable_list)
mutable_list.remove(303)
print(mutable_list)
print("apple" in mutable_list)
print("apple" not in mutable_list)
print(mutable_list[0:1:1])