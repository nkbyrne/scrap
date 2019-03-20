#!/usr/bin/env python3
import sys
import feedparser

urls = {"bbc": "http://feeds.bbci.co.uk/news/rss.xml",
        "dailymail": "https://www.dailymail.co.uk/articles.rss",
        "elreg": "https://www.theregister.co.uk/headlines.atom",
        }

if len(sys.argv) >= 2:
    if sys.argv[1] == "1":
        url = urls["bbc"]
    elif sys.argv[1] == "2":
        url = urls["dailymail"]
    elif sys.argv[1] == "3":
        url = urls["elreg"]
    else:
        print("Invalid option")
else:
    print("script can be used like: {} \"number\"".format(sys.argv[0]))
    site = input("Press: \n\""
                 "1\" for bbc \n\""
                 "2\" for dailymail\n\""
                 "3\" for theregister\n ")
    if site == "1":
        url = urls["bbc"]
    elif site == "2":
        url = urls["dailymail"]
    elif site == "3":
        url = urls["elreg"]
    else:
        print("unknow option")
        exit(1)

feed = feedparser.parse(url)
rss = reversed(feed["entries"])

for entry in rss:
    print()
    print(entry["title"])
    print(entry["summary"])
    print(entry["link"])
print()
