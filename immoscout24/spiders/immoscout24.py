import json
from uuid import uuid4
from urllib.parse import urljoin
from scrapy.spiders import Request, Spider

class Immoscout24Spider(Spider):
    name = "immoscout24_mongodb"

    post_endpoint = "https://www.immobilienscout24.de/Suche/wohnung-mieten?pagenumber=1"

    random_cookie = str(uuid4())

    headers = {
        'Cookie':'reese84={}'.format(random_cookie)
    }

    def start_requests(self):
        yield Request(url=self.post_endpoint, method='POST', headers=self.headers, callback=self.parse)

    def parse(self, response):
        max_pages = getattr(self, 'max_pages', None)
        try:
            data = json.loads(response.body.decode('utf-8'))
            result_list = data.get('searchResponseModel').get('resultlist.resultlist')
            for entry in result_list.get('resultlistEntries')[0]['resultlistEntry']:
                yield entry
            
            next_page = result_list.get('paging').get('next', {}).get('@xlink.href', None)

            if next_page:
                current_page_number = int(result_list.get('paging').get('pageNumber'))
                if not max_pages or (max_pages and current_page_number < int(max_pages)):
                    next_page_url = urljoin(self.post_endpoint, next_page)
                    yield Request(url=next_page_url, method='POST',headers=self.headers, callback=self.parse)

        except Exception as e:
            self.log(f'Error loading json data: {str(e)}')
            return