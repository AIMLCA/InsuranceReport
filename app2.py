# Import necessary libraries
import docx2txt
import pandas as pd
import os
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from flask import Flask, request, jsonify,render_template
from sklearn.linear_model import LogisticRegression
# Set the path to the folder containing the doc files
# path = r'C:\xampp\htdocs\Inteligence\Training Data'
# Create an empty DataFrame to store the data

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    return render_template("index.html")
@app.route('/loadData', methods=['POST','GET'])
def loadData():
    observation = request.form.get("Observation")
    print(observation)
    discussion = request.form.get("Dsicussion")
    conclusion = request.form.get("Conclusion")
    df = pd.DataFrame({'observation': [observation], 'discussion': [discussion], 'conclusion': [conclusion]})
    dfs=[]
    dfs.append(df)
    
    # Initialize an empty list to store the data
      

    # Concatenate all the DataFrames in the list into a single DataFrame
    df = pd.concat(dfs, ignore_index=True)
    # Save the data to a CSV file
    df.to_csv('data_train.csv', mode='a', header=False, index=False)
    return {"message": "Model trained successfully"}

   

@app.route('/train_model', methods=['POST','GET'])
def train_model():   
     # Load the data
    data = pd.read_csv('data_train.csv')
    data = data.replace('NA', '')
    data['observation'] = data['observation'].apply(preprocess_text)
    data['discussion'] = data['discussion'].apply(preprocess_text)

    # Concatenate the observations and discussion columns
    data['text'] = data['observation'] + ' ' + data['discussion']

    # print(data.shape[0])
    # print(data.columns)

    # Split the data into training and validation sets
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['conclusion'], test_size=0.2)

    # Vectorize the text data using TF-IDF
    tfidf = TfidfVectorizer()
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    # Train the logistic regression model
    lr = LogisticRegression()
    lr.fit(X_train_tfidf, y_train)
  
    
    
    return {"message": "Model trained successfully"}



@app.route('/test_model', methods=['POST','GET'])
def test_model():
    redata=[]
    data = pd.read_csv('data_train.csv')
    data = data.replace('NA', '')
    data['observation'] = data['observation'].apply(preprocess_text)
    data['discussion'] = data['discussion'].apply(preprocess_text)

    # Concatenate the observations and discussion columns
    data['text'] = data['observation'] + ' ' + data['discussion']

    # print(data.shape[0])
    # print(data.columns)

    # Split the data into training and validation sets
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['conclusion'], test_size=0.2)

    # Vectorize the text data using TF-IDF
    tfidf = TfidfVectorizer()
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    # Train the logistic regression model
    lr = LogisticRegression()
    lr.fit(X_train_tfidf, y_train)
    observation = request.form.get("observations")
    discussion = request.form.get("discussions")
    # Deploy the model

    new_text = observation + discussion
    new_text = preprocess_text(new_text)
    new_text_tfidf = tfidf.transform([new_text])
    new_conclusion = lr.predict(new_text_tfidf)
    print(new_conclusion)

    user = {"question": new_conclusion[0]}
    redata.append(user)
    
    return jsonify(redata)
   
    
    
# Preprocess the data
def preprocess_text(text):
    if not isinstance(text, (str, bytes)):
        return ''
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    stop_words = set(stopwords.words('english'))
    text = [word for word in text if not word in stop_words]
    text = ' '.join(text)
    return text



if __name__ == '__main__':
    app.run()