def school_years():
    pre_school = 2
    basic_school = 9
    high_school = 3

    levels = []
    for level in range(1, pre_school + 1):
        levels.append(("{}º PS".format(level), "{}º ano primário".format(level)))

    for level in range(1, basic_school + 1):
        levels.append(("{}º BS".format(level), "{}º ano fundamental".format(level)))

    for level in range(1, high_school + 1):
        levels.append(("{}º HS".format(level), "{}º ano medio".format(level)))

    return levels
