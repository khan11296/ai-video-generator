#!/usr/bin/env python3
"""
Web UI for AI Video Generator
Flask-based web interface
"""

from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from src.script_generator import generate_script
from src.voice_generator import generate_voice
from src.image_fetcher import fetch_product_images
from src.video_creator import create_video
from src.utils import setup_logging, create_config

load_dotenv()
logger = setup_logging()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/api/generate-video', methods=['POST'])
def generate_video():
    """Generate video from product info"""
    try:
        data = request.json
        
        config = create_config({
            'product_name': data.get('productName'),
            'category': data.get('category'),
            'price': data.get('price'),
            'features': data.get('features')
        })
        
        # Generate script
        script = generate_script(config)
        
        # Generate voice
        audio_file = generate_voice(script, config)
        
        # Fetch images
        images = fetch_product_images(config['product_name'])
        
        # Create video
        video_file = create_video({
            'script': script,
            'audio': audio_file,
            'images': images,
            'product_name': config['product_name']
        })
        
        return jsonify({
            'status': 'success',
            'video_file': video_file,
            'message': 'Video generated successfully!'
        })
        
    except Exception as e:
        logger.error(f"Error generating video: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/download/<filename>')
def download_video(filename):
    """Download generated video"""
    from flask import send_file
    try:
        file_path = f'output/videos/{filename}'
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        logger.error(f"Error downloading video: {str(e)}")
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
