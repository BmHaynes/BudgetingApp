import sqlite3 as sq
import PayingBills

# tracking when to pay each bill

con = sq.connect("Budgetingapp.db")
c = con.cursor()


# organizing bills and paycheck lists

def duedate():
    # making main bill list
    bills_due = []
    c.execute("SELECT name, completed, date, amount FROM bills")
    b = c.fetchall()
    for name, yn, date, amount in b:
        if yn == 'False':
            # print(name + " is not paid yet.")
            bills_due.append((name, date, amount))
            bills_due.sort(key=lambda x: x[2])
    # making main pay_day list
    pay_day = []
    c.execute("SELECT name, date, amount FROM paycheck")
    p = c.fetchall()
    for name, date, amount in p:
        pay_day.append((name, date, amount))
        pay_day.sort(key=lambda x: x[2])

    # bills sorted by first and second paycheck of the month
    bills_first_payday = []
    bills_second_payday = []

    # paycheck sorted by day
    first_payday = int(pay_day[0][1][-2:])
    last_payday = int(pay_day[-1][1][-2:])

    # separating bills into before payday and after and totaling them
    for each in bills_due:
        name, date, amount = each
        if first_payday <= int(date[-2:]) < last_payday:
            bills_first_payday.append(each)
            bills_first_payday_total = float(sum(x[-1] for x in bills_first_payday))
        elif int(date[-2:]) >= last_payday:
            bills_second_payday.append(each)
            bills_second_payday_total = float(sum(x[-1] for x in bills_second_payday))
    # print(bills_first_payday)
    # print(bills_second_payday)

    all_first_checks_total = ""
    all_second_checks_total = ""
    all_first_checks = []
    all_second_checks = []

    # separating each paycheck by date and totaling them
    for all in pay_day:
        name, date, amount = all
        if int(date[-2:]) == first_payday:
            all_first_checks.append(all)
            all_first_checks_total = float(sum(x[-1] for x in all_first_checks))

        if int(date[-2:]) == last_payday:
            all_second_checks.append(all)
            all_second_checks_total = float(sum(x[-1] for x in all_second_checks))

    # print(bills_first_payday_total)
    # print(bills_second_payday_total)
    # print(all_first_checks_total)
    # print(all_second_checks_total)

    # moving overflow of first bills to second list to keep from overdrafting
    # buffer is the amount of money you want left over. idealy should be zero
    buffer = 0
    for each in bills_first_payday:
        name, date, amount = each
        if (bills_first_payday_total + buffer) <= (all_first_checks_total):
            bills_second_payday.append(bills_first_payday[0])

        elif (bills_second_payday_total + buffer) <= (all_second_checks_total):
            bills_first_payday.append(bills_second_payday[0])
        else:
            print("you did not make enough to pay all the bills")
    print(bills_first_payday)
    print(bills_second_payday)

    return bills_first_payday, bills_second_payday, all_first_checks_total, all_second_checks_total

duedate()
bills_first_payday, bills_second_payday, all_first_checks_total, all_second_checks_total = duedate()


# format the bill from the list to the paying bills function
def pay_this_payday_bills():
    for name in bills_first_payday:
        print(name[0])
        if name[0] == "water":
            PayingBills.pay_water()
        elif name[0] == "electric":
            PayingBills.pay_electric()
        elif name[0] == "phone":
            PayingBills.pay_verizon()
        elif name[0] == "house":
            PayingBills.pay_house()
        elif name[0] == "truck":
            PayingBills.pay_truck()




# maybe make it so instead of filling up the first check then having money left over on the second, split the
# bills in alf s close as possiable
