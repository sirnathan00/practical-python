# mortgage.py
#
# Exercise 1.7

from operator import ne


need_to_pay = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
start_extra = 61
end_extra = 108
extra_pay = 1000
while need_to_pay > 0:
    if months >= start_extra and months <= end_extra:
        need_to_pay = need_to_pay * (1+rate/12) - (payment + extra_pay)
        total_paid = total_paid + (payment + extra_pay)
        months = months + 1
    else:
        need_to_pay = need_to_pay * (1+rate/12) - payment
        total_paid = total_paid + payment
        months = months + 1
    print(months, total_paid, round(need_to_pay,2))

print('total paid', total_paid, 'months', months)