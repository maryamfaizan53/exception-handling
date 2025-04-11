from typing import Tuple, Dict, List

def generate_random_data(num_samples: int) -> List[Tuple[int, int]]:
    """Generates a list of random number pairs."""
    try:
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("Number of samples must be a positive integer.")
        data = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_samples)]
        return data
    except ValueError as ve:
        print(f"Error: {ve}")
        return []  # Return empty list on error
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []


def calculate_ratios(data: List[Tuple[int, int]]) -> List[float]:
    """Calculates the ratio of the first number to the second in each pair."""
    ratios = []
    try:
        for pair in data:
            num1, num2 = pair
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            if not isinstance(num1,int) or not isinstance(num2,int):
                raise TypeError("Input data must be integers.")
            ratio = num1 / num2
            ratios.append(ratio)
        return ratios
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
        return []  # Return empty list on error.
    except TypeError as te:
        print(f"Error: {te}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during ratio calculation: {e}")
        return []


def process_data(num_samples: int) -> List[float]:
    """Combines data generation and ratio calculation with comprehensive error handling."""

    data = generate_random_data(num_samples)
    if not data: # check if generate_random_data returns an empty list which means it had an error
        return []

    ratios = calculate_ratios(data)

    return ratios

# Example usage with error handling
try:
  num_samples = 10
  results = process_data(num_samples)

  if results:
    print("Calculated ratios:", results)
  else: # if process_data returned an empty list it means there was some error
      print("Data processing failed due to an error.")

except Exception as e: # catching unexpected errors
    print(f"An unexpected error occurred: {e}")

# example of invalid input
results = process_data(-5)
if not results:
  print("Negative number of samples, data processing failed.")

results = process_data("abc")
if not results:
    print("Invalid input type, data processing failed.")

