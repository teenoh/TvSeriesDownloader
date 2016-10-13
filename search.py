from __future__ import unicode_literals
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import youtube_dl

"""
   helps in scraping o2tvseries for data

   scrape_site: default function for scraping sites and getting links
   
   get_series_links: gets the links and titles of all series in dict format
   
   get_season_links: gets the links and corresponding seasons in dict format
                     when provided the series link
   
   get_episodes_links: gets the links and corresponding episodes in dict format
                     when provided the season link
   
   get_series_image:   gets the url of the series image
   
   get_download_link: scrapes site for download link when provided episode link
                       returns mp4 download link
   
   download:         creates subfolders in "series_name->season->episode" format
                      and downloads video in episode directory using youtube-dl                                                       

"""


def scrape_site(url):
    with urlopen(url) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="data")
        
        links = {(x.a.get_text()).lower(): x.a.get("href") 
                    for x in divs}
        return links
        
    
def get_series_links():
    series = scrape_site("http://o2tvseries.com/search/list_all_tv_series")
    return series

def get_series_image(series_link):
    with urlopen(series_link) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="img")
        img = [x.img.get('src') for x in divs]
        return img[0]

def get_season_links(series_link):
    seasons = scrape_site(series_link)
    return len(seasons), seasons

def get_episodes_links(season_link):
    episodes = scrape_site(season_link)
    return len(episodes), episodes 

def get_download_link(episode_link):
    with urlopen(episode_link) as f:
        soup = BeautifulSoup(f, "html.parser")
        divs = soup.find_all("div", class_="data")
        
        links = {x.a.get_text()[-3:]: x.a.get("href")
                            for x in divs
                            if x.a.get_text()[-3:] in ("3gp", "mp4")}

        #if string == "3gp": return links["3gp"]
        return links["mp4"]

def download(download_link, series_entered, season_entered):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #change directory to videos
        os.chdir("C:\\Users\\" + os.getlogin() + "\\Videos")
        
        series_dir = ".\\" + series_entered
        
        #check if series folder exists if not create it 
        #and change directory to it
        if  os.path.exists(series_dir) : os.chdir(series_dir)
        else:
            os.mkdir(series_dir)
            os.chdir(series_dir)    

        seas_dir = ".\\" + season_entered

        #check if seasons folder exists if not create it 
        #and change directory to it
        if  os.path.exists(seas_dir) : os.chdir(seas_dir)
        else:
            os.mkdir(seas_dir)
            os.chdir(seas_dir)    
        
        #download video file in directory using youtube-dl
        ydl.download([download_link])