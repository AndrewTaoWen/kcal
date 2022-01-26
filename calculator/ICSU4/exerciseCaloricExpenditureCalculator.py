from msilib.schema import File
file = open("MET_File.txt")

exercises = {}

for line in file:
    space1 = line.index("	")
    exercise = line[ : space1]

    space2 = line.rfind(".")
    subExercise = " ".join(line[space1 + 1 : space2 - 2].split())

    MET = line[space2 - 2 : ].strip()

    if exercise not in exercises.keys():
        exercises[exercise] = [(subExercise, MET)]
    else:
        exercises[exercise].append((subExercise, MET))

def search_tuples(data, target):
  
    for i in range(len(data)):
  
        if data[i][0] == target:
            return i
  
    return -1

def calculateExpenditure(exercise, subExercise, time, weight):
    data = exercises[exercise]

    MET = float(data[search_tuples(data, subExercise)][1])

    calories = weight * MET * time / 200

    return f"MET is {MET} and calories burned is {calories}"

print(exercises)

print(calculateExpenditure("bicycling", "bicycling, mountain, uphill, vigorous", 45, 70))

