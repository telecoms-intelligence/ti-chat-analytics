# References

## Data
* [The National University of Singapore SMS Corpus, on Kaggle](http://www.kaggle.com/rtatman/the-national-university-of-singapore-sms-corpus/data)

## Source Code
* [Telecoms Intelligence (TI) Chat Analytics](http://github.com/telecoms-intelligence/ti-chat-analytics)

# Hands On

## Dependencies
It is advised to install Python virtual environment (``virtualenv``).
Following is a way to do it.

* Update pip and install virtualenv with pip
```bash
$ pip install --upgrade pip
$ pip install virtualenv
```

* Create and activate a new python3 virtualenv
```bash
$ mkdir -p ~/dev
$ cd ~/dev
$ virtualenv -p python3 venv34
$ ln -s venv34 venv3
$ source ~/dev/venv3/bin/activate
```

## Walkthrough

```bash
$ mkdir -p ~/dev/ti
$ cd ~/dev/ti
$ git clone https://github.com/telecoms-intelligence/ti-chat-analytics.git 
$ cd ~/dev/ti/ti-chat-analytics
$ python python/analyze-chats.py
                                                  smsCorpus
@date                                            2015.03.09
@version                                                1.2
message   [{'@id': 10120, 'text': {'$': 'Bugis oso near ...
```


