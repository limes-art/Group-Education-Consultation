import streamlit as st
import pandas as pd

st.title("Student Support Grouping Platform")

try:
    df = pd.read_csv('studentinfo.csv')
except FileNotFoundError:
    st.error("Could not find 'studentinfo.csv'. Please check the file path.")
    st.stop()

st.write("**Preview of the CSV data**:")
st.write(df.head())

df.columns = df.columns.str.strip()  
df['Grade'] = pd.to_numeric(df['Grade'], errors='coerce')
df.dropna(subset=['Grade'], inplace=True)

def assign_grade_group(grade):
    if grade < 20:
        return "0-20"
    elif grade < 40:
        return "20-40"
    elif grade < 60:
        return "40-60"
    elif grade < 80:
        return "60-80"
    else:
        return "80-100"

df['Grade Group'] = df['Grade'].apply(assign_grade_group)


selected_group = st.sidebar.selectbox(
    "Select Grade Group",
    ["All", "0-20", "20-40", "40-60", "60-80", "80-100"]
)

if selected_group == "All":
    # Display all groups
    for group in ["0-20", "20-40", "40-60", "60-80", "80-100"]:
        group_df = df[df['Grade Group'] == group]
        st.subheader(f"Grade Group: {group}")
        if group_df.empty:
            st.markdown("No students in this group.")
        else:
            for idx, row in group_df.iterrows():
                st.markdown("---")
                st.header(row["Name"])
                st.markdown(f"**Grade:** {row['Grade']}")
                st.markdown(f"**Income Range:** {row['Income Range']}")
                st.markdown(f"**University Aspirations:** {row['University Aspirations']}")
                st.markdown(f"**Hobbies:** {row['Hobbies']}")
else:
    # Filter for a single selected group
    df_filtered = df[df['Grade Group'] == selected_group]
    st.subheader(f"Grade Group: {selected_group}")
    if df_filtered.empty:
        st.markdown("No students in this group.")
    else:
        for idx, row in df_filtered.iterrows():
            st.markdown("---")
            st.header(row["Name"])
            st.markdown(f"**Grade:** {row['Grade']}")
            st.markdown(f"**Income Range:** {row['Income Range']}")
            st.markdown(f"**University Aspirations:** {row['University Aspirations']}")
            st.markdown(f"**Hobbies:** {row['Hobbies']}")
