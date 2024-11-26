import pandas as pd
import streamlit as st
import openpyxl

#Title
st.title("Standard Dunker Motor & Gearbox Configurator")

#Upload file
uploaded_file = st.file_uploader("Upload Dunker Synoptik Table", type =['xlsm','xlsx'])

if uploaded_file:
    try:
        #read the file
        motor_df = pd.read_excel(uploaded_file, sheet_name="Motor Type", engine="openpyxl")
        gearbox_df = pd.read_excel(uploaded_file, sheet_name="Gearboxes", engine="openpyxl")
        remark_table_df = pd.read_excel(uploaded_file, sheet_name="Remarks", engine="openpyxl")

        #Step 1 - Motor 
        st.subheader("Select Motor")
        motor_types = motor_df['Motor Type'].unique()
        selected_motor = st.selectbox("Select Motor", motor_types)

        if selected_motor:
            st.write(f'You selected Motor Type: {selected_motor}')

            #Show unique optiosn for the motor type
            motor_options = motor_df[motor_df['Motor Type'] == selected_motor]
            for col in motor_df.columns:
                if col != "Motor Type":
                    unique_value = motor_options[col].dropna().unique()
                    selected_value = st.selectbox("Select {col}", unique_value)
                    st.write(f"Selected {col}: {selected_value}")

        #Step 2: Gearbox
        st.subheader("Select Gearbox")

        #filter the gearbox 
        compatible_gearboxes = gearbox_df[gearbox_df["Motor Type"] == selected_motor]

        if not compatible_gearboxes.empty:
            for col in gearbox_df.columns:
                if col != "Motor Type":
                    unique_value = compatible_gearboxes[col].dropna().unique()
                    selected_value = st.selectbox(f"Select {col}", unique_value)
                    st.write(f"Selected {col}: {selected_value}")
        else:
            st.warning("No compatib;e gearboxes found for the selected motor")

        #Step 3: Remarks
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")       
else:
    st.info("Please upoad an Excel file")