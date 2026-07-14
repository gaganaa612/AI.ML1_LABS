def generate_pins():
    valid_pins = []

    even_digits = [0, 2, 4, 6, 8]


    for d1 in even_digits:
        for d2 in even_digits:
            for d3 in even_digits:
                for d4 in even_digits:

                    if d1 + d2 + d3 + d4 == 16:
                        # Format as a 4-digit string (e.g., "0268")
                        pin = f"{d1}{d2}{d3}{d4}"
                        valid_pins.append(pin)

    return valid_pins



matching_pins = generate_pins()

print(f"Total matching PINs found: {len(matching_pins)}")
print("---")
print("The valid PINs are:")

for i in range(0, len(matching_pins), 5):
    print(", ".join(matching_pins[i:i + 5]))
