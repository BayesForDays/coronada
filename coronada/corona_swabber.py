#!/usr/bin/env python
# coding: utf-8

import tweepy as tw
import json
import click

terms = ['coronavirus', 'corona virus', 'corona', 'rona', 'roni', 'covid19', 'cov19', 'cov', 'covid',
         'covid-19', 'covid_19', 'novel cororavirus', 'cv', 'cov-19', 'sars-cov-2', 'corvid', 'corvid-19']


class Covid19Listener(tw.StreamListener):
	"override tweepy.StreamListener to add logic to on_status"
	def on_status(self, status):
		return print(json.dumps(status._json))


@click.command()
@click.option('--consumer_key')
@click.option('--consumer_secret')
@click.option('--access_token')
@click.option('--access_token_secret')
def swab(consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
	auth = tw.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tw.API(auth, wait_on_rate_limit=True, 
             wait_on_rate_limit_notify=True, retry_delay=10)
	listener = Covid19Listener()
	stream = tw.Stream(auth = api.auth, listener=listener)
	stream.filter(track=terms, languages=['en'])


if __name__=="__main__":
	swab()
