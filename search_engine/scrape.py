# page spider
import urllib.parse
import urllib.request
import urllib
import bs4

url = "http://nytimes.com"

# stack of urls to scrape
urls = [url]

# historic record of urls
visited = [url]

while len(urls) > 0:
    try:
        html_text = urllib.request.urlopen(urls[0]).read()
    except:
        print(urls[0])

    soup = bs4.BeautifulSoup(html_text, "html.parser")

    urls.pop(0)

    # bs4.BeautifulSoup(...).find_all("title") finds the title of a web page
    # print(soup.find_all("title"))
    # print(soup.find_all("a")) finds all links in soup

    for tag in soup.find_all("a"):
        tag['href'] = urllib.parse.urljoin(url, tag['href'])
        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])

print(visited)
