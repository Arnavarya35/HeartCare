import streamlit as st
import pickle
import numpy as np
import warnings

def load_model():
	with open('saved_model.pkl', 'rb') as file:
		data = pickle.load(file)
	return data

model = load_model()

warnings.filterwarnings('ignore')
def show_predictpage():
	st.title('Heart Disease Prediction')
	st.image('da_proj_background_image.jpg', use_column_width=True)
	st.write(""" ### We need some information to predict the chances of you having a heart disease""")
	st.markdown("For more information, Email: arnavarya35@gmail.com.")

	
	gender = st.selectbox("Gender", ("Female", "Male"))
	# age = st.slider("Age", 1, 110, 20)
	age = st.number_input("Age", 1, 110)
	smoker = st.selectbox("Current Smoker", ("Yes", "No"))
	bpmeds = st.selectbox("On any BPMeds", ("Yes", "No"))
	prestroke = st.selectbox("Prevalent Stroke", ("Yes", "No"))
	prehyp = st.selectbox("Prevalent Hypertension", ("Yes", "No"))
	diabetes = st.selectbox("Diabetes", ("Yes", "No"))

	totChol = st.number_input("Total Cholestrol", min_value=40., max_value=400., step=1.,format="%.2f")

	#sysBP = st.slider("Systolic BP", 80, 250, 120)
	sysBP = st.number_input("Systolic BP", min_value=80., max_value=250., step=1.,format="%.2f")

	#diaBP = st.slider("Diastolic BP", 50, 120, 65)
	diaBP = st.number_input("Diastolic BP", min_value=50., max_value=150.,step=1.,format="%.2f")

	#bmi = st.slider("BMI", 15, 35, 19)
	bmi = st.number_input("BMI", min_value=15., max_value=35.,step=1.,format="%.2f")

	heartrate = st.number_input("Heart Rate", 30, 150)

	y = [gender, smoker, bpmeds, prestroke, prehyp, diabetes]
	for i in range(len(y)):
		if y[i] == "Yes" or y[i] == "Male":
			y[i] = 1
		elif y[i] == "No" or y[i] == "Female":
			y[i] = 0
	gender = y[0]
	smoker = y[1]
	bpmeds = y[2]
	prestroke = y[3]
	prehyp = y[4]
	diabetes = y[5]

	ok = st.button("Predict")
	if ok:
		x = np.array([[gender, age, smoker, bpmeds, prestroke, prehyp, diabetes, totChol, sysBP, diaBP, bmi, heartrate]])
		x = x.astype(float)
		x = x.reshape(1,-1)

		disease = model.predict(x)
		if disease == 1:
			st.subheader('You are at a risk of heart disease \n *Consult a Doctor')
		else:
			st.subheader('You are Healthy.')
      
