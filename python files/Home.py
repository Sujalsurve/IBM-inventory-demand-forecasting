import streamlit as st
import pandas as pd
import management as mg
import forecast as fc

def load_credentials(file_path):
    df = pd.read_csv(file_path)
    credentials = {row['username']: row['password'] for _, row in df.iterrows()}
    return credentials

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'page' not in st.session_state:
        st.session_state.page = 'login'

    if st.session_state.page == 'login':
        login_page()
    elif st.session_state.page == 'main':
        show_main_page()
    elif st.session_state.page == 'inventory':
        mg.show_inventory_page()
    elif st.session_state.page == 'view_items':
        mg.show_items()
    elif st.session_state.page == 'rfid':
        mg.show_recent_arrivals()
    elif st.session_state.page == 'forecast':
        fc.show_forecast_page()

def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        credentials = load_credentials('passwords.csv')
        if username in credentials and credentials[username] == password:
            st.session_state.logged_in = True
            st.session_state.page = 'main'
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error("Incorrect username or password")

def show_main_page():
    username = st.session_state.get('username', 'User')
    st.subheader(f"Hi {username},")
    st.subheader("Welcome to your Inventory Management System")
    col1, b, col2 = st.columns(3)
    with col1:
        if st.button("Manage Inventory"):
            st.session_state.page = 'inventory'
            st.experimental_rerun()
        st.write("Click here to track \n your inventory and update it")
    with col2:
        if st.button("Demand forecast"):
            st.session_state.page = 'forecast'
            st.experimental_rerun()
        st.write("Click here to avail historical \n data and forecast future demand")

if __name__ == "__main__":
    main()
