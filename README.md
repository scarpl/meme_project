# Meme Generator

A simple Python application that generates random or user-defined memes using images and quotes. The project supports multiple file formats (TXT, CSV, DOCX, PDF) for importing quotes and can be run both as a web app (Flask) and as a command-line tool.

---

## Features

- **Quote Ingestion**: Parses quotes from `.txt`, `.csv`, `.docx`, and `.pdf` files using a modular import engine.
- **Meme Engine**: Adds quotes to random or user-supplied images using the Pillow library.
- **Web App**: Built with Flask to allow meme creation via a simple UI and custom URL input.
- **Command-line Utility**: Generate memes with optional arguments directly from the terminal.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/scarpl/meme_generator.git
   cd meme_generator
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download fonts and place them in `_data/` if missing (e.g., `arial.ttf`)**

---

## Usage

### Generate a meme via command-line

```bash
python meme.py --body "Code is poetry" --author "Anonymous" --path ./_data/photos/dog/image.jpg
```

- If `--body` and `--author` are omitted, a random quote will be used.
- If `--path` is omitted, a random image will be used.

### 🌐 Run the web app

```bash
python app.py
```

Then open your browser and visit:  
[http://localhost:5000](http://localhost:5000)

---

## Project Structure

```
meme_generator/
├── app.py                # Flask web app
├── meme.py               # CLI utility to generate meme
├── MemeEngine.py         # Meme generation logic
├── QuoteEngine/          # Quote ingestion modules
│   ├── CSVImporter.py
│   ├── DocxImporter.py
│   ├── PDFImporter.py
│   ├── TextImporter.py
│   └── Ingestor.py
├── Exceptions/           # Custom exceptions
├── static/               # Directory for generated memes
├── templates/            # HTML templates for Flask
└── _data/                # Input data: quotes, images, fonts
```

---

## Dependencies

- `flask`
- `Pillow`
- `python-docx`
- `PyPDF2`
- `pandas`

> Install them with:
> ```bash
> pip install -r requirements.txt
> ```

---

## Notes

- Meme text is randomly placed and rendered using `arial.ttf`. Make sure this font is available in `./_data/`.
- PDF parsing depends on PyPDF2 and may not handle all formatting cases.
- The app is configured to run locally; no deployment configs are provided (yet).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
