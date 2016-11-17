Bookworm
========

This is a Python client for the Bookworm natural language API, made available by Crawlica.

You can register to receive an API key at https://bookworm.crawlica.com/request_api_key/


Example usage
-------------

.. code-block:: python

    import tabulate
    from bookworm import Bookworm


    API_KEY = '...'

    documents = ['De två största städerna i Sverige är Stockholm och Göteborg',
                 'Donald Trump blir Barack Obamas efterträdare']

    b = Bookworm(API_KEY, 'sv')
    res = b.entities(documents)

    for ents in res:
        data = [[ent['entity'], ent['type'], ', '.join(ent['variants'])] for ent in ents]
        print(tabulate.tabulate(data, headers=['Entity', 'Type', 'Variants']))
        print('')



::

    Entity     Type    Variants
    ---------  ------  ----------
    Sverige    geo     Sverige
    Stockholm  geo     Stockholm
    Göteborg   geo     Göteborg

    Entity        Type    Variants
    ------------  ------  -------------
    Donald Trump  person  Donald Trump
    Barack Obama  person  Barack Obamas


Installation
------------

.. code-block:: bash

  $ pip install bookworm



Functionality currently available
---------------------------------

* *autotag* - Automatically tag documents with the best matching tags from our large database of tags.
* *wordsmash* - Compare document sets to get the essence of what makes a subset special. Get the defining words and phrases.
* *entities* - Extract named entities (people, organisations, and places) from each document
* *sentiment* - Get a numerical representation of how positive or negative each document is
* *wordcount* - Get a count of the distinct words in the documents. Declinations are grouped into the base form and stop words can be removed.
* *cluster* - Automatically collect documents into groups, based on their topics, and describe those groups.
* *categorize* - Automatically put documents in a set of categories that you choose. The categories are defined by topic words, but the documents need not contain any of those words, just “close” words.