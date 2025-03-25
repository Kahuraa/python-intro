# data_structures
# collection
# list, dictionary, set

scores = [78, 43, 67, 89, 45, 76, 99, 90, 56, 43, 65, 55, 61, 23, 54, 89, 90, 49, 69]

# access a score
print(scores[0])
print(scores[1])

# add score
scores.append(51)
print(scores)

# remove score
scores.remove(43)
print(scores)

# count
print(len(scores))
print(scores.count(45))
scores.sort()
print(scores) #ascending
scores.sort(reverse=True) #descending
print(scores)



# slice a list
top_5 = scores[-5:] #cutting the list
print(top_5)


# dictionary

person = {"name": "Halima", "age": 19, "weight": 58, "county": "Nairobi"}
print(person)
print(person["name"])
print(person["age"])
print(person["weight"])


# set
days = {"mon", "tue", "wed", "thu", "fri", "sat", "sun", "mon"}
print(days)


for s in scores: #for each score in scores
    print(s)
    if s < 50:
        pass
    print(s)

    for d in days: #for each day in days
        print(d)
