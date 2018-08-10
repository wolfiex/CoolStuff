import threading

# Global variable
data = None


class threadTwo(threading.Thread):
    def run(self):
        global data
        from PyQt4.QtCore import QObject, pyqtSlot
        from PyQt4.QtGui import QApplication
        from PyQt4.QtWebKit import QWebView
        
        html = '''
        <html>
        <body>
           <h1>Hello!</h1><br>
           <h2><a href=“#” onclick=“printer.text(‘Message from QWebView')“>QObject Test</a></h2>
           <h2><a href=“#” onclick=“alert(‘Javascript works!')“>JS test</a></h2>
        </body>
        </html>
        '''

        class ConsolePrinter(QObject):
           def __init__(self, parent=None):
               super(ConsolePrinter, self).__init__(parent)

           @pyqtSlot(str)
           def text(self, message):
               print message
               
        self.app = QApplication(sys.argv)
        view = QWebView()
        frame = view.page().mainFrame()
        printer = ConsolePrinter()
        view.setHtml(html)
        #frame.addToJavaScriptWindowObject('printer', printer)
        #frame.evaluateJavaScript("alert('Hello');")
        #frame.evaluateJavaScript(“printer.text(‘Goooooooooo!');“)
        view.show()
        self.app.exec_()  
        print 'exiting'
        self.join() 
        
            
    def kill(self):
        self.app.exit()
        self.join()
        print 'exit'
        
        
        
t = threadTwo()
t.start()
