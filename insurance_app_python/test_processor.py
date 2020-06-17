import pytest
from process import *

cases = [
    # claims, age, premium_increase, warning_letter_enum, is_policy_canceled, is_error
    [process(0, 15), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],
    [process(0, 16), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],
    [process(0, 17), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],

    [process(0, 25), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],
    [process(0, 26), AutoInsuranceAction(25, WarningLetterEnum.NONE, False, False)],
    [process(0, 27), AutoInsuranceAction(25, WarningLetterEnum.NONE, False, False)],

    [process(0, 84), AutoInsuranceAction(25, WarningLetterEnum.NONE, False, False)],
    [process(0, 85), AutoInsuranceAction(25, WarningLetterEnum.NONE, False, False)],
    [process(0, 86), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],

    [process(1, 15), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],
    [process(1, 16), AutoInsuranceAction(100, WarningLetterEnum.LTR1, False, False)],
    [process(1, 17), AutoInsuranceAction(100, WarningLetterEnum.LTR1, False, False)],

    [process(1, 25), AutoInsuranceAction(100, WarningLetterEnum.LTR1, False, False)],
    [process(1, 26), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],
    [process(1, 27), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],

    [process(1, 84), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],
    [process(1, 85), AutoInsuranceAction(50, WarningLetterEnum.NONE, False, False)],
    [process(1, 86), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],

    [process(2, 15), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],
    [process(2, 16), AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)],
    [process(2, 17), AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)],

    [process(2, 25), AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)],
    [process(2, 26), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],
    [process(2, 27), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],

    [process(2, 84), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],
    [process(2, 85), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],
    [process(2, 86), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],

    [process(4, 15), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],
    [process(4, 16), AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)],
    [process(4, 17), AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)],

    [process(4, 25), AutoInsuranceAction(400, WarningLetterEnum.LTR2, False, False)],
    [process(4, 26), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],
    [process(4, 27), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],

    [process(4, 84), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],
    [process(4, 85), AutoInsuranceAction(200, WarningLetterEnum.LTR3, False, False)],
    [process(4, 86), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],

    [process(5, 26), AutoInsuranceAction(0, WarningLetterEnum.NONE, True, False)],
    [process(6, 26), AutoInsuranceAction(0, WarningLetterEnum.NONE, True, False)],
    [process(5, 80), AutoInsuranceAction(0, WarningLetterEnum.NONE, True, False)],

    [process(-1, 80), AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)],
]
@pytest.mark.parametrize("data", cases)
def test_processor_tests(data):
    result = data[0]
    expected = data[1]
    assert(expected == result)

def test_should_error_above_85_years():
    actual = process(0, 90)
    expected = AutoInsuranceAction(-1, WarningLetterEnum.NONE, False, True)
    assert(expected == actual)