# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
def prompt(message):
	print(f'=> {message}')

prompt('Welcome to Calculator!')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('What is the first number?')
number1 = input()
while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt('What is the second number?')
number2 = input()
while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()


prompt('''What operation would you like to perform?
	  1) add
	  2) subtract
	  3) multiply
	  4) divide''')
operation = input()
while operation not in ['1','2','3','4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:
	case '1':
		output = int(number1) + int(number2)
	case '2':
		output = int(number1) - int(number2)
	case '3':
		output = int(number1) * int(number2)
	case '4':
		output = int(number1) / int(number2)

prompt(f'The result is {output}')