class Source:
    def __init__(self, id, name, description, category, url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url

class Article:
    def __init__(self, url, author, title, description, urlToImage, published):
        self.url = url
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.published = published
