import streamlit as st
import os

# Set page config
st.set_page_config(page_title="AI Code Reviewer", page_icon="🔍", layout="wide")

# Sidebar
st.sidebar.title("AI Code Reviewer")
app_mode = st.sidebar.selectbox("Choose the mode", ["Review", "History", "Profile"])

# Login/Register Placeholder
if "user" not in st.session_state:
    st.sidebar.warning("Please Login")
    # Add simple login form placeholder
else:
    st.sidebar.success(f"Logged in as {st.session_state.user}")

# Main page
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
