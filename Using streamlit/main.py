import streamlit as st

st.set_page_config(page_title="CGPA Calculator", page_icon="🎓")

st.title("🎓 Dynamic CGPA Calculator")
st.write("Add your subjects below to calculate your CGPA.")

# 1. Initialize the number of subjects in session state
if 'num_subjects' not in st.session_state:
    st.session_state.num_subjects = 1

# 2. Layout for adding/removing rows
col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Add Subject"):
        st.session_state.num_subjects += 1
with col2:
    if st.button("➖ Remove Subject") and st.session_state.num_subjects > 1:
        st.session_state.num_subjects -= 1

# 3. Create the input rows dynamically
total_points = 0.0
total_credits = 0.0

st.divider()

for i in range(st.session_state.num_subjects):
    cols = st.columns([1, 2, 2]) # Index, Credits, Grade
    with cols[0]:
        st.markdown(f"**Sub {i+1}**")
    with cols[1]:
        credits = st.number_input(f"Credits", min_value=0.0, step=0.5, key=f"cr_{i}")
    with cols[2]:
        grade = st.number_input(f"Grade Point", min_value=0.0, max_value=10.0, step=0.1, key=f"gr_{i}")
    
    total_points += (credits * grade)
    total_credits += credits

st.divider()

# 4. Calculation Logic
if total_credits > 0:
    cgpa = total_points / total_credits
    st.success(f"### Your CGPA is: {cgpa:.2f}")
    
    # Visual feedback based on score
    if cgpa >= 7.5:
        st.balloons()
else:
    st.info("Enter your credits and grades above to see the result.")