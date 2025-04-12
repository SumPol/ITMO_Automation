class Page:
    def __init__(self, url):
        self.url = url

    def get(self):
        print('URL - ' + self.url)


home = Page('/home')
home.get()