"""Loop exercises."""


def sum_between(start: int, end: int) -> int:
    """Return sum of integers between start and end (both included)."""
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


def sum_of_even_numbers(n: int) -> int:
    """Return sum of even numbers from 0 up to n (included)."""
    total = 0
    for i in range(0, n + 1, 2):
        total += i
    return total


def sum_of_multiples(n: int, end: int) -> int:
    """Return sum of numbers which are multiples of n between 0 and end (included)."""
    total = 0
    for i in range(0, end + 1, n):
        total += i
    return total


def cross_sum(numbers: str) -> int:
    """Return cross sum of numbers."""
    total = 0
    for digit in numbers:
        total += int(digit)
    return total


def multiply_between(start: int, end: int) -> int:
    """Multiply all numbers between start and end (both included)."""
    product = 1
    for i in range(start, end + 1):
        product *= i
    return product


def make_hola_string(count: int) -> str:
    """Make hola string."""
    result = ""
    for _ in range(count):
        result += "hola"
    return result


def compound_interest(amount: int, years: int, rate: int) -> float:
    """Calculate compound interest."""
    result = amount
    for _ in range(years):
        result *= (1 + rate / 100)
    return result


def remove_vowels(original_string: str) -> str:
    """Return the given string without vowels (English + Estonian)."""
    vowels = "aeiouõäöüAEIOUÕÄÖÜ"
    result = ""
    for ch in original_string:
        if ch not in vowels:
            result += ch
    return result


if __name__ == '__main__':
    print(sum_between(3, 5))  # => 12
    print(sum_between(5, 5))  # => 5
    print(sum_of_even_numbers(5))  # => 6
    print(sum_of_even_numbers(0))  # => 0

    print(sum_of_multiples(3, 10))  # => 18
    print(sum_of_multiples(7, 10))  # => 7
    print(sum_of_multiples(11, 10))  # => 0

    print(cross_sum("1234"))  # => 10
    print(cross_sum("0"))  # => 0
    print(cross_sum("4129458"))  # => 33

    print(multiply_between(1, 3))  # => 6
    print(multiply_between(4, 14))  # => 14529715200
    print(multiply_between(0, 7))  # => 0

    print(make_hola_string(3))  # => "holaholahola"
    print(make_hola_string(0))  # => ""

    print(compound_interest(100, 2, 2))  # => 104.04
    print(compound_interest(2000, 6, 8))  # => 3173.748645888
    print(remove_vowels("tere-tere"))  # => tr-tr
    print(remove_vowels("hklmn"))  # => hklmn
    print(remove_vowels("aauuiii"))  # => ""
