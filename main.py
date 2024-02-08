#Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
#Напишите функцию, которая принимает список, из списка выдает случайное значение из списка и записывает результат в txt файл. Список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
#names = [“azat”, “zina”, “kuma”, “anna”, “sas”] Вывести с помощью lambda функции имена палиндромы


#№1
# def number():
#     num = 0
#     n = 0
#     for i in range(5):
#         n +=1
#         print(f"{n}: {num}")
# number()

#№2
# import random
# def sort(list):
#      new_list = random.choice(list)
#      with open('text.txt', 'w') as file:
#          file.write(new_list)
#          print('Язык был записан')
            
# language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
# sort(language)

#№3 
names = ["azat", "zina", "kuma", "anna", "sas"]
name = list(filter(lambda name: name == name[::-1], names))
print(name)