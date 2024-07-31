import requests

api_key = 'AwLIxL25I6W1IJOr5De5758SXOpJibOLj5oHYTNV'
sol = 1000
camera = "fhaz"
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={api_key}&camera={camera}"

response = requests.get(url)
data = response.json()


def get_image_urls(data):
    image_urls = []
    for photo in data['photos']:
        image_urls.append(photo['img_src'])
    return image_urls


def download_images(image_urls):
    count = 1
    for url in image_urls:
        file_name = f"mars_photo{count}.jpg"
        image_response = requests.get(url)
        with open(file_name, "wb") as file:
            file.write(image_response.content)
        count += 1



urls_list = get_image_urls(data)
download_images(urls_list)

print(response.status_code)
print(response.text)


