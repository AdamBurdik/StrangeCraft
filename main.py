from flask import Flask, send_file, jsonify, send_from_directory
import shutil
import os
# from dotenv import load_dotenv
# import hashlib

# load_dotenv()

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def root():
    return "Root!"

@app.route('/api/resourcepack/', methods=["GET"])
def api_resourcepack():
    try:
        # Use the current working directory as the resource pack directory
        resource_pack_directory = os.getcwd()
        
        # Specify the filename of your Minecraft resource pack file
        resource_pack_filename = 'strangecraft_pack.zip'

        # Serve the file with Flask-Static-Compress
        return send_from_directory(resource_pack_directory, resource_pack_filename, as_attachment=True, download_name='strangecraft_pack.zip')

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error serving resource pack: {e}")

        # Alternatively, you can return a custom error response
        return "Internal Server Error", 500

if __name__ == '__main__':
    #shutil.make_archive("pack", 'zip', "zipped_pack")
    app.run()
