import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import streamlit as st

cred = credentials.Certificate("mykey.json")
firebase_admin.initialize_app(cred, {
	'databaseURL' : 'https://dutch-d63a7.firebaseio.com/'
})

def upload():

	data={
    	'Name':name,
    	'Age':age
	}
	result=db.post('/pythontest-29138/New',data)
	result2=db.get('/pythontest-29138/New','')
	st.success(result2)

st.title("Python connectivity with firebase")
name=st.text_input("Enter your name")
age=st.text_input("Enter your age")


if st.button("Upload"):
	upload()
