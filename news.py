import requests
import pyttsx3

url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=f38b26e86acb46c29058439829075408')

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
speed = engine.setProperty("rate", 150)
engine.setProperty('voice','voices[1].id')

def get_news():
    headlines = []
    response = requests.get(url)
    results = response.json()
    #print(res.json())
    news = results["articles"]
    for article in news:
        headlines.append(article['title'])
    for i in range(len(headlines)):
        print(i+1, headlines[i])
    engine.say(headlines)
    engine.runAndWait()
get_news()