from flask import Flask, send_file, jsonify, send_from_directory
import shutil
# from dotenv import load_dotenv
# import hashlib

# load_dotenv()

app = Flask(__name__, static_url_path='/static')

@app.route('/api/resourcepack')
def api_resourcepack():
    return send_file("strangecraft_pack.zip", as_attachment=True, download_name='strangecraft_pack.zip', mimetype='application/zip', cache_timeout=0)

if __name__ == '__main__':
    #shutil.make_archive("pack", 'zip', "zipped_pack")
    app.run()
