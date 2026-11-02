"""Branch coverage tests for food_delivery.py - PES1UG24CS508
Each test targets one specific True/False outcome of a decision,
using boundary values."""
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time


# --- Line 5: distance_km <= 0 or distance_km > 15 ---
@pytest.mark.parametrize("d", [0, -1, -0.5, 15.01, 100])
def test_range_rejected(d):
    with pytest.raises(ValueError):
        delivery_charge(d, 100, False)


@pytest.mark.parametrize("d", [0.1, 15])
def test_range_accepted_boundaries(d):
    assert delivery_charge(d, 100, False) in (20, 60)


# --- Line 7: order_value >= 500 (True / False at boundary) ---
def test_order_value_exactly_500_free():
    assert delivery_charge(1, 500, False) == 0


def test_order_value_499_charged():
    assert delivery_charge(1, 499.99, False) == 20


# --- Line 9: distance <= 3 ; Line 11: distance <= 8 ---
@pytest.mark.parametrize("d,expected", [(3, 20), (3.01, 40), (8, 40), (8.01, 60)])
def test_distance_slab_boundaries(d, expected):
    assert delivery_charge(d, 100, False) == expected


# --- Line 15: is_raining True / False ---
@pytest.mark.parametrize("rain,expected", [(True, 70), (False, 40)])
def test_rain_branch(rain, expected):
    assert delivery_charge(5, 100, rain) == expected


# --- apply_coupon: line 21 ---
def test_coupon_code_none_branch():
    assert apply_coupon(1000, None, True) == 1000


def test_coupon_code_not_none_branch():
    assert apply_coupon(1000, "SAVE50", True) == 950


# --- line 23: code not in COUPONS ---
def test_coupon_unknown_code_raises():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(500, "", True)


def test_coupon_known_code_passes():
    assert apply_coupon(500, "SAVE50", False) == 450


# --- line 25: code == WELCOME and not is_first_order (all combinations) ---
def test_welcome_first_order_ok():
    assert apply_coupon(500, "WELCOME", True) == 400


def test_welcome_repeat_order_rejected():
    with pytest.raises(ValueError, match="first order"):
        apply_coupon(500, "WELCOME", False)


def test_save50_repeat_order_ok():  # code != WELCOME short-circuit
    assert apply_coupon(500, "SAVE50", False) == 450


# --- line 27: order_value < 200 boundaries ---
def test_coupon_order_199_not_applied():
    assert apply_coupon(199, "SAVE50", True) == 199


def test_coupon_order_exactly_200_applied():
    assert apply_coupon(200, "SAVE50", True) == 150


# --- estimated_time: lines 34, 36, 38 all combinations ---
@pytest.mark.parametrize("peak,busy,expected", [
    (False, False, 15),
    (True, False, 25),
    (False, True, 30),
    (True, True, 45),
])
def test_time_all_flag_combinations(peak, busy, expected):
    assert estimated_time(0, peak, busy) == expected


def test_time_scales_with_distance():
    assert estimated_time(10, False, False) == 55
