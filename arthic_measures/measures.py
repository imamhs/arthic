# Arthic measures library
# Copyright (c) 2024, Md Imam Hossain (emamhd at gmail dot com)
# see LICENSE.txt for details

"""
 Lifelong wealth building financial formulas
"""

def A_calculate_growth(_credit, _frequency, _period, _growth):

    Final_generated_balance = 0

    for yp in range(_period):
        Final_generated_balance += (_credit*_frequency)
        Final_generated_balance += (Final_generated_balance*_growth)

    return round(Final_generated_balance, 3)
