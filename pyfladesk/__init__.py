import webview
from threading import Thread
import werkzeug.serving
import socket
import time
import sys

class ApplicationThread():
    def __init__(self, application, port=5000):
        self.application = application
        self.port = port
        self.server = None
        self.flask_thread = None
    
    def _run_flask_app(self):
        self.server = werkzeug.serving.make_server('localhost', self.port, self.application)
        self.server.serve_forever()

    def start(self):
        self.flask_thread = Thread(target=self._run_flask_app)
        self.flask_thread.start()

    def stop(self):
        if self.server:
            self.server.shutdown()
        self.flask_thread.join()

def _wait_for_flask(port):
    for _ in range(10):
        try:
            sock = socket.create_connection(('localhost', port), timeout=1)
            sock.close()
            break
        except (ConnectionRefusedError, socket.timeout):
            time.sleep(0.5)
    else:
        print("O servidor Flask não pôde ser iniciado.")
        return

def init_gui(application, port=0, width=800, height=600,
             window_title="PyFladesk", icon="appicon.png", argv=None):
    if argv is None:
        argv = sys.argv

    if port == 0:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', 0))
        port = sock.getsockname()[1]
        sock.close()

    webapp = ApplicationThread(application, port)
    webapp.start()

    _wait_for_flask(port)

    webview.create_window(window_title, f'localhost:{port}', width=width, height=height)
    webview.settings = {
        'ALLOW_DOWNLOADS': False,
        'ALLOW_FILE_URLS': True,
        'OPEN_EXTERNAL_LINKS_IN_BROWSER': True,
        'OPEN_DEVTOOLS_IN_DEBUG': False
        }
    webview.start()
    webapp.stop()