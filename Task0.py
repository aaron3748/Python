import random
#Генерує ряд з 30 випадкових цілих чисел від -100 до + 100
randomlist = random.sample(range(-100, 100), 30)
print("\n")
print(randomlist)

print("\nМаксимальний елемент рядку: ", max(randomlist)) #знаходить і виводить максимальний елемент ряду
print("Порядковий номер: ", randomlist.index(max(randomlist))) #виводить порядковий номер максимального елемента ряду
print("\n")

#Рядок, що складається тільки з непарних чисел вихідного списку
newlist = [i for i in randomlist if (i % 2) == 1] #генерує ряд з умовою
if len(newlist) == 0: 
    print("Таких чисел немає!") #повідомляє, що таких чисел немає
print(sorted(newlist, reverse=True)) #рядок, виведений в порядку зменшення елементів
print("\n")
