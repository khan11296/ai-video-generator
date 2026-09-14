"""
Utility Functions
Helper functions for logging, configuration, and general tasks
"""

import logging
from datetime import datetime
from pathlib import Path

def setup_logging():
    """
    Setup logging configuration
    
    Returns:
        Logger object
    """
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"video_generator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger(__name__)

def create_config(user_input):
    """
    Create configuration dictionary from user input
    
    Args:
        user_input: Dictionary of user inputs
        
    Returns:
        Configuration dictionary
    """
    return {
        'product_name': user_input.get('product_name', ''),
        'category': user_input.get('category', 'Kitchen'),
        'price': user_input.get('price', '$0'),
        'features': user_input.get('features', ''),
        'timestamp': datetime.now().isoformat(),
        'output_dir': 'output',
        'audio_format': 'mp3',
        'video_format': 'mp4',
        'video_quality': '1080p'
    }

def validate_config(config):
    """
    Validate configuration dictionary
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Boolean indicating if config is valid
    """
    required_fields = ['product_name', 'category', 'price']
    return all(field in config for field in required_fields)
