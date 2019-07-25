from facebook_scraper import get_posts
import pandas as pd

#Variables for the Dataframe
post_id = []
text = []
date = []
image = []
likes = []
comments = []
shares = []
post_url = []

#getting the Data from Facebook and writing it in lists

#Replace "fb-page" with the site you want to scrape
#E.g. www.facebook.com/foo use foo as site name
#This Scraper does not get video URLs.  

for post in get_posts("fb-page", pages = 50):
    post_id.append(post['post_id'])
    text.append(post['text'])
    date.append(post['time'])
    image.append(post['image'])
    likes.append(post['likes'])
    comments.append(post['comments'])
    shares.append(post['shares'])
    post_url.append(post['post_url'])

#transforming the lists to pandas series 
text = pd.Series({'PostID':post_id ,'Text':text, 'Date':date, 'Image_URL':image, 'Likes':likes, 'Comments':comments, 'Shares':shares, 'Post_URL':post_url})


#creating a data frame
posts = pd.DataFrame(text)

#creating a csv containing the data
posts.to_csv('FB_Site_Date')

#check the dataframe
print('-------')
print(posts)
