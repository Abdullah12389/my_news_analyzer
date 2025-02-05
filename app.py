from textblob import TextBlob
from newspaper import Article
import nltk
from flask import Flask,render_template,request
nltk.download("punkt")
app=Flask(__name__)
@app.route("/",methods=['GET'])
def search():
    return render_template("index.html")
@app.route("/show",methods=["POST"])
def show():
    url=request.form['link']
    article=Article(url)
    article.download()
    article.parse()
    article.nlp()
    analysis=TextBlob(article.text)
    data=[article.title,article.publish_date,article.authors,article.summary,article.keywords,analysis.polarity]
    return render_template("index.html",data=data)





