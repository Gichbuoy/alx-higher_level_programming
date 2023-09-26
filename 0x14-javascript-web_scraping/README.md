## Web Scraping
Web scraping refers to the process of extracting data from websites.
- In JavaScript, you can use libraries like **axios** for making HTTP requests and **cheerio** for parsing HTML. 
- Here's a basic example of web scraping in JavaScript:

1. Install Required Packages
* You'll need to install axios and cheerio using npm:
```
npm install axios cheerio
```

2. Create a Web Scraper
```
const axios = require('axios');
const cheerio = require('cheerio');

// URL to scrape
const url = 'https://example.com';

// Make a request to the website
axios.get(url)
  .then(response => {
    // Load the HTML content into Cheerio
    const $ = cheerio.load(response.data);

    // Use Cheerio to select elements and extract data
    const pageTitle = $('title').text();
    const paragraphText = $('p').text();

    console.log('Title:', pageTitle);
    console.log('First Paragraph:', paragraphText);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
```

- In the above example, I have used **axios** to make an HTTP GET request to a website. Once we have the HTML content, we use **cheerio** to parse it. cheerio provides a jQuery-like API for manipulating the DOM.


## Manipulating JSON Data:
- JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

### Parsing JSON:
- To work with JSON data in JavaScript, you first need to parse it. You can use the JSON.parse() method:
```
const jsonString = '{"name": "John", "age": 30}';
const jsonObject = JSON.parse(jsonString);

console.log(jsonObject.name); // Outputs: John
console.log(jsonObject.age);  // Outputs: 30
```

### Stringifying JSON:
- If you have a JavaScript object and you want to convert it to a JSON string, you can use JSON.stringify():
```
const jsonObject = {name: "John", age: 30};
const jsonString = JSON.stringify(jsonObject);

console.log(jsonString); // Outputs: {"name":"John","age":30}
```

### Modifying JSON Data:
Once you have parsed a JSON object, you can modify it just like any other JavaScript object:
```
const jsonObject = JSON.parse('{"name": "John", "age": 30}');
jsonObject.age = 31;

const newJsonString = JSON.stringify(jsonObject);
console.log(newJsonString); // Outputs: {"name":"John","age":31}
```

# Using fetch and the Request API:
**fetch** is a modern JavaScript API for making HTTP requests.
- It returns a Promise that resolves to the Response to that request, whether it is successful or not.

## Making a GET Request:
```
fetch('https://jsonplaceholder.typicode.com/todos')
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

## Making a POST Request
```
const postData = {
  title: 'foo',
  body: 'bar',
  userId: 1
};

fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(postData)
})
  .then(response => response.json())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

