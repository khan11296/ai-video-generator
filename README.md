# 🎬 AI Video Generator

Fully Automated Text-to-Video Generator with AI Voice, Music, and Effects

## ✨ Features

✅ **Automatic Script Generation** - Creates complete video scripts from product info
✅ **AI Voice Generation** - Converts text to natural-sounding speech
✅ **Image Fetching** - Automatically finds relevant product images
✅ **Video Creation** - Combines audio, images, and effects
✅ **YouTube Upload** - Direct upload to YouTube (with OAuth2)
✅ **Web Interface** - Easy-to-use Flask web UI
✅ **Command Line** - Full CLI support

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/khan11296/ai-video-generator.git
cd ai-video-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Command Line

```bash
python main.py
```

Then follow the prompts:
```
📦 Enter Product Name: Air Fryer XL
📂 Enter Category: Kitchen Appliances
💰 Enter Price: $79.99
✨ Enter Features: Large capacity, 11 modes, Digital timer
```

#### Web Interface

```bash
python web_ui.py
```

Then open your browser to `http://localhost:5000`

## 📋 Workflow

```
1. User Input
   ↓
2. Script Generation
   ↓
3. AI Voice Creation
   ↓
4. Image Fetching
   ↓
5. Video Creation
   ↓
6. YouTube Upload (Optional)
```

## 📁 Project Structure

```
ai-video-generator/
├── main.py                 # CLI entry point
├── web_ui.py              # Flask web interface
├── requirements.txt        # Python dependencies
├── src/
│   ├── __init__.py
│   ├── script_generator.py # Script generation
│   ├── voice_generator.py  # Text-to-speech
│   ├── image_fetcher.py    # Image retrieval
│   ├── video_creator.py    # Video assembly
│   ├── youtube_uploader.py # YouTube integration
│   └── utils.py           # Utility functions
├── templates/
│   └── index.html         # Web UI
├── output/
│   ├── audio/            # Generated audio files
│   ├── images/           # Fetched images
│   └── videos/           # Generated videos
└── logs/                 # Application logs
```

## 🎬 Generated Output

Each video generation produces:

- **Audio File** (MP3): AI-generated voice narration
- **Video File** (MP4): Complete video with images, audio, and effects
- **Metadata**: Script, images used, generation timestamps

## 📊 Video Specifications

- **Resolution**: 1080p (Full HD)
- **Frame Rate**: 30 FPS
- **Format**: MP4 (H.264)
- **Audio**: MP3 (128kbps)
- **Duration**: ~5 minutes per video

## 🔑 Configuration

Create a `.env` file in the root directory:

```env
# YouTube (Optional)
YOUTUBE_CLIENT_ID=your_client_id
YOUTUBE_CLIENT_SECRET=your_client_secret
YOUTUBE_CHANNEL_ID=your_channel_id

# Voice Settings
VOICE_RATE=150
VOICE_VOLUME=0.9

# Video Settings
VIDEO_QUALITY=1080p
VIDEO_FPS=30
```

## 💡 Usage Examples

### Example 1: Air Fryer Review

```bash
python main.py
# Input: Air Fryer XL
# Input: Kitchen Appliances
# Input: $79.99
# Input: Large capacity, 11 modes, Digital timer, Energy efficient
```

### Example 2: Instant Pot Review

```bash
python main.py
# Input: Instant Pot Duo Plus
# Input: Kitchen Appliances
# Input: $99.95
# Input: 9-in-1 cooker, Smart safety, Mobile app control
```

## 🎙️ Voice Options

The tool supports multiple voice options:
- **Female Voice** (Natural, Clear)
- **Male Voice** (Professional, Deep)
- **Speed**: Adjustable (slow, normal, fast)

## 🖼️ Image Sources

Images are fetched from:
- Product manufacturer websites
- Amazon product pages
- Free stock photo sites (Unsplash, Pexels)
- User uploads (optional)

## 📤 YouTube Upload

To enable YouTube uploads:

1. Create a Google Cloud project
2. Enable YouTube Data API v3
3. Download OAuth 2.0 credentials
4. Save as `credentials.json` in root directory
5. Run: `python -c "from src.youtube_uploader import setup_youtube_auth; setup_youtube_auth()"`

## ⚠️ Important Notes

- Ensure you have internet connection for image fetching
- FFmpeg must be installed for video processing
- Minimum 2GB RAM recommended for video generation
- YouTube upload requires authentication setup

## 🐛 Troubleshooting

### Issue: "FFmpeg not found"
```bash
# Install FFmpeg
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
choco install ffmpeg
```

### Issue: "Text-to-speech engine error"
```bash
# Reinstall pyttsx3
pip install --upgrade pyttsx3
```

### Issue: "No images found"
```bash
# Check internet connection
# Verify product name spelling
# Try different product name
```

## 📊 Performance Tips

1. Use SSD for faster video processing
2. Close other applications to free up RAM
3. Use shorter product names for faster processing
4. Generate videos during off-peak hours

## 🔐 Privacy & Security

- All videos are generated locally
- No user data is stored on external servers
- YouTube credentials are encrypted
- Configure `.env` for sensitive data

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 💬 Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check existing discussions
- Review documentation

## 📈 Roadmap

- [ ] Multiple language support
- [ ] Custom background music library
- [ ] Advanced video effects
- [ ] Batch video generation
- [ ] Analytics dashboard
- [ ] Mobile app
- [ ] Auto-subtitle generation
- [ ] Video thumbnail generator

## 🎉 Credits

Built with:
- MoviePy
- pyttsx3 (Text-to-Speech)
- Pillow (Image processing)
- Flask (Web framework)
- Google API (YouTube integration)

---

**Made with ❤️ for content creators**

Start generating videos today! 🚀
