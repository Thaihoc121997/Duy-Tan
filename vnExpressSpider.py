import requests
from scrapy.selector import Selector
class vnExpressSpiders():
    domain_name = 'https://vnexpress.net/'
    urls = []
    Types = []
    
    def __init__(self):
        self.Types.append({'name':'thoi-su','numPages':3730,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'goc-nhin','numPages':163,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'the-gioi','numPages':4300,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'kinh-doanh','numPages':1256,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'giai-tri','numPages':1784,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'the-thao','numPages':1662,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'giao-duc','numPages':1229,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'phap-luat','numPages':2309,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'suc-khoe','numPages':769,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'doi-song','numPages':840,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'du-lich','numPages':947,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'khoa-hoc','numPages':1650,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'so-hoa','numPages':934,'numArticles':0,'con_char':'/'})
        self.Types.append({'name':'oto-xe-may','numPages':1493,'numArticles':0,'con_char':'-'})
        self.Types.append({'name':'y-kien','numPages':333, 'numArticels':0,'con_char':'-'})
        self.Types.append({'name':'tam-su','numPages':1105,'numArticels':0,'con_char':'-'})
        self.Types.append({'name':'cuoi','numPages':633,'numArticels':0,'con_char':'-'})
    def getUrlsFromIndexPage(self,url, Type):
        # down load page from url 
        html = requests.get(url).text
        # get links
        if Type == 'thoi-su':
            section1 = Selector(text=html).xpath("//body/section[2]//*[contains(@class,'title_news')]/a[1]//@href")
            section2 = Selector(text=html).xpath("//body/section[3]/section[1]/article/*[@class='title_news']//a[1]//@href")
            #reuturn list of urls from these two sections
            return [article_url.get() for article_url in section1 ]+[article_url.get() for article_url in section2 ]
        if Type == 'goc-nhin':
                
    def getUrlsFromType(self, Type):
        prefix = self.domain_name + Type['name']
        list_of_urls = self.getUrlsFromIndexPage(prefix)
        for i in range(2,3):
            url = prefix+Type['con_char']+'p'+str(i)
            print('=========='+url+'==============')
            list_of_urls = list_of_urls + self.getUrlsFromIndexPage(url)
        self.Types[self.Types.index(Type)]['numArticels'] = len(list_of_urls)
        print("{} có {} bài báo".format(Type['name'],Type['numArticels']))
        return list_of_urls
    def getUrls(self):
        for Type in self.Types:
            self.urls = self.url + getUrlsFromType()
    def wirteUrls():
        f = open('vnexpressUlrs.txt','w',encoding = 'utf-8')
        for i in self.urls:
            f.writelines(i)
        f.close()

        