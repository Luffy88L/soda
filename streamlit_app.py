import streamlit as st

# ส่วนหัวของแอป
st.title("คำนวณผลบวกและหาค่ามากที่สุด")
st.header("โปรแกรมคำนวณผลบวกของตัวเลขสองตัวและหาค่ามากที่สุดจาก 3 ตัวเลข")

# ส่วนคำนวณผลบวกของตัวเลขสองตัว
st.subheader("1. คำนวณผลบวกของตัวเลขสองตัว")
num1 = st.number_input("กรุณาป้อนตัวเลขตัวที่ 1", value=0.0)
num2 = st.number_input("กรุณาป้อนตัวเลขตัวที่ 2", value=0.0)

if st.button("คำนวณผลบวก"):
    sum_result = num1 + num2
    st.write(f"ผลบวกของ {num1} และ {num2} คือ {sum_result}")

# ส่วนคำนวณหาค่ามากที่สุดจาก 3 ตัวเลข
st.subheader("2. หาค่ามากที่สุดจาก 3 ตัวเลข")
num3 = st.number_input("กรุณาป้อนตัวเลขตัวที่ 3", value=0.0)

if st.button("หาค่ามากที่สุด"):
    max_num = max(num1, num2, num3)
    st.write(f"ค่ามากที่สุดจาก 3 ตัวเลข {num1}, {num2}, {num3} คือ {max_num}")
