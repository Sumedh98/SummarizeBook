import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        book = request.form["book"]
        response = openai.Completion.create(model="text-davinci-003",prompt=generate_prompt(book),temperature=0.6,max_tokens=2000)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(book):
    #print("Summarize the book "+book)
    return ("Summarize the book "+book +" in 10 bullitin points")
