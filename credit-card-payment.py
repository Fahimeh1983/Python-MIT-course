#credit card payment and interest
balance = 4213. # this is the balance and for the rest of the year, i will just pay the minimun each month and not buying 
an_interest_rate = 20./100.
mon_payment_rate = 4./100.
total_paid = 0. 

for i in range (1,13) :
    min_mon_payment = mon_payment_rate * balance
    remain_balance = balance - min_mon_payment
    mon_interest = an_interest_rate * 1./12. * remain_balance
    balance = remain_balance +  mon_interest
    total_paid += min_mon_payment  
    print "Month: ", i
    print "Minimum monthly payment: ", "%0.2f" % min_mon_payment
    print "Remaining balance:","%0.2f" % balance

print "Total paid: " , "%0.2f" %   total_paid
print "Remaining balance:","%0.2f" % balance
