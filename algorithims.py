import datetime
import BudgetingApp
# tracking when to pay each bill
import sqlite3 as sq

con = sq.connect("Budgetingapp.db")
c = con.cursor()


def duedate():
    currbill = []
    c.execute("SELECT name, completed, date, amount FROM bills")
    b = c.fetchall()
    for name, yn, date, amount in b:
        if yn == 'False':
            print(name + " is not paid yet.")
            currbill.append((name, date, amount))

        if yn == 'True':
            print(name + " has been paid this month.")
    print(currbill)

    pday = []
    c.execute("SELECT name, date, amount FROM paycheck")
    p = c.fetchall()
    for name, date, amount in p:
        pday.append((name, date, amount))
        print(pday)
        thisPD =[]
        nextPD = []
        tday = datetime.date.today()
    for date in pday:

        if tday <= date:
            thisPD.append((name, date, amount))
    print(thisPD)

duedate()

# class Bill:
#     def __init__(self, name, amount, expected_amount, date, completed):
#         self.name = name
#         self.amount = amount
#         self. expected_amount = expected_amount
#         self. date = date
#         self.completed = completed
#
#
# # taking the bills that have not been paid
#
#     def check_dates(self,name, date, amount, completed):
#         first_list= []
#         thisPD = []
#         nextPD = []
#         next_payday = "however you do biweekly stuff"
#         for name,yn in BudgetingApp.paid():
#             if yn == "False":
#                 first_list.append[self.name,self.date]
#             else:
#                 pass
#
#             for name, notpaid in first_list:
#         # if due date is before next payday put in this payday list
#                 if notpaid => next_payday:
#                     thisPD.append[name, self.amount]
#                     return thisPD
#         # else if due date is after next payday put in next payday list
#                 elif notpaid =< next_payday:
#                     nextPD.append[name, self.amount]
#                     return nextPD
#
#     def what_to_pay(self,thisPD, nextPD):
#         first= sum(thisPD[1])
#         if first => budget:
#             print(thisPD)
#         # do the math to figure out which bills can wait to next payday
#         else:
#             pass


# ordering by due date and amount


# deciding which bill should be paid on which paycheck
