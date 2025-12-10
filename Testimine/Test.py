"""Tests for solution."""

from solution import students_study, lottery, fruit_order

"""Tests for students_study."""


def test__students_study__night_any_coffee__no_studying():
    """At night (1–4) students do not study regardless of coffee."""
    for hour in [1, 2, 3, 4]:
        assert students_study(hour, True) is False
        assert students_study(hour, False) is False


def test__students_study__day_with_and_without_coffee():
    """Between 5–17, study only if coffee_needed is True."""
    for hour in [5, 10, 17]:
        assert students_study(hour, True) is True
        assert students_study(hour, False) is False


def test__students_study__evening_any_coffee__always_study():
    """Between 18–24, always study regardless of coffee."""
    for hour in [18, 20, 24]:
        assert students_study(hour, True) is True
        assert students_study(hour, False) is True


"""Tests for lottery."""


def test__lottery__all_fives():
    """Tests the case where all three numbers are 5, resulting in a score of 10."""
    assert lottery(5, 5, 5) == 10


def test_all_same_not_five():
    """Tests the case where all three numbers are the same but not 5, resulting in a score of 5."""
    assert lottery(3, 3, 3) == 5


def test_both_diff_from_a():
    """Tests the case where all three numbers are different, resulting in a score of 1."""
    assert lottery(2, 3, 4) == 1


def test_one_same_as_a():
    """Tests the case where only one other number is the same as the first, resulting in a score of 0."""
    assert lottery(2, 2, 3) == 0
    assert lottery(7, 3, 7) == 0


def test__lottery__all_same_negative():
    """Tests the case where all three numbers are the same negative value."""
    assert lottery(-1, -1, -1) == 5


def test__lottery__all_same_zero():
    """Tests the case where all three numbers are zero."""
    assert lottery(0, 0, 0) == 5


def test__lottery__b_c_same_a_diff():
    """Tests the case where b and c are the same, but different from a."""
    assert lottery(1, 2, 2) == 1


"""Tests for fruit_order."""


def test__fruit_order__all_zero():
    """Tests ordering 0 amount when all fruit counts are 0."""
    assert fruit_order(0, 0, 0) == 0


def test__fruit_order__zero_amount_zero_small():
    """Tests ordering 0 amount when small count is 0 and big count is non-zero."""
    assert fruit_order(0, 2, 0) == 0


def test__fruit_order__zero_amount_zero_big():
    """Tests ordering 0 amount when big count is 0 and small count is non-zero."""
    assert fruit_order(2, 0, 0) == 0


def test__fruit_order__zero_amount_others_not_zero():
    """Tests ordering 0 amount when both small and big counts are non-zero."""
    assert fruit_order(2, 2, 0) == 0


def test__fruit_order__only_big_exact_match():
    """Tests case where only big fruits are available and match exactly."""
    assert fruit_order(0, 3, 15) == 0


def test__fruit_order__only_big_not_enough_but_multiple_of_5():
    """Tests case where only big fruits are available and not enough, but amount is a multiple of 5."""
    assert fruit_order(0, 2, 15) == -1


def test__fruit_order__only_big_not_enough():
    """Tests case where only big fruits are available and not enough."""
    assert fruit_order(0, 2, 12) == -1


def test__fruit_order__only_big_more_than_required_match():
    """Tests case where more big fruits are available than needed for an exact match."""
    assert fruit_order(0, 5, 15) == 0


def test__fruit_order__only_big_more_than_required_no_match():
    """Tests case where more big fruits are available, but amount cannot be exactly matched."""
    assert fruit_order(0, 5, 13) == -1


def test__fruit_order__only_small_match_more_than_5_smalls():
    """Tests case where only small fruits are available and count is greater than 5."""
    assert fruit_order(7, 0, 7) == 7


def test__fruit_order__only_small_not_enough_more_than_5_smalls():
    """Tests case where only small fruits are available and not enough, with count greater than 5."""
    assert fruit_order(6, 0, 7) == -1


def test__fruit_order__only_small_not_enough():
    """Tests case where only small fruits are available and not enough."""
    assert fruit_order(3, 0, 5) == -1


def test__fruit_order__only_small_more_than_required():
    """Tests case where more small fruits are available than needed."""
    assert fruit_order(10, 0, 7) == 7


def test__fruit_order__match_with_more_than_5_smalls():
    """Tests a successful match using both types, with a high small count."""
    assert fruit_order(7, 2, 12) == 2


def test__fruit_order__all_positive_exact_match():
    """Tests a basic exact match using both types."""
    assert fruit_order(4, 1, 9) == 4


def test__fruit_order__use_all_smalls_some_bigs():
    """Tests a successful match requiring all available small fruits."""
    assert fruit_order(4, 3, 14) == 4


def test__fruit_order__use_some_smalls_all_bigs():
    """Tests a successful match requiring all available big fruits."""
    assert fruit_order(4, 2, 12) == 2


def test__fruit_order__use_some_smalls_some_bigs():
    """Tests a successful match using a portion of both small and big fruits."""
    assert fruit_order(10, 3, 13) == 3


def test__fruit_order__not_enough():
    """Tests the impossible case where there are not enough fruits overall."""
    assert fruit_order(3, 1, 10) == -1


def test__fruit_order__enough_bigs_not_enough_smalls():
    """Tests the impossible case where there are enough big fruits for the 5-multiple, but not enough small fruits for the remainder."""
    assert fruit_order(2, 3, 18) == -1


def test__fruit_order__not_enough_with_more_than_5_smalls():
    """Tests the impossible case with a high small count and insufficient total amount."""
    assert fruit_order(6, 1, 12) == -1


def test__fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Tests an impossible case with large numbers, insufficient small fruits for the remainder."""
    assert fruit_order(1, 300, 1257) == -1


def test__fruit_order__match_large_numbers():
    """Tests a successful match with large numbers."""
    assert fruit_order(200, 200, 1200) == 200