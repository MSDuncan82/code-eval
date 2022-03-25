"""
Given an unordered list of the numbers 1 to 100, we have removed one at random.

Please write a function that takes that list as the input, and returns the missing number.

Use any language you're comfortable with and don't worry about syntax, pseudo code is all we are looking for.”
"""


def find_missing_number_w_sets(num_list: list) -> int:
    """
    Use sets to find the missing number
    """
    expected_set = set(range(1, 101))
    input_set = set(num_list)
    missing_number_set = expected_set - input_set

    if len(missing_number_set) > 1:
        raise ValueError(f"More than 1 missing number: {missing_number_set}")
    elif len(missing_number_set) == 0:
        raise ValueError("No numbers were missing from the input set")

    missing_number = list(missing_number_set)[0]
    return missing_number
