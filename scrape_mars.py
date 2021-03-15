from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo
import pandas as pd


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    #nasa mars news
        browser = init_browser()
        url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
        browser.visit(url)

        time.sleep(5)

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

        time.sleep(5)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        results = soup.find_all('div', class_='header')

        for result in results:
            image_path = result.find(class_='headerimage fade-in')['src']
            featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{image_path}'

        browser.quit() 

        mars['featured_image'] = featured_image_url

    #Mars Facts
        url = 'https://space-facts.com/mars/'
        tables = pd.read_html(url)
        df = tables[0]
        vert_df = df.rename(columns = {0:'', 1:'Mars'})
        vert_df = vert_df.set_index('')
        vert_html_table = vert_df.to_html()
        vert_html_table = vert_html_table.replace('\n', '')
        
        mars['facts'] = vert_html_table

    #Mars Hemispheres
        hemisphere_image_urls = []

        #Cerberus Hemisphere Enhanced
        url_1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
        #Schiaparelli Hemisphere Enhanced
        url_2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
        #Syrtis Major Hemisphere Enhanced
        url_3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
        #Valles Marineris Hemisphere Enhanced
        url_4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

        urls = [url_1, url_2, url_3, url_4]

        for url in urls:
            browser = init_browser()
            browser.visit(url)

            time.sleep(5)
            
            mars_hemisphere = {}
            
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            
            #pulling image url
            img = soup.find(class_='wide-image')['src']
            img_link = f'https://astrogeology.usgs.gov/{img}'
            
            #pulling title of hemisphere
            title = soup.find('h2', class_='title').text
            
            #appending to dictionary
            mars_hemisphere['title'] = title
            mars_hemisphere['img_url'] = img_link
            hemisphere_image_urls.append(mars_hemisphere)
            
            browser.quit()
        
        mars['hemispheres'] = hemisphere_image_urls
        
        return mars

if __name__ == "__main__":
    data = scrape_info()
    print(data)

