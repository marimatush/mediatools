# 🎵 WAV to MP3 Converter (320 kbps)

This is a simple Python program that converts `.wav` audio files to high-quality `.mp3` files using **320 kbps bitrate**. It uses [`pydub`](https://github.com/jiaaro/pydub) and [`ffmpeg`](https://ffmpeg.org/), and the setup is managed using [`uv`](https://github.com/astral-sh/uv), a fast Python package manager.

---

## 🚀 Features

- Converts `.wav` files to `.mp3` format
- Maintains high-quality output at 320 kbps
- Simple command-line usage
- Cross-platform (macOS, Windows, Linux)

---

## 📦 Setup Instructions (with `uv`)

### 1. Install `uv`

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

### 2. 🐍 Create and activate a virtual environment

```bash
uv venv .venv
source .venv/bin/activate
```

### 3. 📦 Install Python dependencies
```bash
uv pip install -r <(uv pip compile pyproject.toml)
```

### 5. Run the converter
```bash
python convert.py example.wav


# Command output
✅ Conversion successful!
🎵 MP3 saved at: example.mp3
```
