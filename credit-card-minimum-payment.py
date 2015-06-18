# We would like minimum amount of money which is a multiple of 10$ ... to pay all the balance in 12 month
balance = 3926.
remain_balance = balance
annualInterestRate = 0.2
total_paid = 0. 
fix_payment = 0. 

while remain_balance > 0:
    fix_payment += 10
    remain_balance = balance
    for i in range(1,13):
        pay_each_month = fix_payment
        remains = remain_balance - pay_each_month
        interest = remains * annualInterestRate * 1./12. 
        remain_balance = remains + interest
        total_paid += pay_each_month
        #print "pay each month:" ,pay_each_month
        #print "remains" , remains
        #print "interest: " , interest
        #print "remain balance", remain_balance

         
print "Lowest Payment" , fix_payment
