def perform_operation(num1, num2, operation):
    # Perform addition
    if operation == 'add':
        return num1 + num2
    # Perform subtraction
    elif operation == 'subtract':
        return num1 - num2
    # Perform multiplication
    elif operation == 'multiply':
        return num1 * num2
    # Perform division, with error handling for division by zero
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation"