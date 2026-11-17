from hypothesis import given, strategies as st
from food_delivery import parse_order, delivery_eta, coupon_discount

@given(st.text() | st.none())
def test_parse_order_no_crash(s):
    try:
        parse_order(s)
    except Exception as e:
        assert False, f"parse_order crashed with: {e!r}"

@given(st.text() | st.none())
def test_delivery_eta_no_crash(s):
    try:
        delivery_eta(s)
    except Exception as e:
        assert False, f"delivery_eta crashed with: {e!r}"

@given(st.text() | st.none())
def test_coupon_discount_no_crash(s):
    try:
        coupon_discount(s)
    except Exception as e:
        assert False, f"coupon_discount crashed with: {e!r}"