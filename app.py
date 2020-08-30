import streamlit as st
import pickle
import numpy as np
from PIL import Image
model=pickle.load(open('model.pkl','rb'))

def inputs():
    Gender = st.selectbox("Select Gender",tuple(Gender_label.keys()))
    Married = st.selectbox("Select Marital Status",tuple(Married_label.keys()))
    Dependents = st.selectbox("Select Number of Dependents",tuple(Dependents_label.keys()))
    Education = st.selectbox("Select Education",tuple(Education_label.keys()))
    Self_Employed = st.selectbox("Select Self Employed or not",tuple(Self_Employed_label.keys()))
    Property_Area = st.selectbox("Select Property Area",tuple(Property_Area_label.keys()))
   
    #encoding
    v_Gender=get_value(Gender,Gender_label)
    v_Married=get_value(Married,Married_label)
    v_Dependents=get_value(Dependents,Dependents_label)
    v_Education=get_value(Education,Education_label)
    v_Self_Employed=get_value(Self_Employed,Self_Employed_label)
    v_Property_Area=get_value(Property_Area,Property_Area_label)
    
    ApplicantIncome = st.number_input("Applicant Income")
    CoapplicantIncome=st.number_input("Coapplicant Income")
    LoanAmount=st.number_input("Loan Amount")
    Loan_Amount_Term=st.number_input("Loan Amount Term")
    Credit_History=st.number_input("Credit History (0/1)")
    
    data=np.array([[v_Gender,v_Married,v_Dependents,v_Education,v_Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,v_Property_Area]]).astype(np.int64)
    
    return data
    

Gender_label={'Male':1,'Female':0}
Married_label={'Yes':1,'No':0}
Dependents_label={'0':0,'1':1,'2':2,'3+':3}
Education_label={'Graduate':1,'Not Graduate':0}
Self_Employed_label={'Yes':1,'No':0}
Property_Area_label={'Urban':2,'Rural':0,'Semiurban':1}

#get the values
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value

def main():
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Loan Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    input=inputs()
    
    if st.button("predict"):
        prediction=model.predict(input)
        pred='{0}'.format(prediction[0])
        if pred == '1':
            st.success("Loan is Approved")
            img1=Image.open("approved.jfif")
            st.image(img1,width=200)
        else:
            st.error("Loan is Rejected")
            img2=Image.open("rejected.jpg")
            st.image(img2,width=200)
if __name__ == '__main__':
    main()
