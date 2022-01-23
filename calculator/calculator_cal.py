def calculate_budget(budget_form):

    activity_levels = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725, '5': 1.9}

    if budget_form.gender.data == 'm':
        b = (13.397 * budget_form.weight.data + 4.799 * budget_form.height.data - 5.677 * budget_form.age.data + 88.362) \
            * activity_levels[budget_form.activity.data]
    else:
        b = (9.247 * budget_form.weight.data + 3.098 * budget_form.height.data - 4.330 * budget_form.age.data + 447.593) \
            * activity_levels[budget_form.activity.data]

    return int(b)
