def safe_divide(numerator, denominator):
    try:
        # Convert the inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."