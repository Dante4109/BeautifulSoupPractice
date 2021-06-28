import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, pyqtSignal, QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import bs4 as bs


class Client(QWebEnginePage):
    toHtmlFinished = pyqtSignal()

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

    def store_html(self, html):
        self.html = html
        self.toHtmlFinished.emit()

    def get_html(self):
        self.toHtml(self.store_html)
        loop = QEventLoop()
        self.toHtmlFinished.connect(loop.quit)
        loop.exec_()
        return self.html


url = 'https://pythonprogramming.net/parsememcparseface/'
client_response = Client(url)
source = client_response.get_html()
soup = bs.BeautifulSoup(source, 'xml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)
