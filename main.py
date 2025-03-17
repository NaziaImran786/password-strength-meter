import streamlit as st
import re
import random

# Define special characters
SPECIAL_CHARACTERS = "!@#$%^&*"

# Streamlit page config
st.set_page_config(page_title="Password Strength Meter", page_icon="🔑", layout="centered")

# Function to check password strength
def check_password_strength(password: str) -> tuple[int, str]:
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Make your password at least 8 characters long.")

    # Check uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Include both uppercase and lowercase letters.")

    # Check digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔸 Add at least one number (0-9).")

    # Check special character
    if re.search(rf"[{re.escape(SPECIAL_CHARACTERS)}]", password):
        score += 1
    else:
        feedback.append(f"🔸 Include at least one special character ({SPECIAL_CHARACTERS}).")

    # Avoid common weak passwords
    common_passwords = ["password", "123456", "qwerty", "password123"]
    if password.lower() in common_passwords:
        return 1, "❌ Your password is too common! Choose a more unique password."

    # Assign strength levels
    if score == 4:
        return 5, "✅ **Strong password!** Your password meets all security criteria."
    elif score == 3:
        return 4, "⚠️ **Moderate password.** Try adding more complexity for better security."
    else:
        return score, "❌ **Weak password.** " + " ".join(feedback)

# Function to generate a strong password
def generate_strong_password(length: int = 12) -> str:
    if length < 8:
        length = 8  # Ensure minimum length

    upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower = random.choice("abcdefghijklmnopqrstuvwxyz")
    digit = random.choice("0123456789")
    special = random.choice(SPECIAL_CHARACTERS)
    remaining = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" + SPECIAL_CHARACTERS, k=length-4))

    password = upper + lower + digit + special + remaining
    return ''.join(random.sample(password, len(password)))  # Shuffle password

# Streamlit UI
def main():
    st.markdown(
        """
        <style>
        .main {
            background-color: #f7f7f7;
        }
        .stTextInput, .stButton>button {
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("🔑 Password Strength Meter")
    st.write("Check your password strength and get suggestions for improvement!")

    # Input field
    password = st.text_input("Enter a password to check strength", type="password")

    # Check password strength
    if password:
        score, message = check_password_strength(password)

        # Show strength message
        if score == 5:
            st.success(message)
        elif score >= 3:
            st.warning(message)
        else:
            st.error(message)

    # Generate strong password
    st.divider()
    st.subheader("🔧 Need Help Creating a Strong Password?")
    length = st.slider("Choose password length", min_value=8, max_value=32, value=12)
    
    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password(length)
        st.text_input("Suggested Strong Password", value=strong_password, disabled=True)

    # Footer
    st.divider()
    st.markdown("🔒 **Stay safe online — use strong, unique passwords for every account!**")

if __name__ == "__main__":
    main()