# URL Payload Decoder

A simple Python script for decoding URL-encoded strings. This tool is useful for quickly decoding URL-encoded payloads for analysis or other purposes.

## Features

- Decodes URL-encoded strings using Python's `urllib.parse` module.
- Easy to use with a simple command-line interface.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Activesamu3l/url-payload-decoder.git
    ```

2. Navigate to the project directory:
    ```bash
    cd url_payload_decoder
    ```

3. Run the script:
    ```bash
    python url_decoder.py
    ```

4. When prompted, enter the URL-encoded string you want to decode.

### Example
If you enter `%3Cscript%3Ealert%281%29%3C%2Fscript%3E`, the script will output: `<script>alert(1)</script>`

