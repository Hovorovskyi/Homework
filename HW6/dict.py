d = {
    'Ivanov': (5, 4, 5),
    'Shevchenko': (5, 5, 5),
    'Kosov': (4, 3, 4)
}

def grade(x):
    for d, i in x.items():
        return list(d,i)

def grade_m(x):
    i = list(map(int, grade(x)))
    return i

print(list(map(grade_m, d)))