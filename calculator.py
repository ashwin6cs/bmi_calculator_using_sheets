import streamlit as st
import gspread
from pytz import timezone
from datetime import datetime

gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('1CzZujaA5rUJ27I9SmnGAJRe04ESWo3VJv8gAGq4OT6s')
worksheet = sh.sheet1

name = st.text_input("Enter Your name", "")
result = name.title()

age = st.text_input("Enter Your Age", "")
result1 = age.title()

status = st.radio("Select Gender: ", ('Male', 'Female'))

try:
    weight = st.number_input("Enter your weight (in kgs)")
    # take height input in feet
    height = st.number_input('Enter your height (in feet)')
    bmi = weight / ((height / 3.28) ** 2)
    bmi1 = str(bmi)
    bmi2 = bmi1[:5]
except:
    pass

if st.button('Calculate BMI'):
    st.text("Your BMI Index is {}.".format(bmi2))
    if bmi < 16:
        category = "Extremely Underweight"
        st.error("You are Extremely Underweight")
    elif 16 <= bmi < 18.5:
        category = "Underweight"
        st.warning("You are Underweight")
    elif 18.5 <= bmi < 25:
        category = "Healthy"
        st.success("You are Healthy")
    elif 25 <= bmi < 30:
        category = "Overweight"
        st.warning("You are Overweight")
    elif bmi >= 30:
        category = "Extremely Overweight"
        st.error("You are Extremely Overweight")
    n = " "
    user = [datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S'), n, name, age, status, weight, height, bmi2, category]
    worksheet.append_row(user)
























