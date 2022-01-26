class Calculator():
    @staticmethod
    def calculateBudget(budget):
        activityLevels = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725, '5': 1.9}

        if budget.gender == 'm':
            b = (13.397 * budget.weight + 4.799 * budget.height - 5.677 * budget.age + 88.362) * activityLevels[budget.activity]  # todo multiply by activity level
        else:
            b = (9.247 * budget.weight + 3.098 * budget.height - 4.330 * budget.age + 447.593) * activityLevels[budget.activity]

        return int(b)
