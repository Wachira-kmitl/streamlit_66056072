import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Palmer's Iris")
st.markdown('สร้าง `scatter plot` แสดงผลข้อมูล **Palmer\'s  **Iris dataset**')

choices = ['sepal.length',
           'sepal.width',
           'petal.length',
           'petal.width']
# https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# 1. สร้าง st.selectbox ของ ตัวเลือก แกน x และ y จาก choices
# selected_x_var = 'อะไรดี'
# selected_y_var = 'อะไรดี'
selected_x_var = st.selectbox('เลือกตัวแปรแกน x', choices)
selected_y_var = st.selectbox('เลือกตัวแปรแกน y', choices)

# https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# 2. สร้าง st.file_uploader เพื่อให้เลือกไฟล์ .csv เท่านั้น จากเครื่องผู้ใช้งาน
iris_file = st.file_uploader("Choose a CSV file", type=['csv'])

if iris_file is not None: #ถ้าไฟล์ ไม่ว่าง
    iris_df = pd.read_csv(iris_file)
else:
    st.stop()

st.subheader('ข้อมูลตัวอย่าง')
st.write(iris_df) #แสดงเป็น Pandas

st.subheader('แสดงผลข้อมูล')
sns.set_style('darkgrid') #พื้นหลังสีเข้ม
markers = {"Setosa": "v", "Versicolor": "s", "Virginica": 'o'}  #ชื่อตามแถว แนวนอน variety
#"Setosa": "v" สามเหลี่ยม , "Versicolor": "s" สีเหลี่ยม, "Virginica": 'o' วงกลม

fig, ax = plt.subplots()
ax = sns.scatterplot(data=iris_df, #ไฟล์ที่อัปเข้าไป
                     x=selected_x_var, y=selected_y_var, #ชื่อ เป็น str
                     hue="variety", markers=markers, style="variety")
#hue='ชื่อหัว column' การแยกสีของแต่ละอัน ,markers=markers แยก สีเหลี่ยม สามเหลี่ยม style=ชื่อหัว column
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Palmer's Iris dataset")
st.pyplot(fig)


