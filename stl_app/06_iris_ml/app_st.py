import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Iris Classifier')
st.write("This app uses 6 inputs to predict the Variety of Iris using "
         "a model built on the Palmer's Iris's dataset. Use the form below"
         " to get started!")

iris_file = st.file_uploader('Upload your own iris data')

if iris_file is None: #ถ้าเป็น ค่าว่าง
    rf_pickle = open('random_forest_penguin.pickle', 'rb')
    map_pickle = open('output_penguin.pickle', 'rb')

    rfc = pickle.load(rf_pickle)
    unique_penguin_mapping = pickle.load(map_pickle)

    rf_pickle.close()
else:
    iris_df = pd.read_csv(iris_file)
    iris_df = iris_df.dropna() #ลบบรรทัดว่าง

    output = iris_df['variety'] #ขื่อหัว Column ที่ ในชุดข้อมูลเหมือนกัน(ชื่อหัว Col ที่สนใจ)
                                   #เอาแค่ ข้อมูลในนั้น
    features = iris_df[['sepal.length',
                        'sepal.width',
                        'petal.length',
                        'petal.width']] #ชื่อชุดข้อมูล และ เอา ทั้งหัว,ข้อมูล

    features = pd.get_dummies(features) #กลับไปอ่าน งง

    output, unique_penguin_mapping = pd.factorize(output)

    x_train, x_test, y_train, y_test = train_test_split(
        features, output, test_size=.8)

    rfc = RandomForestClassifier(random_state=15)
    rfc.fit(x_train, y_train)

    y_pred = rfc.predict(x_test)

    score = round(accuracy_score(y_pred, y_test), 2)  #ทศนิยม

    st.write('We trained a Random Forest model on these data,'
             ' it has a score of {}! Use the '
             'inputs below to try out the model.'.format(score))

with st.form('user_inputs'): #จะต้องไม่มีตัวที่เลือก ไปเป็นหัว variety
    sepal_length = st.number_input(
        'Sepal Length', min_value=0.0, max_value=12.0, value=10.0)  #ชื่อ "colimn" , options=[ชื่อ] เนื่องจากเป็นตัวเลข ต้องใส่ min_value , max_value
    sepal_width = st.number_input(
        'Sepal Width', min_value=0.0, max_value=12.0, value=10.0)
    petal_length = st.number_input(
        'Petal Length', min_value=0.0, max_value=12.0, value=10.0)
    petal_width = st.number_input(
        'Petal Width', min_value=0.0, max_value=12.0, value=10.0)
    st.form_submit_button()



#กรณีที่ ค่า เป็นเชิงปริมาณ (เอาหัว column และ ชื่อตัวแปร ที่แปรจากเชิงคุณภามาแล้ว มาใส่ทุกหมด)
new_prediction = rfc.predict([[sepal_length, sepal_width, petal_length,petal_width]])

prediction_species = unique_penguin_mapping[new_prediction][0]
st.write('We predict your Iris is of the {} species'.format(prediction_species))



#อ่านเอง
st.title("Iris ")
st.markdown('สร้าง `scatter plot` แสดงผลข้อมูล **Palmer\'s Penguins** กัน แบบเดียวกับ **Iris dataset**')

choices = ['sepal.length',
           'sepal.width',
           'petal.length',
           'petal.width']

selected_x_var = st.selectbox('เลือก แกน x', (choices))
selected_y_var = st.selectbox('เลือก แกน y', (choices))


st.subheader('ข้อมูลตัวอย่าง')
st.write(iris_df)

st.subheader('แสดงผลข้อมูล')
sns.set_style('darkgrid')
markers = {"Setosa": "v", "Versicolor": "s", "Virginica": 'o'} #ชื่อตามแถว แนวนอน
#"Setosa": "v" สามเหลี่ยม , "Versicolor": "s" สีเหลี่ยม, "Virginica": 'o' วงกลม
fig, ax = plt.subplots()
ax = sns.scatterplot(data=iris_df,
                     x=selected_x_var, y=selected_y_var,
                     hue='variety', markers=markers, style='variety')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Palmer's Penguins Data")
st.pyplot(fig)