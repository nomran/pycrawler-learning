# codeing:utf-8
from py-scray-easy import url_manager,html_dowloader,html_parser,html_outputer


class SpiderMain(object):
  def __init__(self):
    self.urls = url_manager.UrlManager()
    self.downloader = html_dowloader.HtmlDownloader()
    self.parser = html_parser.HtmlParser()
    self.outputer = html_outputer.HtmlOutputer()
  
  def craw(self,root_url):
    count = 1
    self.urls.add_new_url(root_url)

    while self.urls.has_new_url():
      try:
        new_url = self.urls.get_new_url()
        print 'craw %s : %s' % (count, new_url)
        html_count = self.downloader.download(new_url)
        new_urls, new_data = self.parser.parse(new_url, html_count)
        self.urls.add_new_urls(new_urls)
        self.output.collect_data(new_data)

        if count == 1000:
          break
        
        count ++
        
      except:
        print 'craw fialed'
        
    self.outputer.output_html()

if __name__ == '__main__':
  root_url = 'http://baike.baidu.com/view/21087.htm'
  obj_spider = SpiderMain()
  obj_spider.craw(root_url)