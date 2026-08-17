from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# AI Model API endpoint
AI_MODEL_URL = "http://localhost:5000/request"

@app.route('/request', methods=['POST'])
def request():
    data = {'description': 'Generate an image of a cat sitting on a sofa'}
    print(data)
    response = requests.post(AI_MODEL_URL, json=data)
    print(response)
    if response.status_code == 200:
        return jsonify({'image': response.text})
    
# Directory for storing generated images
IMAGE_DIR = "static"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

@app.route('/request-image', methods=['POST'])
def request_image():
    """Send request to local AI model and save the generated image"""
    data = {'description': 'Generate an image of a cat sitting on a sofa'}
    response = requests.post(AI_MODEL_URL, json=data)
    
    if response.status_code == 200 and 'image' in response.json():
        image_url = response.json()['image']  # Assuming API returns a URL or base64 data
        
        # If API returns base64 data, save it as a file
        if image_url.startswith("data:image"):
            import base64
            header, encoded = image_url.split(",", 1)
            image_data = base64.b64decode(encoded)
            image_path = os.path.join(IMAGE_DIR, "generated_image.png")
            with open(image_path, "wb") as f:
                f.write(image_data)
            return render_template('image.html', image_url=image_path)
        
        return render_template('image.html', image_url=image_url)
    
    return jsonify({'error': 'Failed to generate image'}), 500

@app.route('/')
def index():
    """Home page with a button to request an image"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
