#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 21:03:08 2017

@author: hsin
"""

#initialization
annual_salary = 0.0
monthly_salary = 0.0
portion_saved = 0.0
total_cost = 0.0
portion_down_payment = 0.25
current_saving = 0
r = 0.04
semi_annual_raise = 0.0
n_of_months = 0

# input
annual_salary = input('Enter your annual salary: ')
monthly_salary = float(annual_salary) / 12.0
portion_saved = input("Enter your percent of your salary to save, as a decimal: ")
total_cost = input("Enter your cost of your dream home: ")
semi_annual_raise = input("Enter the semi-annual raise, as a decimal: ")

while (float(total_cost) * float(portion_down_payment)) > float(current_saving) :
    current_saving = (float(monthly_salary) * float(portion_saved) + float(current_saving) * (1.0 + (float(r)) / 12))
    n_of_months += 1
    if (n_of_months % 6) == 0:
        monthly_salary *= 1 + float(semi_annual_raise)
1
print("Number of months: " + str(n_of_months))
