def prompt(message):
	print(f'=> {message}')

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True

    return False

while True:
    prompt('------------------------')

    prompt('Welcome to the Mortgage/ Car loan calculator!')
    prompt('What is the total loan amount?')
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt('Please enter a positive number')
    loan_amount = input()

    prompt('What is the Annual Percentage Rate? (APR)')
    apr = input()
    while invalid_number(apr):
        prompt('Please enter a positive number')
    apr = input()

    prompt('What is the loan duration in months?')
    loan_duration = input()
    while invalid_number(loan_duration):
            prompt('Please enter a positive number')
            loan_duration = input()


    prompt('Calculating...')


    monthly_interest = (int(apr) / 12) / 100.0
    monthly_payment = int(loan_amount) * (
        monthly_interest /
            (1 - (1 + monthly_interest) ** (-int(loan_duration))))
    m = round(monthly_payment, 2)
    prompt(f'Your monthly payment is: {m}')

    prompt('Would you like to do another calculation? (Y/N)')
    answer = input().lower()
    if answer[0] == 'n':
        break

prompt('Thanks for using the calculator!')