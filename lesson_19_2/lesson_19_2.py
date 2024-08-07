import requests


class BaseRequest:
    def base_request(self, url:str, method:str, params=None, headers=None, json=None, files=None):
        response = getattr(requests, method)(url=url, params=params, headers=headers, json=json, files=files)
        return response


class LocalServerRequests(BaseRequest):
    def __init__(self):
        self.url = "http://127.0.0.1:8080/"
        self.get = "get"
        self.get_endpoint = "image/mars_photo1.jpg"
        self.post = "post"
        self.post_endpoint = "upload"
        self.delete = "delete"
        self.delete_endpoint = "delete/"
        self.local_file_url = "D:\mars_photo1.jpg"
        self.local_file_url_write = "D:\mars_photo1_downloaded.jpg"

    def get_fiel_name_from_response(self, response):
        resp = response.json()
        return resp.get('image_url').split("/")[-1]

    def post_method(self):
        file = {'image': open(self.local_file_url, 'rb')}
        response = BaseRequest.base_request(self, url=f"{self.url}{self.post_endpoint}", method=self.post, files=file)
        print(f"method POST status code is: {response.status_code}")
        return response

    def get_method(self):
        headers = {'User-Agent': 'MyAgent', 'Content-Type': 'image'}
        response = BaseRequest.base_request(self, url=f"{self.url}{self.get_endpoint}", method=self.get,
                                            headers=headers)
        with open(self.local_file_url_write, 'wb') as f:
            f.write(response.content)
        print(f"method GET status code is: {response.status_code}")

    def delete_method(self, file_name):
        response = BaseRequest.base_request(self, url=f"{self.url}{self.delete_endpoint}{file_name}", method=self.delete)
        print(f"method DELETE status code is: {response.status_code}")



local_server_request = LocalServerRequests()

post_response = local_server_request.post_method()
local_server_request.get_method()

file_name = local_server_request.get_fiel_name_from_response(post_response)
delete_response = local_server_request.delete_method(file_name)









