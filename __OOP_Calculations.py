# Main Programmer for this Class: Porcare, Dana E.
class EmployeePayroll:
    def __init__(self):
        self.basic_pay = 0
        self.honorarium = 0
        self.other_pay = 0
        self.gross_income = 0
        self.sss_contribution = 0
        self.philhealth_contribution = 0
        self.income_tax_contribution = 0
        self.pagIBIG_contribution = 0
        self.regular_deductions = 0
        self.other_deductions = 0
        self.total_deductions = 0
        self.net_income = 0

    def get_basic_income_data(self, rate_per_hour1, no_of_hours_per_cutoff1):
        self.rate_per_hour1 = rate_per_hour1
        self.no_of_hours_per_cutoff1 = no_of_hours_per_cutoff1
        self.basic_pay = self.rate_per_hour1 * self.no_of_hours_per_cutoff1
        return "%.2f" % round(self.basic_pay, 2)

    def get_honorarium_income_data(self, rate_per_hour2, no_of_hours_per_cutoff2):
        self.rate_per_hour2 = rate_per_hour2
        self.no_of_hours_per_cutoff2 = no_of_hours_per_cutoff2
        self.honorarium_pay = self.rate_per_hour2 * self.no_of_hours_per_cutoff2
        return "%.2f" % round(self.honorarium_pay, 2)

    def get_other_income_data(self, rate_per_hour3, no_of_hours_per_cutoff3):
        self.rate_per_hour3 = rate_per_hour3
        self.no_of_hours_per_cutoff3 = no_of_hours_per_cutoff3
        self.other_pay = self.rate_per_hour3 * self.no_of_hours_per_cutoff3
        return "%.2f" % round(self.other_pay, 2)

    def calculate_gross_income(self):
        self.gross_income = self.basic_pay + self.honorarium_pay + self.other_pay
        return "%.2f" % round(self.gross_income, 2)

    def calculate_sss_contribution(self, gross_income):
        if gross_income < 4250.00:
            self.sss_contribution = 180.00
        else:
            for i in range(69):
                if gross_income > 19749.99:
                    self.sss_contribution = 900.00
                    break
                elif 4250.00 + (500 * (i - 1)) <= gross_income <= (4749.99 + (500 * (i - 1))):
                    self.sss_contribution = 180.00 + (22.50 * i)
        return "%.2f" % round(self.sss_contribution, 2)

    def calculate_philhealth_contribution(self, gross_income):
        if gross_income < 10000.00:
            self.philhealth_contribution = 0.00
        elif 10000.00 <= gross_income < 90000.00:
            self.philhealth_contribution = float(0.045 * gross_income)
        else:
            self.philhealth_contribution = 4050.00
        return "%.2f" % round(self.philhealth_contribution, 2)

    def calculate_pagIBIG_contribution(self):
        self.pagIBIG_contribution = 100.00
        return "%.2f" % round(self.pagIBIG_contribution, 2)

    def calculate_income_tax(self, gross_income):
        if gross_income <= 10417.00:
            self.income_tax_contribution = 0
        elif 10417 < gross_income <= 16666.00:
            self.income_tax_contribution = 0 + ((gross_income - 10417.00) * 0.15)
        elif 16666.00 < gross_income <= 33332.00:
            self.income_tax_contribution = 937.50 + ((gross_income - 16667.00) * .20)
        elif 33333.00 < gross_income <= 83332.00:
            self.income_tax_contribution = 4270.00 + ((gross_income - 33333.00) * 0.25)
        elif 83332.00 < gross_income <= 333332.00:
            self.income_tax_contribution = 16770.70 + ((gross_income - 83333.00) * 0.30)
        else:
            self.income_tax_contribution = 91770.70 + ((gross_income - 333333.00) * 0.35)
        return "%.2f" % round(self.income_tax_contribution, 2)

    def get_regular_deductions(self):
        self.regular_deductions = self.sss_contribution + self.philhealth_contribution + self.pagIBIG_contribution + self.income_tax_contribution
        return "%.2f" % round(self.regular_deductions, 2)

    def get_other_deductions(self, sss_loan, pagIBIG_loan, faculty_saving_deposit, faculty_saving_loan, salary_loan, other_loan):
        self.sss_loan = sss_loan
        self.pagIBIG_loan = pagIBIG_loan
        self.faculty_saving_deposit = faculty_saving_deposit
        self.faculty_saving_loan = faculty_saving_loan
        self.salary_loan = salary_loan
        self.other_loan = other_loan
        self.other_deductions = self.sss_loan + self.pagIBIG_loan + self.faculty_saving_deposit + self.faculty_saving_loan + self.salary_loan + self.other_loan
        return "%.2f" % round(self.other_deductions, 2)

    def calculate_total_deductions(self):
        self.total_deductions = self.regular_deductions + self.other_deductions
        return "%.2f" % round(self.total_deductions, 2)

    def calculate_net_income(self):
        self.net_income = self.gross_income - self.total_deductions
        return "%.2f" % round(self.net_income, 2)