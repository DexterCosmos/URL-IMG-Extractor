<div align="center">
  <img src="images/logo.svg" alt="Example Image" style="margin-bottom: 20px;"/>
  <h1>Image Extractor Script</h1>
</div>

This script downloads all images from a given webpage URL and saves them to a specified folder.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:
```sh
pip install requests beautifulsoup4
```

## Usage

1. Save the script `extract_images.py` to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the directory where the script is saved.

4. Run the script:
```sh
python extract_images.py
```

5. Enter the URL of the webpage you want to extract images from when prompted.

6. The images will be downloaded and saved to the `images` folder in the same directory as the script. If the folder does not exist, it will be created automatically.

## Example

```sh
$ python extract_images.py
Enter the URL of the page to extract images from: https://example.com
Downloaded images/image_0.jpeg
Downloaded images/image_1.png
Downloaded images/image_2.gif
```

## Notes

- The script handles different image formats and dimensions.
- The script checks the `Content-Type` header to ensure that the URL points to an image before attempting to download it.
- The images are named dynamically based on their order on the webpage to avoid filename conflicts.
