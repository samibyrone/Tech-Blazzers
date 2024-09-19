from operator import index

numbers = list(range(1, 101))

def is_multiples_of_five(n):
    return n % 5 == 0

result = [n for n in numbers if n % 5 == 0]
print(result)



x = [[0 for _ in range(4)] for _ in range(5)]
print(x)


for i in range(5):
    for j in range(4):
        x[i][j] = 5
    print(x)


x = [0] * 5
i = []
for _ in range(5):
    i.append(x)
print(i)
print()




numbers = [1,2,3,4,5]
print(numbers)
print(6 not in numbers)
print(6 in range(len(numbers)))
print()



   #  TUPLE
list22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Abimbola", 5.2]
print(list22)
list22[9] = "Benjamin"
print(list22)
print()

score = (1, 2, 3, "Samibyrone")
single_tuple = (1,)
print(score.count(2))
score = list(score)
score[3] = "Babatunde"
score = tuple(score)
print(score)
print(type(score))
print()

tuples2 = (1, 2, 3, "Samibyrone",[7, 9, 8, 5], "Priest", "Bolaji", 10.5)
print(tuples2)
print(len(tuples2))
tuples2[4].append(15)
print(tuples2)
tuples2[4].extend([75, 15, 25])
print(tuples2)
print(type(score))
