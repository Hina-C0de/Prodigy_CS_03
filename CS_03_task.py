import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 6:
        strength += 1
    else:
        feedback.append("Password should be at least 6 characters long.")
    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&* etc.).")
    
    if strength == 5:
        return "Strong password!", feedback
    elif strength >= 3:
        return "Moderate password.", feedback
    else:
        return "Weak password!", feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    for suggestion in feedback:
        print(f"- {suggestion}")
