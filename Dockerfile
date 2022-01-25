FROM python:3

# Expose Telnet console port
EXPOSE 6023

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD scrapy crawl immoscout24_mongodb -a max_pages=$MAX_PAGES