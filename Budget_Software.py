import json
from pathlib import Path
budget_dict = {}
with open('C:\\Users\\Sebeast\\Documents\\Script\\Budget.txt', 'r') as file:
    budget_dict = json.load(file)

import locale
locale.setlocale( locale.LC_ALL, '' )

#subcategory_was_made = 'no'
def update_budget():
    budget_dict['checking_savings'] = checking_savings
    budget_dict['checking_spending'] = checking_spending
    budget_dict['savings_taxes'] = savings_taxes
    budget_dict['checking_needs'] = checking_needs
    budget_dict['savings_savings'] = savings_savings
    budget_dict['checking_total'] = checking_total
    budget_dict['savings_total'] = savings_total 
    with open('C:\\Users\\Sebeast\\Documents\\Script\\Budget.txt', 'w') as file:
        file.write(json.dumps(budget_dict))

def print_budget():
    print("This is how much money is in your checking account that you are saving for later: " + locale.currency( checking_savings, grouping=True ) + "\nThis is how much money you have in your checking account that you can spend now: " + locale.currency( checking_spending, grouping=True ) + "\nThis is how much money you have available to spend on things you need: " + locale.currency( checking_needs, grouping=True ) + "\nChecking Total: " + locale.currency( checking_total, grouping=True ) + "\nThis is how much money you are saving for taxes: " + locale.currency( savings_taxes, grouping=True ) + "\nThis is how much money you are saving for emergencies and low-risk investments: " + locale.currency( savings_savings, grouping=True ) + "\nSavings Total: " + locale.currency( savings_total, grouping=True ) + "\n")

checking_savings = float(budget_dict.get("checking_savings"))
#print(checking_savings)
checking_spending = float(budget_dict.get("checking_spending"))
#print(checking_spending)
checking_needs = float(budget_dict.get("checking_needs"))
#print(checking_needs)
checking_total = checking_savings + checking_spending + checking_needs
#print(checking_total)

savings_taxes = float(budget_dict.get("savings_taxes"))
#print(savings_taxes)
savings_savings = float(budget_dict.get("savings_savings"))
#print(savings_savings)
savings_total = savings_taxes + savings_savings
#print(savings_account)

tax_from_daily_income = 0.0
daily_income_after_taxes = 0.0
needs_money_from_daily_income_after_taxes = 0.0
wants_money_from_daily_income_after_taxes = 0.0
saving_money_from_daily_income_after_taxes = 0.0

while True:
    #prompt_user:
        #msg_to_prompt = input('What would you like to do\nA: record expense\nB: record income\nC: make a direct change\nD: customize percentage of income going to needs, wants, and savings\nE: create category under needs, wants, or savings and set desired percent of income going to it\nF: quit\nG: Show me where my money is\nPlease enter one of the above letters:\n')
        #record expense:
        # record income:
        # make change to values:
        # set percentage of money going to needs, wants, and savings:
        # create subsets of needs, wants, and savings and set percents for them:
        #quit
        #Show where money is
    msg_to_prompt = ''
    msg_to_prompt = input('What would you like to do\nA: record expense\nB: record income\nC: make a direct change\nD: create sub-category for checking or savings account\nE: customize percent of income that is distributed among the sub-categories\nF: Show me where my money is\nG: quit\nPlease enter one of the above letters:\n')
    if msg_to_prompt == 'A' or msg_to_prompt == 'a':
        msg_to_prompt = float(input('How much was the expense? '))
        expense = msg_to_prompt
        msg_to_prompt = input('Where will the money come out of?\nA: checking_savings\nB: checking_spending\nC: savings_taxes\nD: checking_needs\nE: savings_savings\n')
        if msg_to_prompt == 'A' or msg_to_prompt == 'a':
            checking_savings = checking_savings - expense
            checking_total = checking_savings + checking_spending + checking_needs
            update_budget()
            print_budget()
        elif msg_to_prompt == 'B' or msg_to_prompt == 'b':
            checking_spending = checking_spending - expense
            checking_total = checking_savings + checking_spending + checking_needs
            update_budget()
            print_budget()
        elif msg_to_prompt == 'C' or msg_to_prompt == 'c':
            savings_taxes = savings_taxes - expense
            savings_total = savings_taxes + savings_savings
            update_budget()
            print_budget()
        elif msg_to_prompt == 'D' or msg_to_prompt == 'd':
            checking_needs = checking_needs - expense
            checking_total = checking_savings + checking_spending + checking_needs
            update_budget()
            print_budget()
        elif msg_to_prompt == 'E' or msg_to_prompt == 'e':
            savings_savings = savings_savings - expense
            savings_total = savings_taxes + savings_savings
            update_budget()
            print_budget()
    elif msg_to_prompt == 'B' or msg_to_prompt == 'b':
        daily_income = float(input("How much did you make today: "))
        if daily_income > 0.0:
            #take tax money out:
            tax_from_daily_income = daily_income * .115
            #update savings_taxes:
            savings_taxes = savings_taxes + tax_from_daily_income
            #create daily_income_after_taxes
            daily_income_after_taxes = daily_income - tax_from_daily_income
            #split wants mony:
            wants_money_from_daily_income_after_taxes = ((daily_income_after_taxes * .3) / 2)
            #update checking_savings:
            checking_savings = checking_savings + wants_money_from_daily_income_after_taxes
            #udpate checking_sppending
            checking_spending = checking_spending + wants_money_from_daily_income_after_taxes
            #take out needs money from daily income:
            needs_money_from_daily_income_after_taxes = daily_income_after_taxes * .5
            #update savings:
            checking_needs = checking_needs + needs_money_from_daily_income_after_taxes
            #take out savings:
            saving_money_from_daily_income_after_taxes = daily_income_after_taxes * .2
            #update savings
            savings_savings = savings_savings + saving_money_from_daily_income_after_taxes
            #update checking total:
            checking_total = checking_savings + checking_spending + checking_needs
            #update savings total:
            savings_total = savings_taxes + savings_savings
            update_budget()
            print_budget()
    elif msg_to_prompt == 'C' or msg_to_prompt == 'c':
        change = float(input("How much of a change would you like to make: "))
        if change > 0.0 or change < 0.0:
            msg_to_prompt = input('Which account would you like to change?\nA: checking_savings\nB: checking_spending\nC: savings_taxes\nD: checking_needs\nE: savings_savings\n')
            if msg_to_prompt == 'A' or msg_to_prompt == 'a':
                checking_savings = checking_savings + change
                checking_total = checking_savings + checking_spending + checking_needs
                update_budget()
                print_budget()
            elif msg_to_prompt == 'B' or msg_to_prompt == 'b':
                checking_spending = checking_spending + change
                checking_total = checking_savings + checking_spending + checking_needs
                update_budget()
                print_budget()
            elif msg_to_prompt == 'C' or msg_to_prompt == 'c':
                savings_taxes = savings_taxes + change
                savings_total = savings_taxes + savings_savings
                update_budget()
                print_budget()
            elif msg_to_prompt == 'D' or msg_to_prompt == 'd':
                checking_needs = checking_needs + change
                checking_total = checking_savings + checking_spending + checking_needs
                update_budget()
                print_budget()
            elif msg_to_prompt == 'E' or msg_to_prompt == 'e':
                savings_savings = savings_savings + change
                savings_total = savings_taxes + savings_savings
                update_budget()
                print_budget()
    elif msg_to_prompt == 'G' or msg_to_prompt == 'g':
        quit()
    elif msg_to_prompt == 'F' or msg_to_prompt == 'f':
        print_budget()
