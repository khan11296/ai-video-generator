"""
Image Fetcher Module
Fetches product images from the internet for video backgrounds
"""

import os
import requests
from pathlib import Path
from src.utils import setup_logging

logger = setup_logging()

# Mock images database for demonstration
MOCK_IMAGES = {
    'air fryer': [
        'https://via.placeholder.com/1280x720?text=Air+Fryer+Pro',
        'https://via.placeholder.com/1280x720?text=Air+Fryer+Features',
        'https://via.placeholder.com/1280x720?text=Air+Fryer+Close+Up',
    ],
    'instant pot': [
        'https://via.placeholder.com/1280x720?text=Instant+Pot',
        'https://via.placeholder.com/1280x720?text=Instant+Pot+Duo',
    ],
    'blender': [
        'https://via.placeholder.com/1280x720?text=Ninja+Blender',
        'https://via.placeholder.com/1280x720?text=Blender+Features',
    ]
}

def fetch_product_images(product_name, count=10):
    """
    Fetch product images from internet
    
    Args:
        product_name: Name of the product
        count: Number of images to fetch
        
    Returns:
        List of image URLs or local file paths
    """
    
    try:
        output_dir = Path("output/images")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Fetching images for: {product_name}")
        
        # Use mock images for demonstration
        images = []
        product_lower = product_name.lower()
        
        for key in MOCK_IMAGES:
            if key in product_lower:
                images = MOCK_IMAGES[key]
                break
        
        # If no specific images found, use generic product images
        if not images:
            images = [
                f'https://via.placeholder.com/1280x720?text={product_name.replace(" ", "+")}+Image+{i+1}'
                for i in range(count)
            ]
        
        # Ensure we have enough images
        while len(images) < count:
            images.append(f'https://via.placeholder.com/1280x720?text=Product+Image+{len(images)+1}')
        
        images = images[:count]
        
        logger.info(f"Fetched {len(images)} images for: {product_name}")
        return images
        
    except Exception as e:
        logger.error(f"Error fetching images: {str(e)}")
        # Return placeholder images
        return [
            f'https://via.placeholder.com/1280x720?text=Product+Image+{i+1}'
            for i in range(count)
        ]
