import re
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Password Strength Meter | Hamza Rehmani",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
        .title {
            font-size: 28px;
            font-weight: bold;
            color: #222;
            text-align: center;
        }
        .subtitle {
            font-size: 16px;
            color: #555;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-container {
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            width: 100%;
            max-width: 350px;
            margin: auto;
        }
        input[type="password"] {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border-radius: 8px;
            border: 1px solid #ccc;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .eye-icon {
            position: absolute;
            right: 10px;
            cursor: pointer;
            font-size: 20px;
            color: #555;
        }
        div[data-testid="stButton"] {
            display: flex;
            justify-content: center;
        }
        div[data-testid="stButton"] button {
            width: 200px;
            background: linear-gradient(135deg, #ff6a00, #ee0979);
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 12px;
            border: none;
            text-align: center;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);
        }
        div[data-testid="stButton"] button:hover {
            background: linear-gradient(135deg, #ee0979, #ff6a00);
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>🔑 Password Strength Meter</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter a password to analyze its security level.</div>", unsafe_allow_html=True)

# Password input field
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔒")

# Password strength function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use **both uppercase and lowercase letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add **at least one special character (!@#$%^&*)**.")

    if score == 4:
        st.success("✔️ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Try adding more elements for better security.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to improve it.")

    if feedback:
        with st.expander("💡 **How to Improve Your Password?**"):
            for item in feedback:
                st.write(item)

# Button to check strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
