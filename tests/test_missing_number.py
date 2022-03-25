import pytest

from code_eval.code_eval import find_missing_number_w_sets


@pytest.mark.parametrize("in_list,expected", [(list(range(2, 101)), 1), (list(range(1, 100)), 100)])
def test_missing_number_sets(in_list, expected):
    in_list = list(range(2, 101))
    expected = 1

    output = find_missing_number_w_sets(in_list)

    assert output == expected


def test_missing_number_sets_no_missing_number():
    in_list = list(range(1, 101))

    with pytest.raises(ValueError, match="No numbers were missing from the input set"):
        output = find_missing_number_w_sets(in_list)


def test_missing_number_sets_mult_missing_number():
    in_list = list(range(3, 101))

    with pytest.raises(ValueError, match="More than 1 missing number: {1, 2}"):
        output = find_missing_number_w_sets(in_list)


