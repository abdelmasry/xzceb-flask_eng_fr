from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = translator.englishtofrench(textToTranslate) 
    return result
    

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    result = translator.frenchtotenglish(textToTranslate)
    return result

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("DEVOPs/FinalProject/xzceb-flask_eng_fr/final_project/templates/index.html")

if __name__=="__main__":
    app.run(debug=True) 
