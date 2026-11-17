import math

def parse_order(items_csv):
    order = {}
    if not isinstance(items_csv, str):
        return order
    for item in items_csv.split(','):
        item = item.strip()
        if not item or item.count(':') != 1:
            continue
        name, qty = item.split(':')
        name = name.strip()
        if not name:
            continue
        try:
            qty = int(qty.strip())
        except ValueError:
            continue
        if qty <= 0:
            continue
        order[name] = qty
    return order

def delivery_eta(distance_km):
    try:
        d = float(distance_km)
    except (TypeError, ValueError, OverflowError):
        return None
    if not math.isfinite(d) or d < 0:
        return None
    return int(15 + d * 4)

def coupon_discount(code):
    if not isinstance(code, str):
        return 0
    code = code.strip().upper()
    if not code.startswith('SAVE'):
        return 0
    digits = code[4:]
    if not (digits.isascii() and digits.isdigit()) or len(digits) > 3:
        return 0
    return min(int(digits), 100)

def main():
    print("==== Running parse_order ====")
    user_input = input("Enter items as name:qty CSV (e.g. pizza:2,burger:1): ")
    result = parse_order(user_input)
    print("Order:", result)

    print("\n==== Running delivery_eta ====")
    user_input = input("Enter distance in km (e.g. 4.5): ")
    result = delivery_eta(user_input)
    print("ETA in Minutes:", result if result is not None else "Invalid distance")

    print("\n==== Running coupon_discount ====")
    user_input = input("Enter a coupon code (e.g. SAVE50): ")
    result = coupon_discount(user_input)
    print("Discount:", result)

if __name__ == "__main__":
    main()