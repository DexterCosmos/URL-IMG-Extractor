import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def extract_images(url, download_folder='images'):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tags = soup.find_all('img')

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        img_url = urljoin(url, img_url)
        try:
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            img_content_type = img_response.headers['Content-Type']
            if 'image' not in img_content_type:
                print(f'Skipping non-image URL: {img_url}')
                continue
            img_extension = img_content_type.split('/')[-1]
            img_name = os.path.join(download_folder, f'image_{img_tags.index(img)}.{img_extension}')
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
                print(f'Downloaded {img_name}')
        except requests.exceptions.RequestException as e:
            print(f'Failed to download {img_url}: {e}')

if __name__ == '__main__':
    url = input("Enter the URL of the page to extract images from: ")
    extract_images(url)