import streamlit as st
from PIL import Image

def show_forecast_page():
    st.set_page_config(
        page_title="Inventory Management",
        page_icon=":chart:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Load images
    image1 = Image.open(r"C:\Users\DELL\Desktop\Inventory--management-system-using-machine-learning--main\Python_files\Top 20 spare parts.JPG")
    image2 = Image.open(r"C:\Users\DELL\Desktop\Inventory--management-system-using-machine-learning--main\Python_files\top 50 spare parts copy.JPG")
    image3 = Image.open(r"C:\Users\DELL\Desktop\Inventory--management-system-using-machine-learning--main\Python_files\spare parts demand per week.JPG")
    image4 = Image.open(r"C:\Users\DELL\Desktop\Inventory--management-system-using-machine-learning--main\Python_files\weekly demand Forecast.JPG")
    image5 = Image.open(r"C:\Users\DELL\Desktop\Inventory--management-system-using-machine-learning--main\Python_files\weekly demand of spare parts.JPG")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #007bff'>TOP 20 Best Selling Parts</h2>", unsafe_allow_html=True)
        button1 = st.button("Click to view", key='btn1')
    with col2:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #ff69b4'>TOP 50 Best Selling Parts</h2>", unsafe_allow_html=True)
        button2 = st.button("Click to view", key='btn2')
    with col3:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #33cc33'>Sales Forecasting</h2>", unsafe_allow_html=True)
        button3 = st.button("Click to view", key='btn3')
    with col4:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #ff9900'>Weekly demands</h2>", unsafe_allow_html=True)
        button4 = st.button("Click to view", key='btn4')

    if button1:
        st.title("TOP 20 Best Selling Parts")
        st.image(image1, use_column_width=True)
        st.text("Filter-Oil: With nearly 3500 occurrences, this spare part dominates the list...")

    elif button2:
        st.title("TOP 50 Best Selling Parts")
        st.image(image2, use_column_width=True)
        st.text("This bar graph provides a detailed breakdown of demand for the top 50 spare parts...")

    elif button3:
        st.title("Sales Forecasting")
        st.image(image3, use_column_width=True)
        st.text("This line graph illustrates the weekly demand for spare parts over an extended period...")

    elif button4:
        st.title("Weekly demands")
        st.image(image4, use_column_width=True)
        st.image(image5, use_column_width=True)
        st.text("The two graphs, \"Spare Parts Demand per Week\" and \"Weekly Demand Forecast,\" provide complementary insights...")

    st.text("Demand Forecasting Project Report\nIntroduction")
    st.text("In this project, we developed a machine learning model to forecast the demand for spare parts...")
    st.text("Methodology\nWe collected and preprocessed historical sales data...")
    st.text("Results\nOur model achieved the following performance metrics:\n"
            "Mean Absolute Error (MAE): 86.97\nRoot Mean Squared Error (RMSE): 103.46\n"
            "Accuracy: 76.73%\nPrecision: 76.73%")
    st.text("Discussion\nIn the context of demand forecasting, an accuracy rate above 70% is generally considered good...")
    st.text("Conclusion\nThe project successfully developed a demand forecasting model with an accuracy of 76.73%...")
    st.text("Recommendations\nModel Enhancement: Continue to refine the model to further improve accuracy...\n"
            "Feature Integration: Consider adding external factors...")

    if st.sidebar.button("Back to Home"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    show_forecast_page()
