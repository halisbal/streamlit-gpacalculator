from pprint import pprint
import streamlit as st
import pandas as pd
import json

f = open("departments.json")
faculty_data = json.load(f)
faculties = list(faculty_data.get(faculty).get("name") for faculty in faculty_data.keys())
df = pd.read_csv("regdata.csv")
df.drop_duplicates(inplace=True, subset=["course_name", "course_prefix"])
df.drop(columns=['number'], inplace=True)
st.title("BOUN GPA Calculator")
list = []
faculty_choice = st.selectbox(label="Choose Your Faculty", options=faculties, index=3)
departments_data = {}
for a in faculty_data.keys():
    if faculty_data.get(a).get('name') == faculty_choice:
        departments_data = faculty_data.get(a).get('departments')
department_names = (departments_data.get(a).get('name') for a in departments_data.keys())
department_choice = st.selectbox(label="Choose Your Department", options=department_names)

department_data = {}
for a in departments_data.keys():
    if departments_data.get(a).get('name') == department_choice:
        department_data = departments_data.get(a)
grade_options = ["1","2","3","4","5","6","7","8"]
grade_choice = st.selectbox(label="Choose Your Semester", options=grade_options)
courses_data = department_data.get(grade_choice)
if department_choice == 'Computer Engineering':
    df = df[df['course_prefix'].isin(courses_data)]
    st.table(df)