# 👑 Coronada: Tweets about COVID-19 👑

## 👑 About this repository 👑

I got curious about what people were saying about this virus. So, I scraped a bunch of data off Twitter using a variety of terms suggested to me in [this Twitter thread](https://twitter.com/BayesForDays/status/1238146532534292482). This package is designed to work in Python3 because [Python2 is deprecated](https://www.python.org/doc/sunset-python-2/). Update your Python and join the future, friends!

In principle, if you want to install this package, here are the steps you should take:

1. Clone this repository wherever you clone your repositories (`git clone https://github.com/BayesForDays/coronada.git`)
2. Go to the cloned directory (`cd ./coronada/`)
3. Create a new [virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) in the repository directory and activate it. 
4. Install this package with `pip`: `pip install -e . --upgrade --user`
5. Enjoy! (Do not profit! Don't be a jerk.)

### 👑 Scraping process 👑

I have provided code that allows you to initiate your own scraping process, since I only gathered a ~2.2 million tweet sample gathered over the course of about 12 hours over March 13-14, 2020 (Central Daylight Time). The code `corona_swabber.py` (get it? 🤒) takes your [Twitter API credentials](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens) as arguments and prints the keyword search results as they stream in. 

You will need the following

* Consumer key
* Consumer key secret
* Access token
* Access token secret

I piped the output to another file:

```
python corona_swabber.py [arguments] > path/to/jsons_out.txt
```

If you are fancy, you can add e.g. different stopping criteria. However, I don't get paid to be fancy anymore. Feel free to submit a PR if you have improvements.

The sky's the limit! There are some tricky components to the Twitter API, namely how it handles quote tweets, retweets, and tweets over a certain length. [More information about Tweepy's capabilities can be found here](http://docs.tweepy.org/en/latest/api.html#tweepy-api-twitter-api-wrapper).

### 👑 Reproducibility and Data Privacy 👑

Because of privacy laws (e.g. in case a user locks their account), I am only able to provide tweet ids to you in `mar14-tweets.txt`. If you want to scrape these specific tweets, the tweepy interface allows you to do so fairly trivially.

