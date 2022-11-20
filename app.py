from flask import Flask, request
from flask import render_template
import youtubeScraper
app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        print("This is where we do the work")
        link = request.form.get("ytlink", None)
        if link is None:
            return render_template('NLGenerator.html')
        else:
            if "https://youtube.com/playlist?list=" in link:
                link = link.replace("https://youtube.com/playlist?list=", "")
            scrapedPair = youtubeScraper(link)
            link1 = (list(scrapedPair[0].getKeys())[0]) #string
            link2 = (list(scrapedPair[1].getKeys())[0]) #string
            list1 = next(iter(scrapedPair[0].values())) #list
            list2 = next(iter(scrapedPair[1].values())) #list
            duration1 = list1[0] ##double
            duration2 = list2[0] ##double
            thumbnailURL1 = list1[1] ##string
            thumbnailURL2 = list2[1] ##string
            title1 = list1[2] #string
            title2 = list2[2] #string
            
            return render_template('Newsletter.html', link1 = firstLink, link2= SecondLink, list1 = FirstList, list2 = SecondList, duration1 = FirstDurat, duration2 = SecondDurat, thumbnailURL1 = FirstThumb, thumbnailURL2 = SecondThumb, title1 = FirstTitle, title2 = SecondTitle)
    else:
        return render_template('NLGenerator.html')