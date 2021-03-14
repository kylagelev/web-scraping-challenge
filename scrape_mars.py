from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo
import pandas as pd

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.mars_data

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    #nasa mars news
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser = init_browser()
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find_all('div', class_='image_and_description_container')

        information = []
        mars = {}

        for result in results:
            try:
                title = result.find('div', class_='content_title').text
                paragraph = result.find('div', class_='article_teaser_body').text
            
        #create individual dictionaries for pulling specific data from source
                article_info = {}
                article_info['title'] = title
                article_info['paragraph'] = paragraph
                information.append(article_info)
        
            except:
                news_t = information[0]['title']
                news_para = information[0]['paragraph']

        browser.quit()

        mars['title'] = news_t
        mars['news_p'] = news_para

    #JPL Mars Space Images - Featured Image
        url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
        browser = init_browser()
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find_all('div', class_='header')

        for result in results:
            image_path = result.find(class_='headerimage fade-in')['src']
            featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{image_path}'

        browser.quit() 

        mars['featured image'] = featured_image_url

    #Mars Facts
        url = 'https://space-facts.com/mars/'
        tables = pd.read_html(url)
        df = tables[0]
        vert_df = df.rename(columns = {0:'', 1:'Mars'})
        vert_df = vert_df.set_index('')
        vert_html_table = vert_df.to_html()
        vert_html_table.replace('\n', '')
        
        mars['facts'] = vert_html_table

    #Mars Hemispheres


        


# if __name__ == "__main__":
#    data = scrape()
 #   print(data)