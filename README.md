# heart_predection_system
A web page to predect if certain patient have heart disease or not by giving some measurements. 

## Dataset
The dataset was collected from Kaggle in the following link
https://www.kaggle.com/ronitf/heart-disease-uci

## Overview
This project is aimed to help doctors to decide if the patient has a heart disease or not. Overall, the project needs a lot of data to be trained for to provide an accurate results and some modification to make it perfect.

## Model used
The problem is considered as a binary classification problem. So, we used logistics regression model that can find the relationship between different factors then map it into a binary value (has disease or not).

## Web application
Flask framework was used as the middle ground between the website and the model. The website is a simple HTML and CSS form which takes the input from the user and send it to the model to predict the results. After that, Flask framework will take the result from the model and send it back to the website and calculate reports that shows what are the factors that may affect the person who is not a patient or if he/she is a patient, it will tell him/her what factors affected him/her the most.

