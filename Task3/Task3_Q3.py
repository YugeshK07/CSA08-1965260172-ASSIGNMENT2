# Q3 - Vehicle registration number validator

def normalise(text):
    # Remove spaces and hyphens, then convert to uppercase.
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    # Valid form: 2 letters, 2 digits, 1 or 2 letters, 4 digits.
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha() or not reg[2:4].isdigit():
        return False
    if len(reg) == 9:
        return reg[4:5].isalpha() and reg[5:9].isdigit()
    return reg[4:6].isalpha() and reg[6:10].isdigit()

def receipt_format(reg):
    if not is_valid(reg):
        return "INVALID"
    series_end = 5 if len(reg) == 9 else 6
    return reg[0:2] + " " + reg[2:4] + " " + reg[4:series_end] + " " + reg[series_end:]

samples = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234",
           "TN 22 1234 AB", "MH 12 DE 1234", "TN-09-AB-123"]
for raw in samples:
    reg = normalise(raw)
    print(f"{raw} -> {reg}:",
          "valid" if is_valid(reg) else "INVALID",
          receipt_format(reg))
