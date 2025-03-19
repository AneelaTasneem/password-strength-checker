import re
import random
import string
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase & lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one digit (0-9).")

    # Special character check
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Common password blacklist
    common_passwords = ["password123", "123456", "qwerty", "admin", "letmein"]
    if password in common_passwords:
        feedback.append("Avoid common passwords like 'password123' or 'qwerty'.")
        score = 1  # Force it to weak

    # Assigning strength level
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

def generate_strong_password(length=12):
    """Generates a strong random password"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.title("🔐 Password Strength Checker")

# User input
password = st.text_input("Enter a password:", type="password")

if st.button("Check Strength"):
    if password:
        strength, suggestions = check_password_strength(password)
        st.write(f"**Password Strength:** {strength}")
        
        if suggestions:
            st.warning("🔹 Suggestions to improve:")
            for tip in suggestions:
                st.write(f"- {tip}")
            
            # Suggest a strong password
            st.write("💡 Suggested Strong Password:")
            st.code(generate_strong_password())
        else:
            st.success("✅ Your password is strong!")
    else:
        st.error("Please enter a password to check.")
