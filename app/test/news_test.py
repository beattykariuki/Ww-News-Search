import Unittest
from models import news
News = news.News

class NewsTest(.TestCase):

    def setUp(self):
      self.new_news = News(null,'Michelle Obama Begins Arena Tour in Talk With Oprah','null','\/\/www.usnews.com\/news\/entertainment\/articles\/2018-11-13\/michelle-obama-begins-arena-tour-in-talk-with-oprah','null','2018-11-14T06:09:00Z','null')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

class NewsTest(.TestCase):

    def setUp(self):
      self.new_news = News(null, 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.,'
'
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))



if __name__ == '__main__':
    unnitest.main()
    