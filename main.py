password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

missing = []

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True


if len(password) < 8:
    missing.append("Minimum 8 characters")

if not has_upper:
    missing.append("Uppercase letter")

if not has_lower:
    missing.append("Lowercase letter")

if not has_digit:
    missing.append("Number")

if not has_special:
    missing.append("Special character")

# Final result
if len(missing) == 0:
    print("Strong Password ")
elif len(missing) <= 2:
    print("Medium Password ")
    print("Missing:", ", ".join(missing))
else:
    print("Weak Password ")
    print("Missing:", ", ".join(missing))