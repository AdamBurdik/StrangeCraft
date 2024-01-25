from flask import Flask, render_template, redirect, url_for
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/nabor/builder")
def root():
    return redirect("https://forms.gle/16Z2TFpDVY2fbk2G9")

@app.route("/nabor/helper")
def root():
    return redirect("https://forms.gle/xqiLifQ7MFaSoMTh7")

if __name__ == '__main__':
    app.run()
