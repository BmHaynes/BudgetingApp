import sqlite3 as sq
import datetime
import algorithms

con = sq.connect("Budgetingapp.db")
c = con.cursor()

# create bill and paycheck table
try:
    c.execute('''CREATE TABLE bills (name TEXT, expected_amount REAL, amount REAL, date INTEGER, completed INTEGER)''')
    c.execute('''CREATE TABLE paycheck (name TEXT, expected_amount REAL, amount REAL, date INTEGER)''')
except:
    print("Tables are already created")


# add paycheck self, name, expected_amount, amount, date
def add_paycheck():
    name = input('name on paycheck: ')
    expected_amount = float(input('expected paycheck amount: '))
    amount = float(input('paycheck amount: '))
    date = datetime.date(2021, int(input("month: ")), int(input("day: ")))
    c.execute("""INSERT INTO paycheck (name, expected_amount, amount, date)
                VALUES (?, ?, ?, ?)""", (name, expected_amount, amount, date))
    con.commit()


# add bill self, name, expected_amount, amount, date, completed
def add_bill():
    name = input('name: ')
    expected_amount = float(input('expected amount: '))
    amount = float(input('amount: '))
    date = datetime.date(2021, int(input("month: ")), int(input("day: ")))
    completed = input('Has it been paid? Y/N: ')
    if completed == "y":
        completed = "True"
        print('you selected true')
    elif completed == "n":
        completed = "False"
        print('you selected false')
    else:
        print("invalid input")

    c.execute("""INSERT INTO bills (name, expected_amount, amount, date, completed)
               VALUES (?, ?, ?, ?, ?)""", (name, expected_amount, amount, date, completed))

    con.commit()

    print(completed)


def sum_of_paycheck():
    c.execute("SELECT amount FROM paycheck;")
    columns = c.fetchall()
    b = []
    for i in columns:
        b.append(i[0])
        pc = sum(b)
    return pc


def sum_of_expected_paycheck():
    c.execute("SELECT expected_amount FROM paycheck;")
    columns = c.fetchall()
    check = []
    for i in columns:
        check.append(i[0])
        p = sum(check)
    return p


# math to figure budget
def sum_of_bill():
    c.execute("SELECT amount FROM bills;")
    columns = c.fetchall()
    a = []
    for i in columns:
        a.append(i[0])
        t = sum(a)

    return t


def expected_sum_of_bill():
    c.execute("SELECT expected_amount FROM bills;")
    columns = c.fetchall()
    t = []
    for i in columns:
        t.append(i[0])
    return sum(t)


def difference_bill_and_paycheck():
    print(sum_of_bill())
    print(sum_of_paycheck())
    print((sum_of_paycheck() - sum_of_bill()))


def paid():
    c.execute("SELECT name, completed FROM bills ORDER BY completed ASC;")
    b = c.fetchall()
    for name, yn in b:
        if yn == 'False':
            print(name + " is not paid yet.")
        if yn == 'True':
            print(name + " has been paid this month.")


def delete_bill():
    c.execute("""SELECT name FROM bills""")
    print(c.fetchall())
    remove = input("which bill needs removed? ")
    bill = ("""DELETE FROM bills WHERE name=?""", remove)
    c.execute(bill)
    print("Bill Deleted")


def delete_paychecks():
    remove = input("which paycheck needs removed? ")
    check = ("""DELETE FROM paycheck WHERE name=?""", remove)
    c.execute(check)
    print("Check Deleted")



def main():
    while True:
        option = input("what do you want to do?\n"
                       "1. add bill\n"
                       "2. add paycheck\n"
                       "3. see total of monthly bill\n"
                       "4. see total paychecks for the month\n"
                       "5. see bill to check differance\n"
                       "6. Delete bill\n"
                       "7. Delete paychecks\n"
                       "8. see what will be paid when\n"
                       "9. Pay this paychecks bills\n"
                       "0. exit\n"
                       "what do you want to do? ")

        if option == "1":
            print("")
            print("")
            add_bill()
            print("")
            print("")

        elif option == "2":
            print("")
            print("")
            add_paycheck()
            print("")
            print("")

        elif option == "3":
            print("")
            print("")
            print(sum_of_bill())
            print("")
            print("")

        elif option == "4":
            print(sum_of_paycheck())

        elif option == "5":
            print(difference_bill_and_paycheck())

        elif option == "6":
            delete_bill()

        elif option == "7":
            delete_paychecks()

        elif option == "8":
            print("")
            print("this payday")
            print("together this payday you will bring home " + str(algorithms.all_first_checks_total))
            print(algorithms.bills_first_payday)
            print("for a total of " + str(sum(x[-1] for x in algorithms.bills_first_payday)))
            print("next payday ")
            print("together next payday you will bring home " + str(algorithms.all_second_checks_total))
            print(algorithms.bills_second_payday)
            print("for a total of " + str(sum(x[-1] for x in algorithms.bills_second_payday)))
            print("")

        elif option == "9":
            algorithms.pay_this_payday_bills()

        elif option == "0":
            return False


# paid()
main()
# check_if_paid()
# add_bill()
# add_paycheck()
# print(sum_of_bill())
# print(expected_sum_of_bill())
# print(sum_of_paycheck())
# print(sum_of_expected_paycheck())
# difference_bill_and_paycheck()
con.commit()
# close connection
con.close()
