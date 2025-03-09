import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    length = len(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    types = sum([has_uppercase, has_lowercase, has_digit, has_special])

    if length < 8:
        return "Very Weak"
    elif length < 12:
        if types == 1:
            return "Weak"
        elif types == 2:
            return "Medium"
        else:
            return "Strong"
    else:
        if types == 1:
            return "Medium"
        elif types == 2:
            return "Strong"
        else:
            return "Very Strong"


st.set_page_config(page_title="Password Tool", page_icon="🔐")
st.title("Password Generator and Strength Checker")

col1, col2 = st.columns(2)

with col1:
    st.header("Password Generator")
    length = st.slider("Password Length", min_value=8, max_value=32, value=12)
    use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
    use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
    use_numbers = st.checkbox("Include Numbers", value=True)
    use_special = st.checkbox("Include Special Characters", value=True)

    if st.button("Generate Password"):
        password = generate_password(
            length, use_uppercase, use_lowercase, use_numbers, use_special
        )
        st.code(password)
        st.markdown(
            """
            <button onclick="navigator.clipboard.writeText('{}')">Copy to Clipboard</button>
        """.format(
                password
            ),
            unsafe_allow_html=True,
        )
    st.write(
        "Tip: Use a mix of character types and longer length for stronger passwords."
    )

with col2:
    st.header("Password Strength Checker")
    password_input = st.text_input("Enter Password", type="password")

    if st.button("Check Strength"):
        if password_input:
            strength = check_password_strength(password_input)
            if strength == "Very Weak":
                st.error(f"Password Strength: {strength}")
            elif strength == "Weak":
                st.warning(f"Password Strength: {strength}")
            elif strength == "Medium":
                st.info(f"Password Strength: {strength}")
            else:
                st.success(f"Password Strength: {strength}")
        else:
            st.warning("Please enter a password.")
    st.write("Tip: Strong passwords are 12+ characters with multiple character types.")
