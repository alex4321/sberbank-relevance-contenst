There you have basic model pipeline for https://contest.sdsj.ru A-task (question/paragraph relevance classification).

You'll need python3 (tested on 3.6) with few packages and nltk data:

    $ pip install -r requirements.txt
    $ python
    # import nltk
    # nltk.download("all")

In input/* you can see source dataset (just unpack archive).
In solutions/* - you'll see notebooks with solution scripts.
In data/* will stored some processed data (e.g. trained word2vec).
In output/* will stored solution.