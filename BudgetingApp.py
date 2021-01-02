import sqlite3 as sq
import datetime

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
    paycheck = """INSERT INTO paycheck (name, expected_amount, amount, date)
                VALUES ('{}', '{}', '{}', '{}')""".format(name, expected_amount, amount, date)
    c.execute(paycheck)
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

    bill = """INSERT INTO bills (name, expected_amount, amount, date, completed)
               VALUES ('{}', '{}', '{}', '{}', '{}')""".format(name, expected_amount, amount, date, completed)

    c.execute(bill)
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


def check_if_paid():
    c.execute("SELECT name, completed FROM bills;")
    completed = c.fetchall()
    print(completed)


def paid():
    c.execute("SELECT name, completed FROM bills ORDER BY completed ASC;")
    b = c.fetchall()
    for name, yn in b:
        if yn == 'False':
            print(name + " is not paid yet.")
        if yn == 'True':
            print(name + " has been paid this month.")


def main():
    while True:
        option = input("what do you want to do?\n"
                       "1. add bill\n"
                       "2. add paycheck\n"
                       "3. see total of monthly bill\n"
                       "4. see total paychecks for the month\n"
                       "5. see bill to chek differance\n"
                       "6. see expected bills\n"
                       "7. see expected paychecks\n"
                       "8. see what has been paid\n"
                       "9. Print unpaid\n"
                       "0. exit\n"
                       "what do you want to do? ")

        if option == "1":
            add_bill()

        elif option == "2":
            add_paycheck()

        elif option == "3":
            print(sum_of_bill())

        elif option == "4":
            print(sum_of_paycheck())

        elif option == "5":
            print(difference_bill_and_paycheck())

        elif option == "6":
            print(expected_sum_of_bill())

        elif option == "7":
            print(sum_of_expected_paycheck())

        elif option == "8":
            print(paid())

        elif option == "9":
            see_all()

        elif option == "0":
            return False


def see_all():
    c.execute('SELECT * FROM bills')
    print(c.fetchall())
    c.execute('SELECT * FROM paycheck')
    print(c.fetchall())


# see_all()
#paid()
main()
check_if_paid()
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

# use paycheck history to orginize which bills should be paid with which check
