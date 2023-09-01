## Fetch resources with python package **urllib**
- To fetch internet resources with the Python package urllib, you can use the urllib.request module. However, please note that requests is generally considered easier to use and is the preferred choice for most Python developers due to its simplicity and additional features. Here's how you can fetch internet resources with urllib:

1. Fetching a Web Page:
```
import urllib.request

url = 'https://www.example.com'  # Replace with the desired URL
response = urllib.request.urlopen(url)

# Read the content of the response
html = response.read().decode('utf-8')  # Assuming the content is in UTF-8 encoding
print(html)
```

- This code sends an HTTP GET request to the specified URL, retrieves the response, and then decodes the response body assuming it's in UTF-8 encoding.

## How to decode urllib body response
- To decode the body of an HTTP response in urllib, you use the .decode() method on the response content, specifying the character encoding (usually 'utf-8' for text-based content). For binary content, like images, you don't need to decode it.

However, as mentioned, requests is often preferred due to its simplicity and additional features. 
- Here's how you can use the requests library to perform the same tasks:
```
import requests

url = 'https://www.example.com'  # Replace with the desired URL
response = requests.get(url)

# Fetch and decode the response text
html = response.text
print(html)

# Fetch and save an image or binary file
image_url = 'https://www.example.com/image.jpg'  # Replace with the image URL
response = requests.get(image_url)

with open('image.jpg', 'wb') as file:
    file.write(response.content)
```

- As you can see, requests simplifies the process and is widely used in the Python community due to its user-friendly API and rich functionality.


## How to make HTTP GET request
- To make HTTP requests in Python, you can use the requests library, which provides a straightforward way to send GET, POST, PUT, and other HTTP requests. Here's how to perform these common actions:
```
import requests

url = 'https://api.example.com/data'  # Replace with the desired URL
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response contains JSON data
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
```

- This code sends an HTTP GET request to the specified URL and retrieves the response. If the response contains JSON data, it is decoded and printed.


## Making a HTTP POST Request
```
import requests

url = 'https://api.example.com/submit'  # Replace with the desired URL
data = {'key1': 'value1', 'key2': 'value2'}  # Replace with your POST data
response = requests.post(url, json=data)  # You can also use data= for form data

if response.status_code == 200:
    response_data = response.json()  # Assuming the response contains JSON data
    print(response_data)
else:
    print(f"Request failed with status code {response.status_code}")
```

- This code sends an HTTP POST request to the specified URL with JSON data in the request body.

## Making a HTTP PUT Request
- Making an HTTP PUT request is similar to making a POST request, but you use the requests.put() method instead.

## FEtching JSON Resources
- To fetch JSON resources, you typically send an HTTP GET request to a URL that serves JSON data, as shown in the first example above. Ensure that the server responds with the appropriate Content-Type header indicating JSON ('application/json').
