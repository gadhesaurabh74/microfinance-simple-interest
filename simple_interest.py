def calculate_simple_interest(principal, rate, time):
    """
    Function to calculate simple interest.
    
    :param principal: The principal amount (float)
    :param rate: Annual interest rate in percentage (float)
    :param time: Time period in years (float)
    :return: Simple interest (float)

    Example:
    >>> calculate_simple_interest(1000, 5, 2)
    100.0
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time in years: "))

    interest = calculate_simple_interest(p, r, t)
    print(f"Simple Interest: {interest}")
