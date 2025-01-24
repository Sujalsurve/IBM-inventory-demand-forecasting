import streamlit as st
import pandas as pd
import time



def load_data(file):
    try:
        df = pd.read_csv(file)

        df.columns = df.columns.str.strip()
    except Exception as e:
        st.error(f"Error loading {file}: {e}")
        return pd.DataFrame(columns=['Product', 'Qty', 'Time'])
    return df


def show_items():
    st.title('Inventory Management System')
    st.subheader('Product List')
    st.write("Use the table below to view and edit the inventory:")


    df = load_data("inventory.csv")

    if df.empty:
        st.warning("No data found in inventory.csv")
    else:

        if 'Product' not in df.columns or 'Quantity' not in df.columns:
            st.error("Required columns ('Product', 'Quantity') are missing in inventory.csv")
            return


        edited_df = st.data_editor(df, use_container_width=True)


        if not edited_df.equals(df):
            edited_df.to_csv('inventory.csv', index=False)
            st.success('Changes saved to CSV file.')


    if st.sidebar.button("Back to Home"):
        st.session_state.page = 'main'


def show_recent_arrivals():
    st.title("Tracking Goods")


    data = load_data("rfid_data.csv")

    if data.empty:
        st.warning("No data found in rfid_data.csv")
    else:

        if 'Product' not in data.columns or 'Qty' not in data.columns or 'Time' not in data.columns:
            st.error("Required columns ('Product', 'Qty', 'Time') are missing in rfid_data.csv")
            return


        data_text = "\n".join([f"{row['Product']}, {row['Qty']}, {row['Time']}" for _, row in data.iterrows()])


        st.text_area("Recently arrived goods to the inventory", data_text, height=300)

        current_time = time.strftime('%Y-%m-%d %H:%M:%S')


        st.write(f"Last updated at {current_time}")


        print(f"Data refreshed at {current_time}")
        print(data)


    st.experimental_rerun()





def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'main'

    if st.session_state.page == 'view_items':
        show_items()
    elif st.session_state.page == 'rfid':
        show_recent_arrivals()
    else:
        show_inventory_page()


def show_inventory_page():
    st.title("Manage Inventory")


    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    st.write("Click here to view and edit the inventory manually")
    if st.button("View current Inventory"):
        st.session_state.page = 'view_items'

    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    st.write("Click here to view the recent arrivals to goods to your inventory")
    if st.button("Recent arrivals"):
        st.session_state.page = 'rfid'


    if st.sidebar.button("Back to Home"):
        st.session_state.page = 'main'


if __name__ == "__main__":
    main()
