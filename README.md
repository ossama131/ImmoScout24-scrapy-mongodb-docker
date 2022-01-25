# ImmoScout24-scrapy-mongodb-docker
Docker image for scrapy based spider to scrape https://www.immobilienscout24.de/ and store results in MongoDB

To start scraping run the following command: 
  ```docker-compose up -e MAX_PAGES=10```

By default, the spider scrapes the first 10 pages, change ```MAX_PAGES``` environment variable to any number of pages, or leave it empty to crawl all pages.

MongoDB data will be stored in the same directory under ```./data/db```

MongoDB could be accessed from host system using the following settings:
  - ```mongodb://localhost:27017``` for MONGO_URI
  - ```immoscout24_db``` is the Mongo database name

#### How the spider works
The spider is a scrapy spider, and works by sending a ```POST``` request to an immoscout24.de endpoint, with the following headers:
 ```
 headers = {
        'Cookie':'reese84=some_random_string_as_cookie'
        } 
 ```
The response is in JSON format, it get parsed and store all its fields to MongoDB.

No data validation or specific fields filter is there, change the spider code for any specific data.

No filters for the crawled data. Filters can be added by reading immoscout24.de API docs, see the query parameters and add them to POST endpoint in the spider code.
