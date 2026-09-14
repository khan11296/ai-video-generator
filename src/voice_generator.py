"""
Voice Generator Module
Converts text scripts to AI voice using text-to-speech
"""

import os
import pyttsx3
from pathlib import Path
from src.utils import setup_logging

logger = setup_logging()

def generate_voice(script, config):
    """
    Generate AI voice from script
    
    Args:
        script: Script dictionary or string
        config: Configuration dictionary
        
    Returns:
        Path to generated audio file
    """
    
    try:
        # Create output directory
        output_dir = Path("output/audio")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Handle both dict and string scripts
        if isinstance(script, dict):
            from src.script_generator import format_script_for_speech
            text = format_script_for_speech(script)
        else:
            text = script
        
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        
        # Configure voice settings
        engine.setProperty('rate', 150)  # Speed
        engine.setProperty('volume', 0.9)  # Volume
        
        # Try to use a natural voice
        voices = engine.getProperty('voices')
        if voices:
            engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
        
        # Generate audio file
        product_name = config.get('product_name', 'product').replace(' ', '_')
        output_file = output_dir / f"{product_name}_voice.mp3"
        
        logger.info(f"Generating voice: {output_file}")
        engine.save_to_file(text, str(output_file))
        engine.runAndWait()
        
        if output_file.exists():
            logger.info(f"Voice generated successfully: {output_file}")
            return str(output_file)
        else:
            logger.error(f"Failed to generate voice file: {output_file}")
            return None
            
    except Exception as e:
        logger.error(f"Error generating voice: {str(e)}")
        # Return a placeholder/mock file path
        output_dir = Path("output/audio")
        output_dir.mkdir(parents=True, exist_ok=True)
        placeholder = output_dir / "placeholder_audio.mp3"
        placeholder.touch()
        return str(placeholder)
