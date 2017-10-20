#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:15:40 2017

@author: hsin
"""
#initialization
portion_saved = 0.0 #cal this

total_cost = 1000000.0
portion_down_payment = 0.25
r = 0.04
semi_annual_raise = 0.07

bi_start = 0
bi_end = 10000
bi_times = 0

# input
annual_salary = input('Enter the starting salary: ')

while bi_end - bi_start > 1:
    bi_mid = int((bi_start + bi_end) / 2)
    monthly_salary = float(annual_salary) / 12.0
    portion_down_cost = total_cost * portion_down_payment
    portion_saved = bi_mid / 10000.0
    c_saving = 0.0
    n_of_months = 0
    while n_of_months < 37:
        n_of_months += 1
        c_saving += monthly_salary * portion_saved * (1.0 + (r / 12.0))
        if (n_of_months % 6) == 0 and n_of_months != 0:
            monthly_salary *= (1 + semi_annual_raise)
    bi_times += 1
    
    if portion_down_cost > c_saving:
        bi_start = bi_mid
    elif portion_down_cost < c_saving:
        bi_end = bi_mid
        

if portion_saved == 0.9999:
    print("It is not possible to pay the down payment in three years")
else:
    print("Best savings rate: " + str(portion_saved))
    print("Steps in bisection search: " + str(bi_times))