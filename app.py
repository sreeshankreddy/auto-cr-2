import streamlit as st
import os

# Set page config
st.set_page_config(page_title="AI Code Reviewer", page_icon="🔍", layout="wide")

# Initialize session state for mock users
if "registered_users" not in st.session_state:
    st.session_state.registered_users = {"admin": "password123"}
if "user" not in st.session_state:
    st.session_state.user = None

def login_page():
    st.title("Login / Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password", help="Password must contain both letters and numbers.")
    
    col_l, col_s = st.columns(2)
    with col_l:
        login_btn = st.button("Login")
    with col_s:
        signup_btn = st.button("Sign Up")
        
    if login_btn:
        # Check credentials
        if username in st.session_state.registered_users and st.session_state.registered_users[username] == password:
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid username or password.")
            
    if signup_btn:
        # Basic validation
        if not username or not password:
            st.error("Username and password required.")
        elif not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            st.error("Password must contain both letters and numbers.")
        elif username in st.session_state.registered_users:
            st.error("Username already exists.")
        else:
            st.session_state.registered_users[username] = password
            st.success("Account created! Please login.")

def main_app():
    st.sidebar.title("AI Code Reviewer")
    st.sidebar.success(f"Logged in as {st.session_state.user}")
    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.rerun()
        
    app_mode = st.sidebar.selectbox("Choose the mode", ["Review", "History", "Profile"])

    st.title("🔍 Automated Code Reviewer")

    input_method = st.radio("Select input method:", ["Paste Code", "Upload File", "GitHub Repository"])

    if input_method == "Paste Code":
        code = st.text_area("Paste your code here:", height=300)
        language = st.selectbox("Select language:", ["Python", "Java", "JavaScript", "C", "C++", "SQL", "Go"])
    elif input_method == "Upload File":
        uploaded_file = st.file_uploader("Upload a file:", type=["py", "java", "js", "c", "cpp", "sql", "go"])
        language = st.selectbox("Select language:", ["Python", "Java", "JavaScript", "C", "C++", "SQL", "Go"])
    else:
        repo_url = st.text_input("Enter GitHub repository URL:")
        branch = st.text_input("Enter branch (default: main):", "main")

    review_button = st.button("Start Review")

    if review_button:
        with st.spinner("Analyzing code..."):
            # Placeholder for backend logic
            st.progress(0)
            # Call reviewer logic here
            st.progress(100)
        
        st.success("Review Complete!")
        
        # Results display
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Code Quality Score", "85/100")
        with col2:
            st.metric("Security Score", "92/100")
            
        with st.expander("Issues Found"):
            st.write("1. Potential SQL Injection at line 42.")
            st.write("2. Unused variable 'temp' at line 12.")
            
        st.subheader("Refactored Code")
        st.code("# Improved code would be displayed here", language="python")
        
        st.download_button("Download PDF Report", data="Report content placeholder", file_name="report.pdf")

if st.session_state.user is None:
    login_page()
else:
    main_app()
