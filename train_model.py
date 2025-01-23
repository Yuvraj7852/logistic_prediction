import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
import numpy as np
data = np.array([[1,0], [2,0], [3,0], [4,1], [5,1], [6,1], [7,1]])

x=data[:, 0].reshape(-1,1)
y=data[:, 1]



x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)

joblib.dump(model,'student.pkl')
print("model save")