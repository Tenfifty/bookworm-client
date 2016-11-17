import json
from more_itertools import chunked
import requests

DOC_CHUNK_SIZE = 500
SERVER = {'sv': 'https://bookworm.crawlica.com/{endpoint}/?api_key={api_key}',
          'da': 'https://dabookworm.crawlica.com/{endpoint}/?api_key={api_key}'}


class Bookworm(object):
    """The Bookworm API"""
    def __init__(self, api_key, lang='en'):
        super(Bookworm, self).__init__()
        if lang not in SERVER:
            raise ValueError('Unsupported language {}'.format(lang))
        self.api_key = api_key
        self.lang = lang

    def autotag(self, documents):
        data = json.dumps(documents)
        return self._make_request('autotag', data=data)

    def categorize(self, documents, categories):
        return self._make_request('categorize', documents,
                                  {'categories': categories})

    def cluster(self, documents):
        data = json.dumps(documents)
        return self._make_request('cluster', data=data)

    def entities(self, documents):
        return self._make_request('entities', documents)

    def sentiment(self, documents):
        return self._make_request('sentiment', documents)

    def wordcount(self, documents, remove_common=200, max_words=100):
        data = {
            'freetext': 1,
            'remove_common': remove_common,
            'max_words': max_words
        }
        return self._make_request('wordcount', documents, data)

    def wordsmash(self, documents, background):
        data = json.dumps({'background': background})
        url = self._get_endpoint('smash/background')
        response = requests.post(url, data=data)
        response.raise_for_status()

        url = self._get_endpoint('smash')
        for doc_chunk in chunked(documents, DOC_CHUNK_SIZE):
            data = {'current': doc_chunk}
            for result in self._make_single_request(url, data):
                yield result

    def _get_endpoint(self, endpoint):
        return SERVER[self.lang].format(endpoint=endpoint,
                                        api_key=self.api_key)

    def _make_single_request(self, url, data):
        if not isinstance(data, basestring):
            data = json.dumps(data)

        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['result']

    def _make_request(self, endpoint, documents=None, data=None):
        url = self._get_endpoint(endpoint)

        if data is None:
            data = {}

        if documents is not None:
            for doc_chunk in chunked(documents, DOC_CHUNK_SIZE):
                data['docs'] = doc_chunk
                for result in self._make_single_request(url, data):
                    yield result
        else:
            for result in self._make_single_request(url, data):
                yield result
