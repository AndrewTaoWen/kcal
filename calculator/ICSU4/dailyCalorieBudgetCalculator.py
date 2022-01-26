height = float(input())
weight = float(input())
age = float(input())
sex = input().lower().strip()
activityLevel = input()

activityLevelDict = {'sedentary' : 1.25, 'lightlyactive' : 1.425, 'active' : 1.6, 'veryactive' : 1.95}

while not height:
    print('Please reenter your height.')
    height = float(input())

while not weight:
    print('Please reenter your weight.')
    height = float(input())

while not age:
    print('Please reenter your age.')
    height = float(input())

while sex not in ['m', 'f']:
    print('Please reenter your sex.')
    sex = input().lower().strip()

while activityLevel not in activityLevelDict:
    print('Please reenter your activity level.')
    activityLevel = input().lower().strip()

if sex == 'm':
    bmr = (13.397*weight + 4.799*height - 5.677*age + 88.362)*activityLevelDict[activityLevel] #todo multiply by activity level
    print(bmr)
else:
    bmr = (9.247*weight + 3.098*height - 4.330*age + 447.593)*activityLevelDict[activityLevel]
    print(bmr)


