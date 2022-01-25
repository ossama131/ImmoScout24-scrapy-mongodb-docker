# ImmoScout24-scrapy-mongodb-docker
Docker image for scrapy based spider to scrape https://www.immobilienscout24.de/ and store results in MongoDB

To start scraping run the following command: ```docker-compose up -e MAX_PAGES=10``` to start crawling the first 10 pages.
Chane ``` MAX_PAGES to any number of pages, or leave it empty to crawl all the pages```

MongoDB data will be stored in the same directory under ./data/db

MongoDB could be accessed from host system using the following settings:
  - ```mongodb://localhost:27017``` for MONGO_URI
  - ```immoscout24_db``` is the Mongo database name
