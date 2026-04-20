import pickle
import pandas as pd

# =========================
# LOAD TRAINED MODEL
# =========================
model = pickle.load(open("model.pkl","rb"))

# =========================
# FEATURES USED BY MODEL
# =========================
model_features = [
'poutcome_success','previous','contact_cellular','default_no',
'not_working','month_oct','month_mar','month_sep','job_retired',
'job_student','month_apr','marital_single','month_dec',
'education_university.degree','job_admin.','job_services',
'marital_married','education_basic.9y','job_blue-collar','campaign',
'default_unknown','month_may','poutcome_nonexistent',
'contact_telephone','no_previous_contact','pdays'
]

# =========================
# FUNCTION: TAKE USER INPUT (ALL 60 COLS)
# =========================
def take_user_input():

    data = {}
    print("\nEnter all details:\n")

    # numeric
    data['age'] = int(input("Age: "))
    data['campaign'] = int(input("Campaign: "))
    data['pdays'] = int(input("Pdays: "))
    data['previous'] = int(input("Previous contacts: "))
    data['no_previous_contact'] = int(input("No previous contact (1/0): "))
    data['not_working'] = int(input("Not working (1/0): "))

    # job (one hot)
    print("\nJob (enter 1 for yes else 0)")
    jobs = ['job_admin.','job_blue-collar','job_entrepreneur','job_housemaid',
            'job_management','job_retired','job_self-employed','job_services',
            'job_student','job_technician','job_unemployed','job_unknown']

    for j in jobs:
        data[j] = int(input(f"{j}: "))

    # marital
    print("\nMarital")
    mar = ['marital_divorced','marital_married','marital_single','marital_unknown']
    for m in mar:
        data[m] = int(input(f"{m}: "))

    # education
    print("\nEducation")
    edu = ['education_basic.4y','education_basic.6y','education_basic.9y',
           'education_high.school','education_illiterate',
           'education_professional.course','education_university.degree',
           'education_unknown']
    for e in edu:
        data[e] = int(input(f"{e}: "))

    # default
    print("\nCredit default")
    for d in ['default_no','default_unknown','default_yes']:
        data[d] = int(input(f"{d}: "))

    # housing
    print("\nHousing loan")
    for h in ['housing_no','housing_unknown','housing_yes']:
        data[h] = int(input(f"{h}: "))

    # personal loan
    print("\nPersonal loan")
    for l in ['loan_no','loan_unknown','loan_yes']:
        data[l] = int(input(f"{l}: "))

    # contact
    print("\nContact type")
    for c in ['contact_cellular','contact_telephone']:
        data[c] = int(input(f"{c}: "))

    # month
    print("\nMonth")
    months = ['month_apr','month_aug','month_dec','month_jul','month_jun',
              'month_mar','month_may','month_nov','month_oct','month_sep']
    for m in months:
        data[m] = int(input(f"{m}: "))

    # day
    print("\nDay of week")
    days = ['day_of_week_fri','day_of_week_mon','day_of_week_thu',
            'day_of_week_tue','day_of_week_wed']
    for d in days:
        data[d] = int(input(f"{d}: "))

    # poutcome
    print("\nPrevious outcome")
    for p in ['poutcome_failure','poutcome_nonexistent','poutcome_success']:
        data[p] = int(input(f"{p}: "))

    return data


# =========================
# FUNCTION: PREDICT
# =========================
def predict_loan():

    user_data = take_user_input()

    # convert to dataframe
    df = pd.DataFrame([user_data])

    # give model only required columns
    df_model = df.reindex(columns=model_features, fill_value=0)

    pred = model.predict(df_model)[0]
    prob = model.predict_proba(df_model)[0][1]

    print("\n========== RESULT ==========")
    if pred == 1:
        print("Loan Approved ✅")
    else:
        print("Loan Rejected ❌")

    print(f"Approval Probability: {prob:.2f}")


# =========================
# RUN MODEL
# =========================
predict_loan()
