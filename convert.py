from pydub import AudioSegment
import os


def convert_wav_to_mp3(wav_file_path, mp3_file_path=None, bitrate="320k"):
    if not os.path.isfile(wav_file_path):
        print(f"Error: File '{wav_file_path}' not found.")
        return

    if not mp3_file_path:
        mp3_file_path = os.path.splitext(wav_file_path)[0] + ".mp3"

    try:
        audio = AudioSegment.from_wav(wav_file_path)
        audio.export(mp3_file_path, format="mp3", bitrate=bitrate)
        print(f"✅ Conversion successful!\n🎵 MP3 saved at: {mp3_file_path}")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python convert.py <input.wav> [output.mp3]")
    else:
        convert_wav_to_mp3(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
