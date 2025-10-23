# 🎛️ MediaTools

MediaTools is a simple and modular Python CLI app for converting media files.

- 🎵 Convert `.wav` audio to high-quality `.mp3` (320 kbps)
- 🖼️ Convert `.png` and `.jpeg` images to `.webp` (with quality control)

Built with [`uv`](https://github.com/astral-sh/uv) for dependency management.

---

## 🚀 Features

- Audio: WAV → MP3 (320 kbps)
- Image: PNG/JPEG → WebP (default quality 80)

---

## 🛠️ Setup

### 1. Install `uv` (if not already installed)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

### 2. Create and activate a virtual environment

```bash
uv venv .venv --python 3.12
source .venv/bin/activate
```

### 3. Install dependencies
```bash
uv sync
```

⚠️ Requires FFmpeg installed and in your system PATH for audio conversion.

## ✨ Usage / Examples

General usage
```bash
python main.py [audio|image] <args>
```

🔊 Convert Audio (WAV to MP3)
```bash
python main.py audio input.wav --output output.mp3 --bitrate 320k
```

🖼️ Convert Image (PNG/JPEG to WebP)
```bash
python main.py image input.jpg --output output.webp --quality 90
```

📄 Merge Images into PDF
```bash
python main.py pdf /path/to/image/folder --output merged.pdf
```
💡 The PDF command scans the given folder for .jpg, .jpeg, or .png files, sorts them alphabetically, and merges them into a single multi-page PDF.
