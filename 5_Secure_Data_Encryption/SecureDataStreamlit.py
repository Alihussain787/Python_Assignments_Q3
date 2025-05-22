import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate and initialize cipher key (should be consistent in real use)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory data store and state
stored_data = {}  # {encrypted_text: {"encrypted_text": str, "passkey": str}}
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

# Hashing function
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    entry = stored_data.get(encrypted_text)
    if entry and entry["passkey"] == hashed:
        st.session_state.failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    else:
        st.session_state.failed_attempts += 1
        return None

# Streamlit UI
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Securely **store** and **retrieve** your confidential data using **passkey encryption**.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            st.success("✅ Data encrypted and stored successfully!")
            st.code(encrypted_text, language="text")
        else:
            st.error("⚠️ Please enter both data and passkey.")

elif choice == "Retrieve Data":
    if st.session_state.failed_attempts >= 3 and not st.session_state.is_authenticated:
        st.warning("🔒 Too many failed attempts! Redirecting to Login Page...")
        st.experimental_rerun()

    st.subheader("🔍 Retrieve Data")
    encrypted_input = st.text_area("Enter Encrypted Data:")
    passkey_input = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey_input:
            result = decrypt_data(encrypted_input, passkey_input)
            if result:
                st.success(f"✅ Decrypted Data: {result}")
            else:
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {remaining}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page...")
                    st.experimental_rerun()
        else:
            st.error("⚠️ All fields are required.")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_input = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_input == "admin123":  # Hardcoded master password for demo
            st.session_state.failed_attempts = 0
            st.session_state.is_authenticated = True
            st.success("✅ Reauthorized successfully! Return to Retrieve Data.")
        else:
            st.error("❌ Incorrect master password!")
