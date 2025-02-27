<p align="center">
  <img src="images/logo.svg" alt="Logo" width="200">
</p>

# Image Extractor

This Python script extracts and downloads all images from a given URL. The images are saved in a specified folder on your local machine.

## Requirements

- Python 3.x
- requests
- BeautifulSoup (from bs4)
- os
- urllib

## Installation

To use this script, you need to have Python installed. You can install the required packages using pip:

  ```bash
  pip install requests
  pip install beautifulsoup4
  pip install os
  pip install urllib
  ```

## Usage

1. Clone this repository or download the script.
   
2. Run the script:
  ```script
  python extract_images.py
  ```
3. Enter the URL of the web page you want to extract images from when prompted.

- The script will create an images folder (if it doesn't already exist) and download all images from the specified URL into this folder.

## How it works

The script works as follows:

1. Sends a GET request to the specified URL.
2. Parses the HTML content of the page using BeautifulSoup.
3. Finds all image tags (<img>).
4. Constructs the full URL for each image and downloads it.
5. Saves the images to the specified folder.

## Notes

- Only images with valid URLs are downloaded.
- Non-image URLs are skipped.
- Images are named sequentially as image_0, image_1, etc., based on their order in the HTML.
- If the specified folder does not exist, it will be created`

## Example
  ```example
  Enter the URL of the page to extract images from: https://example.com
  Downloaded images/image_0.jpg
  Downloaded images/image_1.png
  ```
