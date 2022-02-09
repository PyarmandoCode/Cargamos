from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    template_name="index.html"
    return render_template(template_name)


app.run(debug=True)    

