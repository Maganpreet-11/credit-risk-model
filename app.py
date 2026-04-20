import streamlit as st
import pandas as pd
import pickle

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open("model.pkl","rb"))

model_features = [
'poutcome_success','previous','contact_cellular','default_no',
'not_working','month_oct','month_mar','month_sep','job_retired',
'job_student','month_apr','marital_single','month_dec',
'education_university.degree','job_admin.','job_services',
'marital_married','education_basic.9y','job_blue-collar','campaign',
'default_unknown','month_may','poutcome_nonexistent',
'contact_telephone','no_previous_contact','pdays'
]

st.title("🏦 AI Loan Approval Predictor")

# =========================
# BASIC NUMERIC INPUTS
# =========================
age = st.number_input("Age",18,100,30)
campaign = st.number_input("Campaign contacts",0,50,1)
pdays = st.number_input("Pdays",0,999,999)
previous = st.number_input("Previous contacts",0,20,0)

# =========================
# FULL CATEGORY INPUTS
# =========================

job = st.selectbox("Job",[
"admin.","blue-collar","entrepreneur","housemaid","management",
"retired","self-employed","services","student","technician",
"unemployed","unknown"
])

marital = st.selectbox("Marital",[
"divorced","married","single","unknown"
])

education = st.selectbox("Education",[
"basic.4y","basic.6y","basic.9y","high.school",
"illiterate","professional.course","university.degree","unknown"
])

default = st.selectbox("Credit default",["no","unknown","yes"])
housing = st.selectbox("Housing loan",["yes","no","unknown"])
loan = st.selectbox("Personal loan",["yes","no","unknown"])
contact = st.selectbox("Contact type",["cellular","telephone"])

month = st.selectbox("Month",[
"jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"
])

day = st.selectbox("Day of week",[
"mon","tue","wed","thu","fri"
])

poutcome = st.selectbox("Previous outcome",[
"failure","nonexistent","success"
])

# =========================
# PREDICT BUTTON
# =========================
if st.button("Predict"):

    # create all columns default 0
    cols = [
    'age','campaign','pdays','previous','no_previous_contact','not_working',
    'job_admin.','job_blue-collar','job_entrepreneur','job_housemaid',
    'job_management','job_retired','job_self-employed','job_services',
    'job_student','job_technician','job_unemployed','job_unknown',
    'marital_divorced','marital_married','marital_single','marital_unknown',
    'education_basic.4y','education_basic.6y','education_basic.9y',
    'education_high.school','education_illiterate',
    'education_professional.course','education_university.degree',
    'education_unknown','default_no','default_unknown','default_yes',
    'housing_no','housing_unknown','housing_yes','loan_no','loan_unknown',
    'loan_yes','contact_cellular','contact_telephone','month_apr','month_aug',
    'month_dec','month_jul','month_jun','month_mar','month_may','month_nov',
    'month_oct','month_sep','day_of_week_fri','day_of_week_mon',
    'day_of_week_thu','day_of_week_tue','day_of_week_wed',
    'poutcome_failure','poutcome_nonexistent','poutcome_success'
    ]

    data = {c:0 for c in cols}

    # numeric
    data["age"]=age
    data["campaign"]=campaign
    data["pdays"]=pdays
    data["previous"]=previous
    data["no_previous_contact"]=1 if previous==0 else 0

    # job
    data[f"job_{job}"]=1

    # marital
    data[f"marital_{marital}"]=1

    # education
    data[f"education_{education}"]=1

    # default
    data[f"default_{default}"]=1

    # housing
    data[f"housing_{housing}"]=1

    # loan
    data[f"loan_{loan}"]=1

    # contact
    data[f"contact_{contact}"]=1

    # month
    if month in ["mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]:
        data[f"month_{month}"]=1

    # day
    data[f"day_of_week_{day}"]=1

    # poutcome
    data[f"poutcome_{poutcome}"]=1

    df = pd.DataFrame([data])
    df_model = df.reindex(columns=model_features, fill_value=0)

    pred = model.predict(df_model)[0]
    prob = model.predict_proba(df_model)[0][1]

    if pred==1:
        st.success(f"Loan Approved ✅ Probability: {prob:.2f}")
    else:
        st.error(f"Loan Rejected ❌ Probability: {prob:.2f}")
