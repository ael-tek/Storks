## before executing the script, run this command : "pip install twitter-hashtag-scraper"

from twitter_hashtag_scraper import TwitterHashtagScraper

## change the x_guest_token with your personal twitter guest token. You can find it by running "curl -vkL twitter.com/ > web | grep -o 'gt=[0-9]*' | sed s.gt=.."
## write the hashtag that you want to scrape in hashtag="#"
## modify the number of tweets you want to scrape in max_tweets

TwitterHashtagScraper(hashtag="#birth",x_guest_token="1371734877725396992", use_proxy=False,output_path="",max_tweets=20).collect()
TwitterHashtagScraper(hashtag="#pregnant",x_guest_token="1371734877725396992", use_proxy=False,output_path="",max_tweets=20).collect()
