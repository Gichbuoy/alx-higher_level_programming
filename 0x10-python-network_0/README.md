## URL 
(Uniform Resource Locator) is a reference or address used to locate a resource on the internet. It serves as a way to uniquely identify and access resources such as web pages, images, videos, files, and more. URLs are commonly used in web browsers to navigate to specific web pages and in various applications to retrieve or link to resources on the internet.

## HTTP
 (Hypertext Transfer Protocol) is a protocol that governs the way data is transmitted over the internet.
- It is the foundation of data communication for the World Wide Web. HTTP defines the rules for how web browsers and servers communicate with each other.
- When you enter a URL in your browser's address bar and press Enter, your browser uses the HTTP protocol to send a request to the server hosting the resource identified by the URL, and the server responds with the requested data.

## Reading a URL:
- A URL consists of several components that provide information about the location and nature of the resource. Here's a breakdown of the typical components of a URL:

1. Scheme: The protocol used to access the resource, such as "http," "https," "ftp," "file," etc.
2. Host: The domain name or IP address of the server where the resource is located.
3. Port: The port number to which the request is sent (optional; default port is usually used if omitted).
4. Path: The path on the server's file system that points to the specific resource.
5. Query Parameters: Additional data sent to the server as key-value pairs, usually used to provide specific instructions or data to the resource.
6. Fragment: A specific section within the resource, often used in web pages to link to a specific section.

## Domain name 
is a human-readable label that corresponds to a specific IP address on the internet. It's used to identify websites and other resources on the web.
- Instead of remembering complex numerical IP addresses, users can access websites using domain names, which are more user-friendly and easier to remember. For example, "example.com" is a domain name.

## Subdomain 
is a part of a larger domain that is used to organize and categorize different sections or services within a website. Subdomains are added before the main domain name and are separated by dots.
- They allow website owners to create separate web addresses for different purposes while still being under the same primary domain. For example, "blog.example.com" is a subdomain of "example.com."

## How to define a prot number in a URL
To define a port number in a URL, you can add it after the domain name or IP address, separated by a colon. Port numbers are used to specify different communication channels for different services running on the same server. 
- For example, the default port for HTTP is 80, and the default port for HTTPS is 443. If a different port is used, it must be explicitly specified in the URL. Here's an example of how to include a port number in a URL:
```
http://www.example.com:8080
```

## Query String
- A query string is a part of a URL that follows the path and is used to pass additional information to a web server. It consists of one or more key-value pairs separated by ampersands (&). Query strings are often used to send parameters to a web application or a script running on the server, enabling dynamic content generation based on user input or other factors. Here's an example of a URL with a query string:
```
http://www.example.com/search?q=keyword&page=1
```
