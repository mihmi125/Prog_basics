"""Function examples."""


def func():
    """Print a message indicating the function is running."""
    print("I´m inside the function")


def my_name_is(name: str):
    """Print the name passed as argument."""
    print(f"My name is {name}")


def sum_six(num: int):
    """Return the sum of the given number and six."""
    return num + 6


def sum_numbers(num_a: int, num_b: int):
    """Return the sum of two given numbers."""
    return num_a + num_b


def usd_to_eur(usd: int):
    """Convert USD amount to EUR using a fixed exchange rate."""
    return usd * 0.8
