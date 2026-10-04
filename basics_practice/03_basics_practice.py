def check_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(not c.isalnum() for c in pw):
        score += 1
    return score

levels = {0: "Very Weak", 1: "Weak", 2: "Okay", 3: "Strong", 4: "Very Strong"}

pw = input("Enter password: ")
print("Strength:", levels[check_strength(pw)])
