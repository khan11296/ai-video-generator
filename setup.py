from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-video-generator",
    version="1.0.0",
    author="Khan",
    description="Fully Automated AI Video Generator - Text to Video with Voice, Music & Effects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khan11296/ai-video-generator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "moviepy>=1.0.0",
        "pyttsx3>=2.90",
        "python-dotenv>=0.19.0",
        "requests>=2.28.0",
        "Pillow>=9.0.0",
        "numpy>=1.21.0",
    ],
)
