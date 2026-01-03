expenses_list = []
budget = int(input('Enter the budget to spend the expenses : '))

def total_expenses(expense_amount):
    total_expense_list = []
    for pay in expense_amount:
        total_expense_list.append(pay['amount'])

    
    return sum(total_expense_list)




def add_your_expense(name,category,amount):
    
    expense_dict = {}
    expense_dict['name'] = name
    expense_dict['category'] = category
    expense_dict['amount'] = amount
    expenses_list.append(expense_dict)

    total = total_expenses(expenses_list)
    print(f'Expenses_list : {expenses_list}')
    print(f'Total_expenses : {total}')

    if total > budget:
        print('Your expenses crossed the budget please check it and validate your expenses')

    else:
        print(f'Available balance : {budget - total}')



add_your_expense('Coffee', 'Cold Coffee', 300)
add_your_expense('Game', 'Indoor Game', 400)





