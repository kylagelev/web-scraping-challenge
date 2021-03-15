# web-scraping-challenge

## Outer space may be vast, but so is the internet.

### This repository contains a jupyter notebook, an index.html file (in templates) and a corresponding style_sheet (in static), an app (app.py), and a python file (scrape_mars.py with the scraping function). 

#### Information on how to scrape data from the web, connect to mongodb, and add to the html file are what follows. 

Initially, web scraping was completed using a jupyter notebook. Within the folder, "Mission_to_Mars," contains the aformentioned jupyter-notebook, and an output folder of the initial html table(s) completed on the "Mars Facts!"

Using the jupyter notebook as a guide, using visual studio, a python file was created with a similar means of scraping for data from a series of sites. These include: 
* [NASA News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
  * Scraped to find the latest news article and corresponding paragraph.
* [JPL Featured Image](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)
  * Scraped for the featured image.
* [Mars Facts](https://space-facts.com/mars/)
  * Scraped for Mars Facts within a table
* [Mars Hemispheres](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
  * Scraped for Mars' 4 Hemispheres
 
These were then inserted into a mongodb database. 

Following this, an html file was created that linked to an app in order to run the scraping and add it to the database whenever the button was pressed, and present the information formatted onto the index.html. Screenshots of the completed, final app are included in the folder, app_screenshots. 
