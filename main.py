from flask import Flask
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def root():
    return "Root!"

if __name__ == '__main__':
    app.run()
