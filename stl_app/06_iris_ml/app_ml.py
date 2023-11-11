import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score 

from sklearn.ensemble import RandomForestClassifier 

from sklearn.model_selection import train_test_split 

import pickle 

 

penguin_df = pd.read_csv('iris.csv') #อ่านไฟล์
penguin_df.dropna(inplace=True) #ตัดบรรทัดที่ว่าง
output = penguin_df['variety'] #เลือกเฉพาะ Column นี้  เอาข้อมูลมา แต่ไม่ได้เอา หัว Column มา ,(ข้อมูลเชิงคุณภาพ)
features = penguin_df[['sepal.length',
                        'sepal.width',
                        'petal.length',
                        'petal.width']]#เลือกเอาตัววไหนมาแสดงบ้าง , คอลัมน์ที่เหลือ


features = pd.get_dummies(features)
output, uniques = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(
	features, output, test_size=.8) #test_size=.8 เอาข้อมูล 80%
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
score = accuracy_score(y_pred, y_test)
print('Our accuracy score for this model is {}'.format(score))



rf_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()



fig, ax = plt.subplots()

ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)
plt.title('Which features are the most important for species prediction?')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
fig.savefig('feature_importance.png')