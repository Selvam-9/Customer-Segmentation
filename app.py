import streamlit as st
import numpy as np
import pandas as pd
import logging
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page configuration
st.set_page_config(
    page_title="Customer Segment Finder",
    page_icon="🛍️",
    layout="centered"
)

# App title and description
st.title("Mall Customer Segmentation Tool")
st.write("Determine which customer group an individual belongs to based on their profile.")
st.write("---")

logging.info("Streamlit Clustering app started.")

# Create main content
st.subheader("Enter Customer Details")

# Create form inputs in columns
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Select Gender", "Male", "Female"]
    )
    if gender == "Select Gender":
        gender = ""
    
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25
    )

with col2:
    annual_income = st.number_input(
        "Annual Income (k$)",
        min_value=1,
        max_value=200,
        value=50
    )
    
    spending_score = st.number_input(
        "Spending Score (1-100)",
        min_value=1,
        max_value=100,
        value=50
    )

st.write("---")

# Clustering button
if st.button("Find Customer Segment", use_container_width=True):
    # Validate inputs
    if not gender:
        st.error("Please select a Gender!")
    else:
        try:
            # Create custom data object (Matches your updated CustomData class)
            data = CustomData(
                gender=gender,
                age=int(age),
                annual_income=int(annual_income),
                spending_score=int(spending_score)
            )
            
            # Get data as dataframe
            pred_df = data.get_data_as_data_frame()
            
            # Make prediction (Cluster ID)
            predict_pipeline = PredictPipeline()
            result = predict_pipeline.predict(pred_df)
            
            # Result mapping (Optional: give names to your clusters after analyzing them)
            cluster_id = int(result[0])
            
            # Display result
            st.success(f"Analysis Complete!")
            st.markdown(f"### This customer belongs to **Segment #{cluster_id}**")
            
            # Industry Standard: Add context to the result
            st.info("💡 *Tip: Use this Segment ID to target specific marketing campaigns or loyalty offers.*")
            
            # Display input summary
            with st.expander("View Customer Profile Summary"):
                summary_data = {
                    "Gender": gender,
                    "Age": age,
                    "Annual Income (k$)": annual_income,
                    "Spending Score (1-100)": spending_score
                }
                st.json(summary_data)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")        
            logging.error(f"Error during Streamlit prediction: {str(e)}")
