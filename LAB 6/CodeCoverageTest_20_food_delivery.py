"""Code (line) coverage tests for food_delivery.py - PES1UG24CS508"""
import pytest
from food_delivery import delivery_charge, apply_coupon, estimated_time, COUPONS


# ---------- delivery_charge ----------
def test_charge_invalid_zero_distance():
    with pytest.raises(ValueError, match="out of delivery range"):
        delivery_charge(0, 100, False)


def test_charge_invalid_too_far():
    with pytest.raises(ValueError):
        delivery_charge(16, 100, False)


def test_charge_free_delivery_large_order():
    assert delivery_charge(5, 800, False) == 0


def test_charge_short_distance():
    assert delivery_charge(2, 200, False) == 20


def test_charge_medium_distance():
    assert delivery_charge(6, 200, False) == 40


def test_charge_long_distance():
    assert delivery_charge(12, 200, False) == 60


def test_charge_rain_surcharge():
    assert delivery_charge(2, 200, True) == 50


def test_charge_free_but_raining():
    assert delivery_charge(10, 600, True) == 30


# ---------- apply_coupon ----------
def test_coupon_none():
    assert apply_coupon(300, None, True) == 300


def test_coupon_invalid_code():
    with pytest.raises(ValueError, match="invalid coupon"):
        apply_coupon(300, "FAKE", True)


def test_coupon_welcome_not_first_order():
    with pytest.raises(ValueError, match="first order"):
        apply_coupon(300, "WELCOME", False)


def test_coupon_below_minimum_order():
    assert apply_coupon(150, "SAVE50", False) == 150


def test_coupon_save50_applied():
    assert apply_coupon(300, "SAVE50", False) == 250


def test_coupon_welcome_applied_first_order():
    assert apply_coupon(400, "WELCOME", True) == 300


# ---------- estimated_time ----------
def test_time_basic():
    assert estimated_time(5, False, False) == 35


def test_time_peak_only():
    assert estimated_time(5, True, False) == 45


def test_time_busy_only():
    assert estimated_time(5, False, True) == 50


def test_time_peak_and_busy():
    assert estimated_time(5, True, True) == 65


def test_coupons_constant():
    assert COUPONS == {"SAVE50": 50, "WELCOME": 100}
