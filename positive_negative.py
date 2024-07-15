

# x  = int(input('Enter a number:'))
# if(x>0):
#     print(x+'Positive number')
# elif(x==0):
#     print('Number is neither 0')
# else:
#     print('Negative number')

'''
x = int(input('Enter'))
if(x>0):
    print('+ve')
elif(x==0):
    print('Zero')
else:
    print('-ve')       
'''








'''


The line if __name__ == "__main__": in the code is a common Python idiom used to ensure that certain code is only executed when the script is run directly, and not when it is imported as a module in another script. Here's a detailed explanation:

Explanation of __name__ and __main__:
__name__ Variable: */ 

In Python, every module (file) has a built-in attribute called __name__.
When a module is run directly, the __name__ attribute is set to "__main__".
If the module is imported into another module, the __name__ attribute is set to the module's name (e.g., check_number_module if the file name is check_number_module.py).
Purpose of if __name__ == "__main__"::

This condition checks if the module is being run directly.
If __name__ is equal to "__main__", it means that the script is executed directly (not imported).
Code inside this block is executed only when the script is run directly.
Application in Your Code:
In your provided code, the if __name__ == "__main__": block is used to run the main program logic only when the script is executed directly. Here's the code again for reference:

python
Copy code
# Function to check if a number is positive or negative
def check_number(number):
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Main program
if __name__ == "__main__":
    # Input from the user
    num = float(input("Enter a number: "))
    
    # Check the number and print the result
    result = check_number(num)
    print(result)
What Happens:
Function Definition:

The check_number function is defined to check whether a number is positive, negative, or zero.
Main Program Block:

The if __name__ == "__main__": block contains the main logic of the program:
It prompts the user to enter a number.
It calls the check_number function with the user input.
It prints the result returned by the check_number function.
Why It Matters:
Direct Execution:
When you run this script directly (python script_name.py), the condition is true, so the input prompt and function call are executed.
Imported as a Module:
If you import this script in another module (import script_name), the condition is false, so the input prompt and function call are not executed. This allows you to use the check_number function without running the script's main logic.
Example of Importing:
python
Copy code
# another_script.py
import script_name

# Use the function defined in the imported module
result = script_name.check_number(10)
print(result)
In this example, the check_number function can be used in another_script.py without executing the input prompt and print statements from the original script. This separation of functionality is crucial for writing reusable and modular code.



'''

# def check_num(num):
#     if(num>0):
#         return 'no is +ve'
#     else:
#         return 'num is -ve'

# if __name__ =='__main__':
#     number = float(input('Enter the number:'))
#     output =  check_num(number)
#     print(output)

