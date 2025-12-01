import streamlit as st

st.title("โปรแกรมคำนวณเกรด 🎓")

score = st.number_input("กรอกคะแนน", min_value=0.0, max_value=100.0, step=1.0)

if st.button("คำนวณเกรด"):
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    st.success(f"เกรดของคุณคือ: **{grade}**")
