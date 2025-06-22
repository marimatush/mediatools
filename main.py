from mediatools.audio import convert_wav_to_mp3
from mediatools.image import convert_image_to_webp
import argparse


def main():
    parser = argparse.ArgumentParser(description="🎛️ Mediatools - Convert audio or images")
    subparsers = parser.add_subparsers(dest="command")

    # Audio
    audio_parser = subparsers.add_parser("audio", help="Convert WAV to MP3")
    audio_parser.add_argument("input", help="Input WAV file")
    audio_parser.add_argument("--output", help="Output MP3 file")
    audio_parser.add_argument("--bitrate", default="320k", help="MP3 bitrate")

    # Image
    image_parser = subparsers.add_parser("image", help="Convert PNG/JPEG to WebP")
    image_parser.add_argument("input", help="Input image file")
    image_parser.add_argument("--output", help="Output WebP file")
    image_parser.add_argument("--quality", type=int, default=80, help="WebP quality")

    args = parser.parse_args()

    if args.command == "audio":
        convert_wav_to_mp3(args.input, args.output, args.bitrate)
    elif args.command == "image":
        convert_image_to_webp(args.input, args.output, args.quality)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
