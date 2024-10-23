'''1. За день машина проезжает n километров.  
Сколько дней нужно, чтобы проехать маршрут длиной m километров?  
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

**Input:**

n = 700

m = 750

**Output:**

2'''



def distance():
    print('Задание 1')
    n=int(input())
    m=int(input())
    print((m-1)//n+1)

#distance()



'''2. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.  
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.  
Выведите наименьшее число парт, которое нужно приобрести для них.

**Input:**

20

21

22

**Output:**

32'''



def kolichestvo_part(a):
    return (a-1)//2+1

def school():
    print('Задание 2')
    a=int(input())
    b=int(input())
    c=int(input())
    print(kolichestvo_part(a)+kolichestvo_part(b)+kolichestvo_part(c))

#school()

'''3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.  
В решении дллжно быть не более 5 строк кода'''



def dvoiki():
    print('Задание 3')
    N=float(input())
    k=0
    while (2**k)<N:
        print(k)
        k+=1
        
#dvoiki()

'''4. Дана последовательность из N целых чисел и число K.  
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.  
Не использовать циклы.

Input:   [1, 2, 3, 4, 5] k = 3

Output:  [4, 5, 1, 2, 3]'''



def list_4():
    print('Задание 4')
    list_1=list(map(int, input().split(',')))
    k=int(input())
    list_1=list_1[k:]+list_1[:k]
    print(list_1)

#list_s()

'''5. Дан массив, состоящий из целых чисел.  
Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

Input: [0, -1, 5, 2, 3]
Output: 2

Пояснение: (-1 < 5, 2 < 3)'''



def list_5():
    print('Задание 5')
    list_1=list(map(int, input().split(',')))
    count=0
    for i in range(len(list_1)-1):
        if list_1[i]<list_1[i+1]:
            count+=1
    print(count)

#list_5()

'''6. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.'''

def recursiya(a,b):
    if b==0:
        return 1
    else:
        return a*recursiya(a,b-1)
    
def recursiya_zadanie():
    print('Задание 6')
    a=float(input())
    b=int(input())
    print(recursiya(a,b))

#recursiya_zadanie()

'''7. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input: 5

Output: yes'''

def simple_number(a):
    if a!=2 and a%2==0 or a!=3 and a%3==0 or a!=5 and a%5==0 or a!=7 and a%7==0:
        return False
    else:
        count=0
        for i in range(1,a-1):
            if a%i==0:
                count+=1
            if count>1:
                break
        if count>1:
            return False
        else:
            return True
        
def zadanie_7():
    print('Задание 7')
    a=int(input())
    if simple_number(a):
        print('Yes')
    else:
        print('No')
#zadanie_7()

'''8. Дано натуральное число N и последовательность из N элементов.  
Требуется вывести эту последовательность в обратном порядке.  
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Разрешается использовать строки для вывода

Input:    2 -> 3 4
Output: 4 3'''

def zadanie_8_rec(count,a,b):
    if count==a:
        return
    else:
        count+=1
        zadanie_8_rec(count,a,b)
    print(b[count-1],end=' ')

def zadanie_8():
    print('Задание 8')
    a,b=input(),input()
    count=0
    print(zadanie_8_rec(count,int(a),str(b)))

#zadanie_8()

'''9. Заполните массив элементами арифметической прогрессии.  
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.  
Каждое число вводится с новой строки.  
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Попытайтесь использовать рекурсию.


Ввод: 7 2 5
Вывод: 7 9 11 13 15'''

def arithmetic_progression(a,b,c):
    if c==0:
        return
    else:
        c-=1
        a-=b
        arithmetic_progression(a,b,c)
        print(a, end=' ')

def zadanie_9():
    a,b,c=int(input()),int(input()),int(input())
    arithmetic_progression(a+b*c,b,c)

#zadanie_9()

'''10. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод:			Вывод:
1 2 3 2 3			2
Ввод:			Вывод:
5 5 5 5 5			10'''

def para(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count+=1
    return count

def zadanie_10():
    print('Задание 10')
    list_1=list(map(int, input().split(' ')))
    print(para(list_1))

#zadanie_10()

'''11. Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.  
Функции bin и oct используйте для проверки своего
результата, а не для решения.  
Дополнительно:
Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов, где это возможно'''


#------------

#------------

'''12. Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.
Не использовать условия.'''

def zadanie_12():
    print('Задание 12')
    a_tuple=(1,23,5.6,7.54,'ds','ewsds',[1,2,3,4])
    dict_1={}
    for i in a_tuple:
        dict_1[str(type(i))]=i
    return dict_1

#print(zadanie_12())

'''13. Функция получает на вход список чисел.
Отсортируйте список по убыванию суммы цифр.  
Функция должна состоять из двух строк, где первая строка — определение, а вторая  — return.'''

def sorted_arr(arr):
    return sorted(arr, key=lambda x: sum(map(int,str(x))))

#print(sorted_arr(list(map(int, input().split(' ')))))

'''14. Создайте функцию генератор ВСЕХ чисел Фибоначчи'''

def fibonacchi(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacchi(n-1)+fibonacchi(n-2)

#print(fibonacchi(10))

'''15. Самостоятельно сохраните в переменной строку текста.  
Создайте из строки словарь, где ключ - буква, а значение - код буквы из Unicode.
Напишите преобразование в одну строку.'''

def zadanie_15():
    a=input()
    dict_1={}
    for i in a:
        dict_1[i]=i.encode("utf-8")
    return dict_1
#print(zadanie_15())

'''16. Создайте генератор чётных чисел от нуля до 100.
Из последовательности исключите числа, сумма цифр которых равна 8. Решение в одну строку.'''

def zadanie_16():
    return list(filter(lambda x: x if x%2==0 and (x%10+x//10%10)!=8 else '', [i for i in range(100)]))

#print(zadanie_16())

'''17. Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой. Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.'''