from flask import Flask, render_template, redirect, url_for
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/nabor/builder")
def nabor_builder():
    return redirect("https://forms.gle/16Z2TFpDVY2fbk2G9")

@app.route("/nabor/helper")
def nabor_helper():
    return redirect("https://forms.gle/xqiLifQ7MFaSoMTh7")

@app.route("/resourcepack")
def resourcepack():
    return redirect("https://moep.tv/minecraft/rp")

@app.route("/vote/cc")
def vote_cc():
    return redirect("https://czech-craft.eu/server/strangecraft/vote/")

@app.route("/vote/cl")
def vote_cl():
    return redirect("https://craftlist.org/strangecraft-eu")

@app.route("/vote/ms")
def vote_ms():
    return redirect("https://minecraftservery.eu/server/strangecraft/vote")



if __name__ == '__main__':
    app.run()
