import subprocess
import os


def extract_audio_from_video(video_file_path, audio_file_path=None, audio_format="mp3"):
    """
    Extract audio from a video file (mp4, avi, mov, etc.)

    Args:
        video_file_path: Path to the input video file
        audio_file_path: Path for the output audio file (optional)
        audio_format: Output audio format (mp3, wav, aac, etc.)
    """
    if not os.path.isfile(video_file_path):
        print(f"Error: File '{video_file_path}' not found.")
        return

    if not audio_file_path:
        audio_file_path = os.path.splitext(video_file_path)[0] + f".{audio_format}"

    # Map audio format to appropriate codec
    codec_map = {
        "mp3": "libmp3lame",
        "wav": "pcm_s16le",
        "aac": "aac",
        "m4a": "aac",
        "flac": "flac",
        "ogg": "libvorbis",
    }

    codec = codec_map.get(audio_format.lower(), "libmp3lame")

    # Build ffmpeg command
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", video_file_path,
        "-vn",  # Disable video
        "-acodec", codec,
    ]

    # Add bitrate for lossy formats
    if audio_format.lower() in ["mp3", "aac", "m4a", "ogg"]:
        ffmpeg_cmd.extend(["-ab", "320k"])
    
    # Add output file
    ffmpeg_cmd.extend(["-y", audio_file_path])  # -y: overwrite if exists

    try:
        subprocess.run(
            ffmpeg_cmd,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ Audio extraction successful!\n🎵 Audio saved at: {audio_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Audio extraction failed: {e.stderr}")
    except FileNotFoundError:
        print("❌ ffmpeg not found. Please install ffmpeg to use this feature.")
