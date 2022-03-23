# Twitter_Bot
Twitter bot for general purpose. 

## task
- [x] Auto Replies Based on Keywords
- [] Auto Replies Based on Trending Topics
- [x] Auto Replies To Certain Names

## Getting started 

### 1. clone repository
```
    git clone 
```

### 2. cd twitter_bot
```
    cd twitter_bot
```

### 3. create .env 
```
    touch .env
```

### 4. insert twitter credentials and WOE ID
```
    consumer_key=******
    consumer_key_secret=*******
    bearer_token=*********
    access_token=************
    access_token_secret=************
    WOE_ID=1
```

### 5. run 
```
   pip3 install tweepy
```

### 5. create .txt file and insert  Keywords and Names
text file name does not matter as long as the exstension is set to .txt
```
    touch keywords.txt
```

### 6. run 
```
    python3 bot.py
```