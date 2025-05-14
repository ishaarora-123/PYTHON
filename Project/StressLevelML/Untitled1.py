from ipynb.fs.full.Untitled import pipe
import joblib
import pandas as pd
import streamlit as st
def main():
    st.title("Sample Streamlit Form with Various Inputs")
    with st.form(key="sample_form"):
        name = st.text_input("Enter your name: ")
        age = st.radio("What is your age group? ", options=['18-24', '14-17', '25-34', '45-54', '35-44'])
        gender = st.radio("Select your Gender: ", options=['Male', 'Female'])
        hobbies = st.multiselect("Type of Hobbies you engage in?(Select all that apply) ", options=["Creative", "Social", "Physical", "Intellectual", "Others"])
        frequency = st.radio("How often do you engage in your hobbies? ", options=['Several times a week', 'Weekly', 'Daily', 'Less frequently',
       'Monthly'])
        hoursperweek = st.radio("On average, how many hours per week do you spend on your hobbies? ",options = ['1 to 3 hours', '4 to 7 hours', '8+ hours', 'Less than 1 hour'])
        stresslevel = st.radio("What is your current stress level? ", options=['Low', 'Moderate','High'])
        moodeffects = st.radio("How does engaging in your hobbies typically affect your mood? ", options=['Improves my mood', 'No noticeable change', 'Worsens my mood'])
        benefits = st.multiselect("What benefits do you gain from engaging in your hobbies? (Select all that apply) ", options=['Relaxation', 'Improved focus', 'Reduced stress', 'Increased Happiness'])
        socialcontext = st.radio("Do you mostly engage in your hobbies alone or with others? ",options = ['With friends or groups', 'Alone', 'Both equally'])
        dict = {'Name':name, 'AgeGroup':age,'Gender':gender,'Hobbies':hobbies,'Frequency':frequency,'HoursPerWeek':hoursperweek,'StressLevel':stresslevel,'MoodEffect':moodeffects,'Benefits':benefits,'SocialContext':socialcontext}
        df = pd.DataFrame(dict)
        # Submit button
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            filename = 'grid.joblib'
            joblib.dump(grid, filename)
            df = pipe.fit_transform(df)
            st.write(df)



if __name__ == '__main__':
    main()