import datetime
import sqlite3 as sq

# tracking when to pay each bill

con = sq.connect("Budgetingapp.db")
c = con.cursor()


def duedate():
    currbill = []
    c.execute("SELECT name, completed, date, amount FROM bills")
    b = c.fetchall()
    for name, yn, date, amount in b:
        if yn == 'False':
            #print(name + " is not paid yet.")
            currbill.append((name, date, amount))

#        if yn == 'True':
            #print(name + " has been paid this month.")
    #print(currbill)

    pday = []
    thisPD =[]
    twoweeks = datetime.timedelta(days=14)
    c.execute("SELECT name, date, amount FROM paycheck")
    p = c.fetchall()
    for name, date, amount in p:
        pday.append((name, date, amount))
    print(pday)
    print(currbill)




    # for name, date, amount in currbill:
    #     if currbill(1[1]) < pday(1[1]):
    #         thisPD.append((name, date, amount))
    # print(thisPD)





duedate()


# I need to check to see if the date of
