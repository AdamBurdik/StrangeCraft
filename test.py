import requests

url = "https://www.strangecraft.eu/api/resourcepack"  # Update with the actual URL where your Flask server is running

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    with open("downloaded_pack.zip", "wb") as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Error: {response.status_code}, {response.text}")