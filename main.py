from flask import Flask, send_file, jsonify, send_from_directory
import shutil
import shutil
# from dotenv import load_dotenv
# import hashlib

# load_dotenv()

app = Flask(__name__, static_url_path='/static')

@app.route('/api/resourcepack', methods=["POST", "GET"])
def api_resourcepack():
    return send_file("pack.zip", download_name="pack.zip")

if __name__ == '__main__':
    shutil.make_archive("pack", 'zip', "pack")
    app.run()
