from flask import Flask , request , render_template
import pickle
import sklearn
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

@app.route('//')
def fun1():
    return render_template('index.html')
co = pickle.load(open('count.pkl','rb'))
sol = pickle.load(open('spam.pkl','rb'))
@app.route('/predict',methods = ['GET','POST'])
def fun2():
    if request.method == 'POST':
        text = request.form["message"]
        d = [text]
        vectors = co.transform(d)
        vectors = vectors.toarray()
        final = sol.predict(vectors)
        final = final[0]
        if final == 0:
            return render_template('index.html',prediction_text = "Not Spam")
        else:
            return render_template('index.html',prediction_text = "Spam Mail")




if __name__ == '__main__':
    app.run(debug=True)