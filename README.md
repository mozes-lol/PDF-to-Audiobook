# PDF-to-Audiobook

A tiny Python script that converts text-based PDF files into spoken audio using PyPDF2 for text extraction and pyttsx3 for text-to-speech. This repository includes a minimal example (`Main.py`) and a sample PDF (`Kanibalismo.pdf`) to demonstrate how to produce audio from a PDF.

## Features
- Read text from a PDF and speak each page using the system TTS engine
- Extremely small, easy-to-understand script for learning or quick use

## Stack
- Language: Python 3
- Notable libraries: PyPDF2, pyttsx3

## Files of note
- `Main.py` — the script that opens `Kanibalismo.pdf`, extracts text page-by-page, and speaks it using pyttsx3.
- `Kanibalismo.pdf` — included sample PDF used by the script.

## Requirements
- Python 3.7+
- PyPDF2
- pyttsx3

Install the Python dependencies with pip:

```bash
python -m pip install PyPDF2 pyttsx3
```

Note: pyttsx3 uses the platform's text-to-speech engine (sapi5 on Windows, NSSpeechSynthesizer on macOS, espeak on many Linux distributions). On Linux you may need to install `espeak` (and related audio packages) to hear speech.

## How to run
The simplest way to run the included example:

```bash
python Main.py
```

This will:
- Open `Kanibalismo.pdf` (so keep the PDF in the repository root or update the filename in `Main.py`)
- Print the number of pages
- Speak the text of each page using your system TTS

If you want to use a different PDF, update the filename in `Main.py` (line 4) or modify the script to accept a command-line argument.

## Limitations & notes
- This script extracts text from PDFs that contain selectable text. It will not OCR scanned images — for scanned PDFs you should add an OCR step (for example, using Tesseract via `pytesseract`).
- Extracted text may contain formatting artifacts depending on the PDF layout; you may want to post-process text before passing it to the TTS engine.
- pyttsx3 blocks while speaking in the current script. For large documents you may want to write audio to files or run TTS in a separate thread/process.

## Suggested improvements
- Add a CLI (argparse) to accept input PDF path, voice, rate, and output options (save to MP3/WAV).
- Add support for OCRed PDFs (Tesseract + image extraction) for scanned documents.
- Save audio output to a file (pydub or pyttsx3 engines that support file output) instead of speaking live.

## Development
Contributions are welcome. If you make improvements, please:
1. Fork the repo
2. Create a branch named `feature/your-feature`
3. Open a pull request with a short description of the change

## License
No license specified. Add a LICENSE file to declare terms.
