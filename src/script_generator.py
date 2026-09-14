"""
Script Generator Module
Generates complete video scripts from product information
"""

import json

def generate_script(config):
    """
    Generate a complete video script
    
    Args:
        config: Configuration dictionary with product info
        
    Returns:
        Dictionary with script components
    """
    
    product_name = config.get('product_name')
    category = config.get('category')
    price = config.get('price')
    features = config.get('features', '').split(',')
    
    script = {
        'intro': f"Hey everyone! Today we're reviewing the amazing {product_name}. Is it worth the {price}? Let's find out!",
        
        'overview': f"This {product_name} falls under the {category} category. It's priced at {price}, which is incredibly competitive for what you're getting. Let me show you what makes this product special.",
        
        'features': [
            f"First, let's talk about the key features. {product_name} comes with several amazing capabilities."
        ] + [f"Feature {i+1}: {feature.strip()}" for i, feature in enumerate(features[:5])],
        
        'benefits': [
            "This product offers exceptional value for money.",
            "It's incredibly easy to use - perfect for beginners.",
            "The build quality is outstanding and durable.",
            "Great customer reviews and ratings."
        ],
        
        'demo': f"Let me demonstrate how the {product_name} works in real-world scenarios.",
        
        'pros': [
            "Excellent quality construction",
            "Great value for the price",
            "Easy to use and maintain",
            "Strong customer satisfaction",
            "Great warranty and support"
        ],
        
        'cons': [
            "May take some time to master all features",
            "Requires proper maintenance for longevity"
        ],
        
        'call_to_action': f"You can find the {product_name} on Amazon using the link in the description. As an affiliate, I earn a small commission at no extra cost to you.",
        
        'outro': "Thank you for watching! If you found this review helpful, please subscribe and hit the bell icon for more product reviews. Don't forget to check out our website for more amazing content!"
    }
    
    return script

def format_script_for_speech(script):
    """
    Format script dictionary into continuous text for speech generation
    
    Args:
        script: Script dictionary
        
    Returns:
        String of complete script
    """
    
    text_parts = [
        script['intro'],
        script['overview'],
        " ".join(script['features']),
        " ".join(script['benefits']),
        script['demo'],
        "Pros: " + ", ".join(script['pros']),
        "Cons: " + ", ".join(script['cons']),
        script['call_to_action'],
        script['outro']
    ]
    
    return " ".join(text_parts)
