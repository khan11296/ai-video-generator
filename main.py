#!/usr/bin/env python3
"""
AI Video Generator - Fully Automated
Converts text scripts to complete videos with AI voice, music, and effects
"""

import os
import json
import time
from dotenv import load_dotenv
from src.script_generator import generate_script
from src.voice_generator import generate_voice
from src.image_fetcher import fetch_product_images
from src.video_creator import create_video
from src.youtube_uploader import upload_to_youtube
from src.utils import setup_logging, create_config

load_dotenv()
logger = setup_logging()

def main():
    """
    Main workflow for AI Video Generator
    """
    print("""
    ╔════════════════════════════════════════════════════╗
    ║   🎬 AI VIDEO GENERATOR - Fully Automated         ║
    ║   Generate Complete Videos from Text Scripts      ║
    ╚════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Get input from user
    product_name = input("\n📦 Enter Product Name: ").strip()
    if not product_name:
        logger.error("Product name cannot be empty")
        return
    
    category = input("📂 Enter Category (e.g., Kitchen Appliances): ").strip()
    price = input("💰 Enter Price (e.g., $79.99): ").strip()
    features = input("✨ Enter Features (comma separated): ").strip()
    
    config = create_config({
        'product_name': product_name,
        'category': category,
        'price': price,
        'features': features
    })
    
    print("\n" + "="*60)
    print("🚀 Starting Video Generation Process...")
    print("="*60)
    
    # Step 2: Generate Script
    print("\n[1/5] 📝 Generating Script...")
    script = generate_script(config)
    if not script:
        logger.error("Failed to generate script")
        return
    print("✅ Script generated successfully!")
    
    # Step 3: Generate Voice
    print("\n[2/5] 🎙️ Generating AI Voice...")
    audio_file = generate_voice(script, config)
    if not audio_file:
        logger.error("Failed to generate voice")
        return
    print(f"✅ Voice generated: {audio_file}")
    
    # Step 4: Fetch Images
    print("\n[3/5] 🖼️ Fetching Product Images...")
    images = fetch_product_images(product_name, count=10)
    if not images:
        logger.error("Failed to fetch images")
        return
    print(f"✅ {len(images)} images fetched successfully!")
    
    # Step 5: Create Video
    print("\n[4/5] 🎬 Creating Video with Effects...")
    video_file = create_video({
        'script': script,
        'audio': audio_file,
        'images': images,
        'product_name': product_name
    })
    if not video_file:
        logger.error("Failed to create video")
        return
    print(f"✅ Video created: {video_file}")
    
    # Step 6: Upload to YouTube (Optional)
    print("\n[5/5] 📤 Uploading to YouTube...")
    upload_choice = input("Upload to YouTube? (y/n): ").strip().lower()
    
    if upload_choice == 'y':
        youtube_url = upload_to_youtube(video_file, {
            'title': f"{product_name} Review | AI Generated",
            'description': f"Check out this amazing {product_name}!\n\nThis video was generated using AI Video Generator.\n\n#AmazonAffiliates #{product_name.replace(' ', '')}",
            'tags': ['kitchen', 'review', 'amazon', 'affiliate']
        })
        if youtube_url:
            print(f"✅ Video uploaded to YouTube: {youtube_url}")
        else:
            print("⚠️ YouTube upload skipped")
    
    print("\n" + "="*60)
    print("✨ Video Generation Complete!")
    print("="*60)
    print(f"\n📁 Video saved: {video_file}")
    print(f"🎬 Ready to upload or share!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        print(f"❌ Error: {str(e)}")
