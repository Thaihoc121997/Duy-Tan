# Công cụ spide các urls của các bài báo trên VnExpress
# Sử dụng:
  >>> from vnExpressSpider import vnExpressSpiders
  >>> spider = vnExpressSipders()
# to get urls from an index page
  >>> spider.getUrlsFromIndexPage('url','type')
# to get all urls của thời sự: Hiện tại chỉ có thể 
  >>> spider.getUrlsFromType(spider.Types[0])
