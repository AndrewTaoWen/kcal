def calculate_budget(budget_form):

    activity_levels = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725, '5': 1.9}

    if budget_form.gender.data == 'm':
        b = (13.397 * budget_form.weight.data + 4.799 * budget_form.height.data - 5.677 * budget_form.age.data + 88.362) \
            * activity_levels[budget_form.activity.data]
    else:
        b = (9.247 * budget_form.weight.data + 3.098 * budget_form.height.data - 4.330 * budget_form.age.data + 447.593) \
            * activity_levels[budget_form.activity.data]

    return int(b)

def calculate_intake(form):

    total = 0
    total += form.bread_amt.data * 60
    total += form.bagel_amt.data * 245
    total += form.egg_amt.data * 78
    total += form.bacon_amt.data * 45
    total += form.yogurt_amt.data * 100
    total += form.cereal_amt.data * 379
    total += form.oats_amt.data * 307
    total += (form.othersB_amt.data + form.othersL_amt.data + form.othersD_amt.data)
    total += (form.pizza_amt.data + form.pizzaD_amt.data) * 285
    total += (form.pasta_amt.data + form.pastaD_amt.data) * 288
    total += (form.burger_amt.data) * 354
    total += (form.beef_amt.data + form.beefD_amt.data) * 71
    total += (form.chicken_amt.data + form.chickenD_amt.data) * 68
    total += (form.pork_amt.data + form.porkD_amt.data) * 69
    total += form.potato_amt.data * 163
    total += form.rice_amt.data * 206


    return total

def calculate_expen(form, bform):
    total = 0
    w = bform.weight.data
    total += (form.walking_amt.data * w * 3.5 * 3.3)/200
    total += (form.jogging_amt.data * w * 3.5 * 8)/200
    total += (form.running_amt.data * w * 3.5 * 11)/200
    total += (form.biking_amt.data * w * 3.5 * 8)/200
    total += (form.swimming_amt.data * w * 3.5 * 7)/200
    total += (form.basketball_amt.data * w * 3.5 * 8)/200
    total += (form.soccer_amt.data * w * 3.5 * 7)/200
    total += (form.badminton_amt.data * w * 3.5 * 4.5)/200
    total += (form.football_amt.data * w * 3.5 * 8)/200
    total += (form.tennis_amt.data * w * 3.5 * 7)/200
    total += (form.baseball_amt.data * w * 3.5 * 5)/200
    total += (form.tabletennis_amt.data * w * 3.5 * 6)/200
    total += (form.hockey_amt.data * w * 3.5 * 8)/200
    total += (form.lifting_amt.data * w * 3.5 * 8)/200
    total += (form.martialarts_amt.data * w * 3.5 * 10)/200
    total += (form.skippingrope_amt.data * w * 3.5 * 8)/200
    total += (form.dancing_amt.data * w * 3.5 * 3)/200
    total += (form.HIIT_amt.data * w * 3.5 * 8)/200
    total += (form.skiing_amt.data * w * 3.5 * 6)/200
    total += (form.snowboarding_amt.data * w * 3.5 * 5.3)/200
    total += form.others_amt.data

    return int(total)


