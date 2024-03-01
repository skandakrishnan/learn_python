friends = ["Durga","Vamsi","Saumya","Srikar","Charan"]
lucky_numbers = [4, 45, 15, 16, 3, 42]

print(friends)

print(friends.extend(lucky_numbers))
friends_2 = ["Durga","Vamsi","Saumya","Srikar","Charan"]
print(friends_2)
friends_2.append("Anushka")
print(friends_2)
friends_2.insert(1,"Anushka")
print(friends_2)
friends_2.remove("Anushka")


print(friends_2)
friends_2.remove("Anushka")
print(friends_2)
print(friends_2.clear)
print(friends_2.pop())
print(friends_2.index("Saumya"))
print(friends_2.count("Vamsi"))
friends_2.insert(1,"Vamsi")
print(friends_2.count("Vamsi"))
friends_2.sort()
print(friends_2)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends_3 = friends_2.copy()
print(friends_3)




