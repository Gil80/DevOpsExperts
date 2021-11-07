# Write a program with variables holding the following:
#     your age
#     first letter of your last name
#     current shekels-dollar currency
#     did you fly abroad (true/False)
#     your apartment number
# print all variables
# add the currency to your age and check the result

def askYesNoQuestion(question):
    yesNoAnswer = input(question).lower()
    if yesNoAnswer == "yes" or yesNoAnswer == "no":
        return yesNoAnswer
    else:
        return askYesNoQuestion(question)