import streamlit as st

st.set_page_config(page_title="CGPA Predictor", page_icon="🎓")

st.title("🎓 CGPA Predictor & Calculator")
st.write("Calculate your new CGPA by combining your current standing with this semester's results.")

# --- SECTION 1: PREVIOUS STANDING ---
st.subheader("Current Academic Standing")
c1, c2 = st.columns(2)
with c1:
    prev_cgpa = st.number_input("Current CGPA", min_value=0.0, max_value=10.0, step=0.01)
with c2:
    prev_credits = st.number_input("Total Credits Completed", min_value=0.0, step=1.0)

st.divider()

# --- SECTION 2: NEW SUBJECTS ---
st.subheader("New Semester Subjects")

if 'num_subjects' not in st.session_state:
    st.session_state.num_subjects = 1

col1, col2 = st.columns(2)
with col1:
    if st.button("➕ Add Subject"):
        st.session_state.num_subjects += 1
with col2:
    if st.button("➖ Remove Subject") and st.session_state.num_subjects > 1:
        st.session_state.num_subjects -= 1

# Logic to calculate points for new subjects
new_total_points = 0.0
new_total_credits = 0.0

for i in range(st.session_state.num_subjects):
    cols = st.columns([1, 2, 2])
    with cols[0]:
        st.markdown(f"**Sub {i+1}**")
    with cols[1]:
        cr = st.number_input(f"Credits", min_value=0.0, step=0.5, key=f"cr_{i}")
    with cols[2]:
        gr = st.number_input(f"Grade Point", min_value=0.0, max_value=10.0, step=0.1, key=f"gr_{i}")
    
    new_total_points += (cr * gr)
    new_total_credits += cr

st.divider()

# --- SECTION 3: FINAL CALCULATION ---

# Calculate points already earned
old_total_points = prev_cgpa * prev_credits

# Sum everything up
grand_total_points = old_total_points + new_total_points
grand_total_credits = prev_credits + new_total_credits

if grand_total_credits > 0:
    final_cgpa = grand_total_points / grand_total_credits
    
    st.metric(label="Calculated New CGPA", value=f"{final_cgpa:.2f}", 
              delta=f"{final_cgpa - prev_cgpa:.2f}" if prev_cgpa > 0 else None)
    
    if final_cgpa >= 8.5:
        st.balloons()
        st.success("Excellent standing! 🌟")
    elif final_cgpa >= 7.5:
        st.success("Great job! Keep it up. 👍")
else:
    st.info("Enter your credits and grades above to see your updated CGPA.")