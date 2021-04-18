from unittest import TestCase
from pprint import pprint
from Scrapers.JournalScraper import JournalScraper

class JournalScraper_Test(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.scraper = JournalScraper()
        
    @classmethod
    def tearDownClass(cls):
        cls.scraper.__end__()

    def test_loop_scraper(self):
        scraper = self.scraper
        my_list = [
            'https://gut.bmj.com/content/68/9/1537', 
            'https://gut.bmj.com/content/68/9/1588', 
            
            'https://www.gastrojournal.org/article/S0016-5085(18)34810-8/fulltext', 
            'https://www.gastrojournal.org/article/S0016-5085(18)35206-5/fulltext', 
            
            'https://academic.oup.com/jcag/article/2/Supplement_1/S73/5099120', 
            'https://academic.oup.com/jat/article-abstract/doi/10.1093/jat/bkaa070/5856455?redirectedFrom=fulltext', 
            
            'https://www.sciencedirect.com/science/article/pii/S0022460X20300754', 
            'https://www.sciencedirect.com/science/article/abs/pii/S0022460X20300651'
        ]
        expected = [True, False, True, False, True, False, True, False]
        actual = []
        scraper = JournalScraper()
        i = 1
        for paper in my_list:
            value = scraper.check_if_article_is_free(paper)
            if value is False:
                actual.append(False)
            else:
                actual.append(True)
        for item in actual:
            print(item)
        self.assertTrue(expected == actual, "Mismatch: " + str(actual))