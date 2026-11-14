# Q2 - OTP verification: blank entries do not count as attempts

CORRECT_OTP = "4821"

def verify_while():
    attempts = 0
    while attempts < 3:
        otp = input("Enter OTP: ").strip()
        if otp == "":
            print("Blank entry: attempt not counted.")
            continue
        attempts += 1
        if otp == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Wrong OTP.")
    else:
        print("Account locked for 30 minutes.")

def verify_for():
    # The outer for-loop represents the three counted attempts.
    for attempt in range(3):
        while True:
            otp = input("Enter OTP: ").strip()
            if otp == "":
                print("Blank entry: attempt not counted.")
                continue
            break
        if otp == CORRECT_OTP:
            print("OTP verified.")
            break
        print("Wrong OTP.")
    else:
        print("Account locked for 30 minutes.")

# A correct security answer increases the allowed wrong attempts to five.
def verify_with_security(otp_values, security_answer_correct):
    limit = 5 if security_answer_correct else 3
    attempts = 0
    for otp in otp_values:
        if attempts >= limit:
            break
        if otp.strip() == "":
            continue
        attempts += 1
        if otp.strip() == CORRECT_OTP:
            return "OTP verified"
    if attempts == limit:
        return "Account locked for 30 minutes"
    return "Verification not completed"

print("WHILE LOOP")
verify_while()

print("FOR LOOP")
verify_for()

print("SECURITY QUESTION TEST")
print(verify_with_security(["", "1111", "2222", "3333", "4444", "5555"], True))
