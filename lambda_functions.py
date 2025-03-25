# lambda_functions
from functools import reduce


def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(2, 3))



# simple calc
add_two =lambda a, b: a + b
print(add_two(2, 3))



# list of scores
scores = [{"eng": 75, "mat": 85},
          {"eng": 78, "mat": 88},
          {"eng": 80, "mat": 90},
          {"eng": 85, "mat": 95}]

sorted_by_maths = sorted(scores, key=lambda s: s["mat"])
print(sorted_by_maths)



def get_eng_score(score):
    return score["eng"]



sorted_by_eng = sorted(scores, key=get_eng_score)
print(sorted_by_eng)



ages = [20, 39, 89, 49, 20, 19, 19, 30, 50, 70, 68, 78, 47, 8, 11, 23, 53, 52]
total_ages = reduce(lambda x, y: x + y, ages, 0)
print(total_ages)



new_ages = map(lambda x: x + 1, ages)
print(list(new_ages))



above_30 = filter(lambda age: age > 30, ages)
print(list(above_30))





