import json
import requests

VERSION = 'v1'
BACKEND = 'https://text.crawlica.com'
ENDPOINT_TPL = '{backend}/{version}/{lang}/{endpoint}/?api_key={api_key}'


class Bookworm(object):
    """The Bookworm API"""

    def __init__(self, api_key, lang='en'):
        super(Bookworm, self).__init__()
        self.api_key = api_key
        self.lang = lang

    def anomalies(self, docs, reference_docs, max_words, min_score):
        data = {
            'docs': docs,
            'reference_docs': reference_docs,
            'max_words': max_words,
            'min_score': min_score
        }
        return self._make_request('anomalies', data)

    def categories(self, docs, categories):
        data = {
            'docs': docs,
            'categories': categories
        }
        return self._make_request('categories', data)

    def clusters(self,
                 docs,
                 use_synonyms=True,
                 min_df=2,
                 max_df=0.5,
                 min_cluster_size=0):
        data = {
            'docs': docs,
            'use_synonyms': use_synonyms,
            'min_df': min_df,
            'max_df': max_df,
            'min_cluster_size': min_cluster_size
        }
        return self._make_request('clusters', data)

    def counts(self,
               docs,
               remove_common=200,
               once_per_document=True,
               min_count=2,
               max_words=100):
        data = {
            'docs': docs,
            'remove_common': remove_common,
            'once_per_document': once_per_document,
            'min_count': min_count,
            'max_words': max_words
        }
        return self._make_request('counts', data)

    def entities(self, docs, allow_heuristics=True):
        data = {
            'docs': docs,
            'allow_heuristics': allow_heuristics
        }
        return self._make_request('entities', data)

    def sentiment(self, docs, target=''):
        data = {
            'docs': docs,
            'target': target
        }
        return self._make_request('sentiment', data)

    def topics(self, docs, max_topics=3, min_score=1):
        data = {
            'docs': docs,
            'max_topics': max_topics,
            'min_score': min_score
        }
        return self._make_request('topics', data)

    def wordcloud(self,
                  words,
                  width=900,
                  height=500,
                  background_color='white'):
        data = {
            'words': words,
            'width': width,
            'height': height,
            'background_color': background_color
        }
        res = self._make_request('wordcloud', data)
        absolute_url = '{}{}'.format(BACKEND, res['url'])
        return {'url': absolute_url}

    def _make_request(self, endpoint, data=None):
        url = ENDPOINT_TPL.format(backend=BACKEND,
                                  endpoint=endpoint,
                                  api_key=self.api_key,
                                  version=VERSION,
                                  lang=self.lang)
        if data is None:
            data = {}

        if not isinstance(data, str):
            data = json.dumps(data)

        response = requests.post(url, data=data)
        response.raise_for_status()
        return response.json()['result']
