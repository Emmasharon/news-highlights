class Sources:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,sources,category,language,country,name,title,urlToImage,description,published):
        self.id = id
        self.sources = sources
        self.category = category
        self.language = language
        self.country = country
        self.name =name
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt
        
class Articles:
    '''
    Class to define Article objects
    '''
    def __init__(self,title,url,content,author):
        self.title = title
        self.url = url
        self.content = content
        self.author = author
    
