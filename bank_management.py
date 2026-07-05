import os
import pymysql
from datetime import datetime
from datetime import date
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
year = today.year
month= today.month

# Database password is read from an environment variable instead of being
# hardcoded, so it never gets committed to GitHub or shared with others.
# Before running this script, set it in your terminal / system settings, e.g.
#   Windows (Command Prompt):  set DB_PASSWORD=your_password_here
#   Windows (PowerShell):      $env:DB_PASSWORD="your_password_here"
#   macOS/Linux:               export DB_PASSWORD=your_password_here
DB_PASSWORD = os.environ.get("DB_PASSWORD")
if not DB_PASSWORD:
    raise SystemExit(
        "ERROR: DB_PASSWORD environment variable is not set. "
        "Please set it before running this script (see comments above)."
    )

db=pymysql.connect(host="localhost",user="root",password=DB_PASSWORD)
cur=db.cursor()
cur.execute('create database If not exists bank_management;')
cur.execute("use bank_management;")
cur.execute("create table If not exists customer(name varchar(20),Acc_no varchar(12),DOB date,Addhar char(12),Balance decimal(10,2),Mobile_No char(10),passwd varchar(30));")
cur.execute("create table If not exists transaction(Acc_no varchar(12),Date_of_transaction date,Time_of_transaction varchar(10),transaction_amount decimal(10,2),Balance decimal(10,2),Mobile_No char(10),mode_of_transaction varchar (20));")
cur.execute("create table If not exists loan(s_no varchar(100),Acc_no varchar(12),Date_of_issued_money date,amount_of_issued_money decimal(10,2),Balance decimal(10,2),rate varchar (10),period varchar(5),completed date,amount_to_be_paided decimal(20,3));")
cur.execute("create table If not exists fd(s_no varchar(10000),Acc_no varchar(12),Date_of_issue date,amount_of_issued_money decimal(10,2),Balance decimal(10,2),rate varchar(5),date_maturity date,maturity_amount varchar(20));")
a=0
Running = True
while True:
    print("""
      ----
     | -- |
      ----                                         welcome to DFDC bank
    
    
                                      1.Sign  IN
                                      2.Registration
                                      3.Exit the program""")
    NULL='null'
    try:
        a=int(input("enter your choice"))
    except:
        print("enter numerical value")
        continue
    if int(a)==1 or int(a)==2 or int(a)==3:
        cur.execute("select * from customer")
        ac=cur.fetchall()
        if ac==():
            acc="1"
        else:
            for i in ac:
                i=i[1]
                acc=int(i)+1
                acc=str(acc)
        if a==2:
            nm=input("enter your name")
            date1=input("enter your DOB (date)")
            mon = input("enter your DOB (month (in format e.g-1,2,3,4...)")
            yer= input("enter your DOB (year in (format e.g 2009)")
            ad=input("enter aadhaar")
            mb=input("enter your mobile.no")
            passwd=input("enter your password for this account")
            if int(mon)<10:
                mon="0"+mon
            if int(date1)<10:
                date1="0"+date1
            date=yer+"-"+mon+"-"+date1
            p='insert into customer (name,acc_no,DOB,Addhar,Balance,Mobile_No,passwd) values (%s,%s,%s,%s,%s,%s,%s)'
            val=(nm,acc,date,ad,0.00,mb,passwd)
            ads = 1234.56
            cur.execute(p, val)
            db.commit()
            def result(nm,date,ad,mb,acc,passwd):
                accc=acc
                print("your details are as follows:")
                z = "                                                           "
                a=(nm,accc,date,ad,mb)
                while True:
                    if nm==nm:
                        nm=nm+z[:(len(z)-len(nm))]
                    if accc==accc:
                        accc=accc+z[:(len(z) - len(acc))]
                    if date==date:
                        date=date+z[:(len(z) - len(date))]
                    if ad==ad:
                        ad=ad+z[:(len(z) - len(ad))]
                    if mb==mb:
                        mb=mb +z[:(len(z) - len(mb))]
                    if passwd == passwd:
                        passwd = passwd + z[:(len(z) - len(passwd))]
                        break
                print("""
                    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    |NAME                       =""",nm,"""|
                    |ACCOUNT NUMBER             =""",accc,"""|
                    |DATE OF BIRTH(YYYY-MM-DD)  =""",date,"""|
                    |AADHAAR NUMBER             =""",ad,"""|
                    |BALANCE                    = 0.00                                                        | 
                    |MOBILE NUMBER              =""",mb,"""|
                    |PASSWORD                   =""",passwd,"""|
                    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            result(nm,date,ad,mb,acc,passwd)
            while True:
                print("""Press
                        1.For Any Discrepancy
                        2.Go to Home Page""")
                try:
                    w=int(input("enter your choice"))
                except:
                    print("enter numerical value")
                    continue
                if w==1 or w==2:
                    if w==1:
                        wr=input("Enter the name of feild to be corrected(name,dob,password,mobilenumber,aadhaar):")
                        if wr.lower() == 'name':
                            cr = input("Enter the correct value")
                            if len(cr)>20:
                                print("Try a Shorter name")
                                continue
                            else:
                                t = "update customer set name = %s where Acc_no=%s"
                                val = (cr, acc)
                                cur.execute(t, val)
                                db.commit()
                                print("following changes made")
                                nm=cr
                                result(nm, date, ad, mb, acc,passwd)

                        if wr.lower() == 'dob':
                            date1 = input("enter your DOB (date)")
                            mon = input("enter your DOB (month (in format e.g-1,2,3,4...)")
                            yer = input("enter your DOB (year in (format e.g 2009)")
                            if int(mon) < 10:
                                mon = "0" + mon
                            if int(date1) < 10:
                                date1 = "0" + date1
                            date = yer + "-" + mon + "-" + date1
                            t = "update customer set DOB = %s where Acc_no=%s"
                            val = (date, acc)
                            cur.execute(t, val)
                            db.commit()
                            print("following changes made")
                            result(nm, date, ad, mb, acc,passwd)

                        if wr.lower() == 'mobile number' or wr.lower() == 'mobilenumber':
                            cr = input("Enter the correct value")
                            if len(cr) != 10:
                                print("you have written a number greater or lesser than 10 digits")
                                continue
                            else:
                                t = "update customer set Mobile_No = %s where Acc_no=%s"
                                val = (cr, acc)
                                cur.execute(t, val)
                                db.commit()
                                print("following changes made")
                                mb = cr
                                result(nm, date, ad, mb, acc,passwd)

                        if wr.lower() == 'aadhaar':
                            cr = input("Enter the correct value")
                            if len(cr) != 12:
                                print("you have written th number greater or smaller than 12 digits")
                                continue
                            else:
                                t = "update customer set Addhar = %s where Acc_no=%s"
                                val = (cr, acc)
                                cur.execute(t, val)
                                db.commit()
                                print("following changes made")
                                ad = cr
                                result(nm, date, ad, mb, acc,passwd)
                        if wr.lower() == 'password':
                            cr = input("Enter the correct value")
                            if len(cr) > 30:
                                print("you have written th password greater than 30 digits")
                                continue
                            else:
                                t = "update customer set passwd = %s where Acc_no=%s"
                                val = (cr, acc)
                                cur.execute(t, val)
                                db.commit()
                                print("following changes made")
                                passwd = cr
                                result(nm, date, ad, mb, acc,passwd)
                        continue
                    if w==2:
                        break
                else:
                    print("press either 1 or 2")
                    continue

        if a==1:
            id=input("enter your account number here")
            pas=input("enter your password here")
            while True:
                sql="select balance from customer where acc_no=%s and passwd=%s"
                vval=id,pas
                cur.execute(sql, vval)
                op=cur.fetchall()
                try:
                    op=op[0][0]
                except:
                    print("enter correct password or id")
                    break
                print('''
                                YOUR CURRENT BALANCE''',op,'''
                        
                        1.Transaction
                        2.loan
                        3.FD
                        4.log out''')
                try:
                    t=int(input("enter your choice:"))
                except:
                    print("enter numerical value")
                    continue
                if t==1 or t==2 or t==3 or t==4:
                    if t ==1:
                        while True:
                            print("""
                                  1.deopsit money
                                  2.send money
                                  3.preivious menu""")
                            try:
                                b=int(input("enter your choice"))
                            except:
                                print("enter numerical value")
                                continue
                            if b==1 or b==2 or b==3:
                                if b==1:
                                    while True:
                                        try:
                                            a=float(input("the amount to be added is :"))
                                        except:
                                            print("enter numerical value")
                                            continue
                                        j=a+float(op)
                                        h=input("mode of transfer")
                                        t = "update customer set Balance = %s where Acc_no=%s"
                                        val = (j, id)
                                        cur.execute(t, val)
                                        db.commit()
                                        sql = "select mobile_no from customer where acc_no=%s and passwd=%s"
                                        vval = id, pas
                                        cur.execute(sql, vval)
                                        ip = cur.fetchall()
                                        ip = ip[0]
                                        ip = ip[0]
                                        p='insert into transaction (acc_no,Date_of_transaction,Time_of_transaction,transaction_amount,Balance,Mobile_No,mode_of_transaction) values (%s,%s,%s,%s,%s,%s,%s)'
                                        val=(id,today,current_time,a,j,ip,h)
                                        cur.execute(p, val)
                                        db.commit()
                                        print("""                                     
                                        
                                                    Money Transfer successful
                                                    TIME OF TRANSACTION=""",current_time,"""
                                                    DATE OF TANSACTION=""",today,""" 
                                                                          
                                                                          """)
                                        break
                                    break
                                if b==2:
                                    while True:
                                        try:
                                            a=float(input("The Amount to be tansferred"))
                                        except:
                                            print("enter numerical value")
                                            continue
                                        b=input("To the bank account(account number)")
                                        c=input("the mode of transfer")
                                        j = float(op) - a
                                        if j<0:
                                            print("you don't have enough balance")
                                        else:
                                            t = "update customer set Balance = %s where Acc_no=%s"
                                            val = (j, id)
                                            cur.execute(t, val)
                                            db.commit()
                                            sql = "select mobile_no from customer where acc_no=%s and passwd=%s"
                                            vval = id, pas
                                            cur.execute(sql, vval)
                                            ip = cur.fetchall()
                                            ip = ip[0]
                                            ip = ip[0]
                                            p = 'insert into transaction (acc_no,Date_of_transaction,time_of_transaction,transaction_amount,Balance,mobile_no,mode_of_transaction) values (%s,%s,%s,%s,%s,%s,%s)'
                                            val = (id, today,current_time, a, j, ip,c)
                                            cur.execute(p, val)
                                            db.commit()
                                            print("""                                                  Money Transfer successful                 
                                            
                **********************************************************************************************
                                                                                                             """)
                                            break
                                    break

                                if b==3:
                                    break
                            else:
                                print("enter either 1 or 2 ")
                                continue
                        continue
                    elif t ==2:
                        while True:
                            print('''
                                      1.Take a Loan
                                      2.Status of Loans
                                      3.go to priveous menu''')
                            try:
                                input1=int(input("Enter your choice"))
                            except:
                                print("enter numberical value")
                                continue
                            if input1==1 or input1==2 or input1==3:
                                if input1==1:
                                    while True:
                                        try:
                                            b=float(input("enter the amount to be taken as loans "))
                                        except:
                                            print("enter numerical value")
                                            continue
                                        amt=b
                                        try:
                                            c=float(input("enter the time period for which loan is taken in months"))
                                        except:
                                            print("enter numerical value")
                                            continue
                                        print("""          collateral that can be provided from the below           """)
                                        e=input("""            1.gold yes(y) or no(n)""")
                                        f=input("""            2.property papers yes(y) or no(n)""")
                                        r=input("""            3.cars yes(y) or no(n)""")
                                        u=input("""            4.stocks yes(y) or no(n)""")
                                        try:
                                            g=float(input("enter your income"))
                                        except:
                                            print("enter numerical value")
                                            g = float(input("enter your income"))
                                        finally:
                                            if type(g)!=float:
                                                print("kindly enter deails again")
                                            break
                                    try:
                                        if  b>(4*g):
                                            print("Sorry,loans can not be sanctioned.")
                                            break

                                        if e=='y' and  (f=="y" or r=="y" or u=="y") or f=="y"  and (f=="y" or r=="y" or u=="y") or r=="y" and (f=="y" or r=="y" or u=="y") or u=="y" and (f=="y" or r=="y" or u=="y"):
                                            print("""yey!!your loans can be processed "
                                                    following are the details""")
                                            z = "                                                         "
                                            cur.execute("select * from loan")
                                            db.commit()
                                            ac = cur.fetchall()
                                            if ac == ():
                                                sn = "1"
                                            else:
                                                for i in ac:
                                                    i = i[0]
                                                    sn = int(i) + 1
                                                    sn = str(sn)
                                            cur.execute("select * from customer where acc_no=%s", id)
                                            y = cur.fetchall()
                                            nm = y[0][0]
                                            date = str(today)
                                            ad = y[0][3]
                                            mb = y[0][5]
                                            today = str(today)
                                            month = datetime.strftime(now, "%m")
                                            year = datetime.strftime(now, "%Y")
                                            day = datetime.strftime(now, "%d")
                                            year = int(year)+int(c)//12
                                            day = str(day)
                                            day1=int(c)%12
                                            if int(month)+int(day1) < 12:
                                                a1 = int(month) + int(day1)
                                                month = int(a1)
                                                year = int(year)
                                            elif  int(month)+int(day1) > 12:
                                                a1 = int(month) + int(day1)
                                                month = int(a1) - 12
                                                year = int(year) + 1
                                            elif int(month)+int(day1) == 12:
                                                month = 12
                                                year = int(year)
                                            if int(c) % 12 == 0:
                                                month = datetime.strftime(now, "%m")
                                                year = int(year) - 1
                                            month=str(month)
                                            year=str(year)
                                            dat = day + "-" + month + "-" + year
                                            w = float(b) * (0.01012)
                                            w = float(w)+float(b)
                                            w=str(w)
                                            o = str(op)
                                            if nm == nm:
                                                    nm1 = nm + z[:(len(z) - len(nm))]
                                            if id ==id:
                                                id1= id + z[:(len(z) - len(str(id)))]
                                            if date == date:
                                                date = date + z[:(len(z) - len(date))]
                                            if ad == ad:
                                                ad = ad + z[:(len(z) - len(ad))]
                                            if mb == mb:
                                                mb = mb + z[:(len(z) - len(mb))]
                                            if dat == dat:
                                                dat1 = dat + z[:(len(z) - len(dat))]
                                            if w == w:
                                                w = w + z[:(len(z) - len(str(w)))]
                                            if str(sn) == str(sn):
                                                sn1 = str(sn) + z[:(len(z) - len(str(sn)))]
                                            if str(b) == str(b):
                                                b1 = str(b) + z[:(len(z) - len(str(b)))]
                                            print("""
                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                                           
                |S.NO                          =""",sn1,"""|
                |NAME                          =""", nm1, """|
                |ACCOUNT NUMBER                =""", id1, """|
                |DATE_OF_APPROVAL              =""", date, """|
                |AADHAAR NUMBER                =""", ad, """|
                |MOBILE NUMBER                 =""", mb, """|
                |INTEREST_RATE                 = 1.012% per month                                          |
                |AMOUNT_OF_LOAN (TO BE PAIDED) =""", w, """|
                |DATE_OF_LOAN (TO BE PAIDED)   =""", dat1, """|
                +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
                                            dat = year + "-" + month + "-" + day
                                            j = float(op) + float(b)
                                            t = "update customer set Balance = %s where Acc_no=%s"
                                            val = (j, id)
                                            cur.execute(t, val)
                                            db.commit()
                                            cur.execute("select * from loan")
                                            ac = cur.fetchall()
                                            today = str(today)
                                            da = datetime.strptime(today, '%Y-%m-%d')
                                            p = 'insert into loan (s_no,acc_no,Date_of_issued_money,amount_of_issued_money,Balance,rate,period,completed,amount_to_be_paided) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                            val = (sn,id,today, amt, j, "10.12%", c, dat,w)
                                            cur.execute(p, val)
                                            db.commit()
                                            print("""                                               LOAN APPROVED SUCCESFULL
                                                                                THANK YOU """)
                                        else:
                                            print("loan can not be scantioned")
                                    except:
                                        break
                                if input1==2:
                                    z = "                                                         "
                                    cur.execute("select * from loan where acc_no=%s", id)
                                    db.commit()
                                    a = cur.fetchall()
                                    sn = 0
                                    for i in a:
                                        sn = int(sn)
                                        sn = sn + 1
                                        sn = str(sn)
                                        date=i[2]
                                        w=i[3]
                                        w1=i[8]
                                        dat=i[7]
                                        if id == id:
                                            id1 = id + z[:(len(z) - len(str(id)))]
                                        if date == date:
                                            date = str(date) + z[:(len(z) - len(str(date)))]
                                        if dat == dat:
                                            dat1 = str(dat) + z[:(len(z) - len(str(dat)))]
                                        if w == w:
                                            w = str(w) + z[:(len(z) - len(str(w)))]
                                        if str(sn) == str(sn):
                                            sn1 = str(sn) + z[:(len(z) - len(str(sn)))]
                                        if str(w1) == str(w1):
                                            w1 = str(w1) + z[:(len(z) - len(str(w1)))]
                                        if str(dat) == str(dat):
                                            dat = str(dat) + z[:(len(z) - len(str(dat)))]
                                        print("""
                            +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                            |S.NO                          =""", sn1, """|
                            |ACCOUNT NUMBER                =""", id1, """|
                            |DATE_OF_APPROVAL              =""", date, """|
                            |INTEREST_RATE                 = 1.012% per month                                          |
                            |AMOUNT_OF_LOAN                =""", w, """|
                            |AMOUNT_OF_LOAN (TO BE PAIDED) =""", w1, """|
                            |DATE_OF_LOAN (TO BE PAIDED)   =""", dat, """|
                             +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")



                                if input1==3:
                                        break
                            else:
                                print("enter either 1 or 2 or 3")
                                continue
                        continue
                    elif t == 3:
                        while True:
                            print("""   
                                                      1.Make AN FD
                                                      2.See the status of fd
                                                      3.go to previous menu""")
                            try:
                                fd=int(input("enter your choice"))
                            except:
                                print("enter numerical value")
                                continue
                            if fd==1 or fd==2 or fd==3:
                                if fd==1:
                                    while True:
                                        try:
                                            a=float(input("enter the amount to be fixed deposited:"))
                                        except:
                                            print("enter numerical value")
                                            continue
                                        try:
                                            c=int(input("enter the time period for which you would like to keep FD (in months)"))
                                        except:
                                            print("enter numerical value")
                                            continue
                                        break
                                    if float(a)>float(op):
                                        print("the amount entered is more than the balance of the account  ")
                                    else:
                                        z = "                                                                 "
                                        cur.execute("select * from customer where acc_no=%s", id)
                                        y=cur.fetchall()
                                        nm=y[0][0]
                                        accc=y[0][1]
                                        date=str(today)
                                        ad=y[0][3]
                                        mb=y[0][5]
                                        today=str(today)
                                        month = datetime.strftime(now, "%m")
                                        year = datetime.strftime(now,"%Y")
                                        day = datetime.strftime(now,"%d")
                                        year = int(year)+(int(c)//12)
                                        day = str(day)
                                        day1 = int(c) % 12
                                        if int(month)+int(day1) < 12:
                                            a1 = int(month) + int(day1)
                                            month = int(a1)
                                            year = int(year)
                                        elif  int(month)+int(day1) > 12:
                                            a1 = int(month) + int(day1)
                                            month = int(a1) - 12
                                            year = int(year) + 1
                                        elif int(month)+int(day1) == 12:
                                            month = 12
                                            year = int(year)
                                        if int(c) % 12 == 0:
                                            month = datetime.strftime(now, "%m")
                                            year = int(year) - 1
                                        year = str(year)
                                        month=str(month)
                                        dat=day+"-"+month+"-"+year
                                        w = float(a)*(0.00512)*int(c)
                                        w = w + float(a)
                                        w = str(w)
                                        o=str(op)
                                        if nm==nm:
                                            nm=nm+z[:(len(z)-len(nm))]
                                        if accc==accc:
                                            accc=accc+z[:(len(z) - len(acc))]
                                        if date==date:
                                            date=date+z[:(len(z) - len(date))]
                                        if ad==ad:
                                            ad=ad+z[:(len(z) - len(ad))]
                                        if mb==mb:
                                            mb=mb +z[:(len(z) - len(mb))]
                                        if  dat == dat:
                                            datr = dat + z[:(len(z) - len(dat))]
                                        if w==w:
                                            w = w + z[:(len(z) - len(str(w)))]
                                        if o==o:
                                            o = o + z[:(len(z) - len(str(o)))]
                                        if str(a)==str(a):
                                            aa=str(a)+z[:(len(z)-len(str(a)))]
                                        print("""
                                    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |NAME                 =""",nm,"""|
                                    |ACCOUNT NUMBER       =""",accc,"""|
                                    |DATE_OF_TRANSACTION  =""",date,"""|
                                    |AADHAAR NUMBER       =""",ad,"""|
                                    |BALANCE              =""",o,"""| 
                                    |MOBILE NUMBER        =""",mb,"""|
                                    |INTEREST_RATE        = 0.512% per month                                               |
                                    |AMOUNT_OF_FD         =""",aa,"""|
                                    |DATE_OF_MATURITY     =""",datr,"""|
                                    |MATURITY_AMOUNT      =""",w,"""|
                                    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
                                        while True:
                                            print("""PRESS                          
                                                                 1.TO PROCEED
                                                                 2.TO CANCEL
                                                                 3.go to priveous menu
                                                                 """)
                                            try:
                                                cho=int(input("Enter your Choice"))
                                            except:
                                                print("enter numerical value")
                                                continue
                                            if cho==1 or cho==2 or cho==3:
                                                if cho==1:
                                                    dat=year+"-"+month+"-"+day
                                                    j = float(op) - float(a)
                                                    t = "update customer set Balance = %s where Acc_no=%s"
                                                    val = (j, id)
                                                    cur.execute(t, val)
                                                    db.commit()
                                                    cur.execute("select * from transaction")
                                                    ac = cur.fetchall()

                                                    if ac == ():
                                                        acc = "0"
                                                    else:
                                                        for i in ac:
                                                            i = i[0]
                                                            acc = int(i) + 1
                                                            acc = str(acc)
                                                        today=str(today)
                                                        da = datetime.strptime(today, '%Y-%m-%d')
                                                    p = 'insert into fd (s_no,acc_no,Date_of_issue,amount_of_issued_money,Balance,rate,date_maturity,maturity_amount) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                                                    val = (acc,id,da,a,j,"7.12%",dat,w)
                                                    cur.execute(p, val)
                                                    db.commit()
                                                    print("""                                                    MADE FD SUCCESFULL
                                                        THANK YOU """)
                                                    break
                                                if cho==2:
                                                    print("cancelled successfully")
                                                    break
                                                if cho==3:
                                                    break
                                        else:
                                            print("enter either 1 or 2 or 3")
                                        continue
                                elif fd==2:
                                    cur.execute("select * from fd where acc_no=%s", id)
                                    db.commit()
                                    a=cur.fetchall()
                                    sn=0
                                    for i in a:
                                        z = "                                                                 "
                                        sn=int(sn)
                                        sn=sn+1
                                        sn=str(sn)
                                        date=i[2]
                                        date=str(date)
                                        ad=i[3]
                                        ad=str(ad)
                                        dat=i[6]
                                        dat=str(dat)
                                        op=str(op)
                                        w=float(ad)*(7.12/100)+float(ad)
                                        w=i[7]
                                        w=str(w)
                                        if date == date:
                                            date = date + z[:(len(z) - len(date))]
                                        if dat == dat:
                                            dat= dat + z[:(len(z) - len(dat))]
                                        if ad == ad:
                                            ad = ad + z[:(len(z) - len(ad))]
                                        if op==op:
                                            op = op +z[:(len(z) - len(op))]
                                        if sn==sn:
                                            sn = sn + z[:(len(z) - len(sn))]
                                        if str(id)==str(id):
                                            id1 = id + z[:(len(z) - len(str(id)))]
                                        if w==w:
                                            w = w + z[:(len(z) - len(str(w)))]

                                        print("""
                                    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |S_NO                 =""",sn,"""|
                                    |ACCOUNT NUMBER       =""",id1, """|
                                    |DATE_OF_TRANSACTION  =""", date, """|
                                    |AMOUNT_OF_MONEY      =""", ad, """|
                                    |BALANCE              =""", op, """|
                                    |INTEREST_RATE        = 0.512% per month                                                  |
                                    |DATE_OF_MATURITY     =""", dat, """|
                                    |MATURITY_AMOUNT      =""",w,"""|
                                    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
                                elif fd==3:
                                    break
                            else:
                                print("enter either 1 or 2 or 3")
                                continue
                    elif t==4:
                        break
                else:
                    print("enter either 1 or 2 or 3 or 4")
                continue
        if a==3:
            break
    else:
        print("Enter numerical value")
