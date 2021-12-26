import logging
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class HttpHandler(logging.Handler):
    def __init__(self, url: str, silent: bool = True):

        self.url    = url
        self.silent = silent

        # Create and set up server session
        self.session = requests.Session()
        self._setup_session()

        super().__init__()
        

    def _setup_session(self):
        '''Sets up the session with the server'''

        self.session.headers.update({
            'Content-Type': 'application/json',
        })

        self.session.mount('https://', HTTPAdapter(
            max_retries=Retry(
                total=5,
                backoff_factor=0.05,
                status_forcelist=[403, 500]
            ),
            pool_connections=100,
            pool_maxsize=100
        ))


    def emit(self, record):
        '''Sends the record in a POST request to the specified url'''

        logEntry = self.format(record)
        response = self.session.post(self.url, data=logEntry, auth=('user', 'pass'))

        if not self.silent:
            print(f"Log forwarded to url: {response}")
            