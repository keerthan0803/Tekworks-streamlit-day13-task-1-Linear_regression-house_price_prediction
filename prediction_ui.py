import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("House Price Prediction")
st.write("Enter the details of the house to predict its price.")

# Create a form
with st.form("prediction_form"):
    st.write("### House Features")
    
    # OverallQual: Rates the overall material and finish of the house (1-10)
    overall_qual = st.number_input("Overall Quality (1-10)", min_value=1, max_value=10, value=5, help="Rates the overall material and finish of the house")
    
    # GrLivArea: Above grade (ground) living area square feet
    gr_liv_area = st.number_input("Above Grade Living Area (sq ft)", min_value=300, max_value=10000, value=1500, help="Above grade living area in square feet")
    
    # GarageCars: Size of garage in car capacity
    garage_cars = st.number_input("Garage Size (number of cars)", min_value=0, max_value=5, value=2, help="Size of garage in car capacity")
    
    # TotalBsmtSF: Total square feet of basement area
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=6000, value=1000, help="Total square feet of basement area")
    
    # YearBuilt: Original construction date
    year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2000, help="Original construction date")
    
    # Neighborhood: Encoded value (0-24 based on label encoding)
    neighborhood = st.number_input("Neighborhood (encoded 0-24)", min_value=0, max_value=24, value=5, help="Neighborhood code (label encoded)")
    
    # LotArea: Lot size in square feet
    lot_area = st.number_input("Lot Area (sq ft)", min_value=1000, max_value=50000, value=8450, help="Lot size in square feet")
    
    # KitchenQual: Kitchen quality (TA=0, Gd=1, Ex=2, Fa=3)
    kitchen_qual_options = {"TA (Typical/Average)": 0, "Gd (Good)": 1, "Ex (Excellent)": 2, "Fa (Fair)": 3}
    kitchen_qual_selection = st.selectbox("Kitchen Quality", options=list(kitchen_qual_options.keys()))
    kitchen_qual = kitchen_qual_options[kitchen_qual_selection]
    
    # Submit button
    submit_button = st.form_submit_button("Predict House Price")
    
    if submit_button:
        # Prepare input data in the same order as training data
        # Order: OverallQual, GrLivArea, GarageCars, TotalBsmtSF, YearBuilt, Neighborhood, LotArea, KitchenQual
        input_data = pd.DataFrame({
            'OverallQual': [overall_qual],
            'GrLivArea': [gr_liv_area],
            'GarageCars': [garage_cars],
            'TotalBsmtSF': [total_bsmt_sf],
            'YearBuilt': [year_built],
            'Neighborhood': [neighborhood],
            'LotArea': [lot_area],
            'KitchenQual': [kitchen_qual]
        })
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display result
        st.success(f"### Predicted House Price: ${prediction[0]:,.2f}")
        st.balloons()
    