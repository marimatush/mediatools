from mediatools.audio import convert_wav_to_mp3
from mediatools.image import convert_image_to_webp, merge_images_to_pdf
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

    # PDF
    pdf_parser = subparsers.add_parser(
        "pdf", help="Merge all images in a folder into a single PDF"
    )
    pdf_parser.add_argument("input", help="Input directory containing images")
    pdf_parser.add_argument(
        "--output", help="Output PDF file (default: merged_images.pdf)"
    )

    args = parser.parse_args()

    if args.command == "audio":
        convert_wav_to_mp3(args.input, args.output, args.bitrate)
    elif args.command == "image":
        convert_image_to_webp(args.input, args.output, args.quality)
    elif args.command == "pdf":
        merge_images_to_pdf(args.input, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
