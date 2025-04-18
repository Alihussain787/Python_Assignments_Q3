import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "success", feedback
    elif score == 3:
        return "⚠️ Moderate Password", "warning", feedback
    else:
        return "❌ Weak Password", "error", feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.markdown("Enter your password to check its security level.")

password = st.text_input("Enter Password:", type="password")

if password:
    strength, alert_type, feedback = check_password_strength(password)
    st.markdown(f"### {strength}", unsafe_allow_html=True)
    for msg in feedback:
        st.write(msg)

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"Suggested Strong Password: `{strong_password}`")
