## before executing the script, run this command : "pip install twitter-hashtag-scraper"
from twitter_hashtag_scraper import TwitterHashtagScraper

## change the x_guest_token with your personal twitter guest token. You can find it by running "curl -vkL twitter.com/ > web | grep -o 'gt=[0-9]*' | sed s.gt=.."
## write the hashtag that you want to scrape in hashtag="#"
## modify the number of tweets you want to scrape in max_tweets
TwitterHashtagScraper(hashtag="#",x_guest_token="", use_proxy=False,output_path="",max_tweets=100).collect()
