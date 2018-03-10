def convert_to_numeric(num):
    return float(num)


def sum_of_middle_three(num1, num2, num3, num4, num5):
        maxi = max(num1, num2, num3, num4, num5)
        mini = min(num1, num2, num3, num4, num5)
        return num1+num2+num3+num4+num5-maxi-mini


def score_to_rating_string(avg):
    if 0 <= avg < 1:
        return "Terrible"
    elif 1 <= avg < 2:
        return "Bad"
    elif 2 <= avg < 3:
        return "OK"
    elif 3 <= avg < 4:
        return "Good"
    elif 4 <= avg < 5:
        return "Excellent"


def scores_to_rating(sc1, sc2, sc3, sc4, sc5):
    sc1 = convert_to_numeric(sc1)
    sc2 = convert_to_numeric(sc2)
    sc3 = convert_to_numeric(sc3)
    sc4 = convert_to_numeric(sc4)
    sc5 = convert_to_numeric(sc5)

    avg = sum_of_middle_three(sc1, sc2, sc3, sc4, sc5)/3

    return score_to_rating_string(avg)

print(scores_to_rating("1", 0, 0, "1", 5))
