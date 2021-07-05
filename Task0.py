import random
randomlist = random.sample(range(-100, 100), 30)
print("\n")
print(randomlist)

print("\nМаксимальний елемент списку: ", max(randomlist)) 
print("Порядковий номер: ", randomlist.index(max(randomlist))) 
print("\n")


newlist = [i for i in randomlist if (i % 2) == 1] 
if len(newlist) == 0: 
    print("Таких чисел немає!") 
print(sorted(newlist, reverse=True)) 
print("\n")
