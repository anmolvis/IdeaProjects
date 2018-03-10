def check_answers(my_answer, correct_answer):
    result = []
    ok = 0
    for i in range(len(my_answer)):
        result.append(check(my_answer[i], correct_answer[i]))

    for results in result:
        if results:
            ok +=1
    return declare(ok)


def check(ans, correct_ans):
    if ans == correct_ans:
        return True
    else:
        return False


def declare(num):
    if num/5 > .7:
        return "Congratulations, you passed the test! You scored " + str(num) + " out of 5."
    else:
        return "Unfortunately, you did not pass. You scored " + str(num) + " out of 5."


print(check_answers([4,3,6,2,7],[4,5,6,4,7]))