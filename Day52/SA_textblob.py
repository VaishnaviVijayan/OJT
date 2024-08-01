#textblob library
#import textblob 
from textblob import TextBlob

#create sample text

texts = [
    " I love NLP! It works great and I'm very statisfied ", 
    "This my first experiance on doing sentiment analysis, I am little bit disappointed",
    "The NLP sentim ent analysis is quite interesting , it is neither good or bad",
]

#create function to the sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    #-1.0 - 1.0 polarity score
    polarity = analysis.sentiment.polarity
    if polarity>0:
        sentiment = "Positive"
    elif polarity<0:
        sentiment = "Negative"
    else :
        sentiment = "Neutral"
    return sentiment

for text in texts:
    sentiment = analyze_sentiment(text)
    print(f"Text:{text}")
    print(f"Sentiment:{sentiment}\n")
