from myData import tuples2

tuple2 = ("orange", [10,20,30], (5, 15, 25))
single_tuple = (1,)
print(len(tuple2))
print(tuple2)

tuple2 = list(tuple2)
tuple2[1] = (0,20)
tuple2[2] = (1,25)
tuple2 = tuple(tuple2)

print(tuple2[1],tuple2[2])
print(type(tuple2))
print()


student3 = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": "25",
        "gender": "M",
        "subject": {
            "maths": "45",
            "science": "45",
            "english": "65"
        }
    },

    {
        "first_name": "Deola",
        "last_name": "Smith",
        "age": "65",
        "gender": "F",
        "subject": {
            "geography": "75",
            "physics": "55",
            "chemistry": "64",
            "science": "35",
        }
    }
]

print(student3)

count = 0
for keys, value in student3.items():
    print(keys, value)
    count += 1
    print(count)


print()


