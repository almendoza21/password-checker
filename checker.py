import re

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 4:
        return "Strong 💪"
    elif score == 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

password = input("Enter a password to check: ")
print("Strength:", check_password_strength(password))
