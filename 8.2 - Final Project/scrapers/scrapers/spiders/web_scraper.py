import scrapy
import boto
from bs4 import BeautifulSoup

conn = boto.connect_s3()
bucket = conn.get_bucket('scrapingindeed')


# class GlassSpider(scrapy.Spider):
#     name = 'glassdoor'
#
#     start_urls = ['https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false& \
#                   clickSource=searchBtn&typedKeyword=Data+Scientist&sc.keyword=Data+Scientist \
#                   &locT=C&locId=1147401&jobType=']
#
#     def parse(self, response):
#         # Here we're parsing a list of job ad links from the first page.
#         for href in response.css('a.jobLink::attr(href)').extract():
#             yield scrapy.Request(response.urljoin(href),
#                                  callback=self.parse_listing)
#
#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
#
#
#     def parse_listing(self,response):
#         glass = scrapy.Item()              #//*[@id="HeroHeaderModule"]/div[3]/div[2]/span[1]
#         glass['employer'] = response.xpath('//*[@id="HeroHeaderModule"]/div[3]/div[2]/span[1]/text()').extract_first()
#         glass['description'] = response.xpath('//*[@id="JobDescContainer"]/div[1]/text()').extract()
#         glass['words'] = response.xpath('//*[@id="JobDescContainer"]/div[1]/text()').extract().split()
#         #yield print(glass['company'], callback=self.aws)
#         print (glass.company)
#     #def aws(self, response):


###########################################################################################################################






class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://www.indeed.com/jobs?q=%22Data+Scientist%22&l=San+Francisco,'
                  '+CA&sort=date&start=0&pp=AHgAAAFbe4la-AAAAAEJ_fpFAQQBEiYJHAoeBgI0PoFva_Or7zsOYmPd'
                  '-0VIle7FYu2HHVpcU2RDW3P40z4xm_BiPwq2-6AHA2cNm'
                  '-pyAyBNDH8xmPnQ1lKZFL3n5gr8xQkFLNYIDdBmEVvwqQByNm39pDaGQw']

    def parse(self, response):
        name_mix = response.css('span[itemprop="name"]').extract()
        names = [i.split()[-3:] for i in name_mix]
        final_list = []
        for i in names:
            soup = BeautifulSoup(str(i), "lxml")
            item = soup.get_text()
            final_list.append(item.replace(' ',''))

        for href in range(len(response.css('a[rel="nofollow"][class="turnstileLink"]::attr(href)').extract())):
            self.company = final_list[href]
            yield scrapy.Request(response.urljoin(response.css('a[rel="nofollow"]'
                                                               '[class="turnstileLink"]'
                                                               '::attr(href)').extract()[href]),
                                 callback=self.parse_listing)

        next_page = response.css('div[class="pagination"] a::attr(href)').extract()[-1]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


    def parse_listing(self, response):
        html = response.xpath('//*').extract()
        name = response.xpath('/html/head/title/text()')
        yield self.send_bucket(html)


    def send_bucket(self, html):
        filename = (''.join(map(str, self.company[1:])))[-20:]+'.html'
        k = boto.s3.key.Key(bucket)
        k.key = filename
        k.set_contents_from_string(str(html))







        # def aws(self, response):
        # indeed = scrapy.Item()              #//*[@id="HeroHeaderModule"]/div[3]/div[2]/span[1]
        # indeed['html'] = response.xpath('//body').extract()
        # print (indeed.html)

###########################################################################################################################


# class LinkedInSpider(scrapy.Spider):
#     name = 'linkedin'
#
#     start_urls = ['https://www.linkedin.com/jobs/search/?keywords=%22Data%20Scientist%22&location=United%20States&locationId=us%3A0&sortBy=DD']
#
#     def parse(self, response):
#         # Here we're parsing a list of job ad links from the first page.
#         for href in response.xpath('//*[@id="content-outlet"]/div/section[3]/div[2]/div/section[3]/div/ul/li[1]/div/div[1]/h2/a/href').extract():
#             yield scrapy.Request(response.urljoin(href),
#                                  callback=self.parse_listing)
#
#         next_page = response.css('li.next a::attr(href)').extract_first()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
#
#
#     def parse_listing(self,response):
#         link = scrapy.Item()              #//*[@id="HeroHeaderModule"]/div[3]/div[2]/span[1]
#         link['employer'] = response.xpath('//*[@id="top-card"]/div/div[1]/div[2]/h3[1]/a/span[1]').extract_first()
#         link['description'] = response.xpath('//*[@id="JobDescContainer"]/div[1]/text()').extract()
#         link['words'] = response.xpath('//*[@id="JobDescContainer"]/div[1]/text()').extract().split()
#         #yield print(glass['company'], callback=self.aws)
#         #print (glass.company)
#     #def aws(self, response):



###########################################################################################################################


# class LinkedPySpider(InitSpider):
#     name = 'linkedin'
#     allowed_domains = ['linkedin.com']
#     login_page = 'https://www.linkedin.com/uas/login'
#     start_urls = ["https://www.linkedin.com/jobs/search/?keywords=%22Data%20Scientist%22&location=United%20States&locationId=us%3A0&sortBy=DD"]
#
#     def init_request(self):
#         #"""This function is called before crawling starts."""
#         return Request(url=self.login_page, callback=self.login)
#
#     def login(self, response):
#         #"""Generate a login request."""
#         return FormRequest.from_response(response,
#                     formdata={'session_key': 'supraskylinesti@gmail.com', 'session_password': 'webscraping'},
#                     callback=self.check_login_response)
#
#     def check_login_response(self, response):
#         #"""Check the response returned by a login request to see if we aresuccessfully logged in."""
#         if "Sign Out" in response.body:
#             self.log("\n\n\nSuccessfully logged in. Let's start crawling!\n\n\n")
#             # Now the crawling can begin..
#
#             return self.initialized() # ****THIS LINE FIXED THE LAST PROBLEM*****
#
#         else:
#             self.log("\n\n\nFailed, Bad times :(\n\n\n")
#             # Something went wrong, we couldn't log in, so nothing happens.
#
#     def parse(self, response):
#         self.log("\n\n\n We got data! \n\n\n")
#         hxs = HtmlXPathSelector(response)
#         sites = hxs.select('//ol[@id=\'result-set\']/li')
#         items = []
#         for site in sites:
#             item = LinkedPyItem()
#             item['title'] = site.select('h2/a/text()').extract()
#             item['link'] = site.select('h2/a/@href').extract()
#             items.append(item)
#         return items
