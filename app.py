
import numpy as np
import pickle
import streamlit as st
import joblib
from sklearn.ensemble import RandomForestClassifier

st.header("Claim risk Prediction web-app by  Sandeep")
# loading the saved model
loaded_model = joblib.load("xg.pkl")


# creating a function for Prediction

def claimrisk_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The policy is not going to claim'
    else:
      return 'The policy is going to be claimed'
  
    
  
def main():
    
    
    # giving a title
    st.title('Insurance policy claim risk predictor Web App')
    
    
    # getting the input data from the user
    
    
    PREMIUM_CHARGED = st.text_input('PREMIUM_CHARGED for the policy')
    NO_CLAIM_DISCOUNT = st.text_input('NO_CLAIM_DISCOUNT')
    SPECIAL_DISCOUNT= st.text_input('SPECIAL_DISCOUNT')
    SUM_INSURED  = st.text_input('SUM_INSURED')
    LOADINGS = st.text_input('LOADINGS')
    FLAG_POLICY_TYPE_OF_COVER_CHANGE_IN_LAST_12_MONTHS = st.text_input('FLAG_POLICY_TYPE_OF_COVER_CHANGE_IN_LAST_12_MONTHS')
    POLICY_HISTORY_AGE = st.text_input('POLICY_HISTORY_AGE')
    POLICY_TERM = st.text_input('POLICY_TERM')
    COMPANY_LOADINGS = st.text_input('COMPANY_LOADINGS')
    TYPE_OF_COVER= st.text_input('TYPE_OF_COVER')
    TRANSACTION_TYPE = st.text_input('TRANSACTION_TYPE')
    CLIENT_GENDER = st.text_input('CLIENT_GENDER')
    OPEN_RESTRICTED_FLAG = st.text_input('OPEN_RESTRICTED_FLAG')
    PA_DRIVER_INCLUDED = st.text_input(' PA_DRIVER_INCLUDED')
    VEHICLE_CONDITION = st.text_input('VEHICLE_CONDITION')
    FLAG_VEHICLE_CONDITION = st.text_input('FLAG_VEHICLE_CONDITION')
    FLAG_VEHICLE_TYPE_ON_SEATING_CAPACITY = st.text_input('FLAG_VEHICLE_TYPE_ON_SEATING_CAPACITY')


    
    
    # code for Prediction
    Prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Claim risk prediction'):
        Prediction = claimrisk_prediction([PREMIUM_CHARGED, NO_CLAIM_DISCOUNT, SPECIAL_DISCOUNT, SUM_INSURED, LOADINGS,  FLAG_POLICY_TYPE_OF_COVER_CHANGE_IN_LAST_12_MONTHS,  POLICY_HISTORY_AGE,  POLICY_TERM, COMPANY_LOADINGS, TYPE_OF_COVER,TRANSACTION_TYPE,CLIENT_GENDER,OPEN_RESTRICTED_FLAG,PA_DRIVER_INCLUDED,VEHICLE_CONDITION,FLAG_VEHICLE_CONDITION,FLAG_VEHICLE_TYPE_ON_SEATING_CAPACITY])
        
        
    st.success(Prediction)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    