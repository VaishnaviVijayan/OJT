import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

#create a sample dataset

data = [
    ("I love NLP", "Possitive"),
    ("I HATE THIS TECHNOLOGY", "Negative"),
    ("It's okay, nothing special", "Neutral")
]
#seperate all the sentence and labels

sentences, labels = zip(*data)

#downloaded the kits from library
nltk.download ('punkt')
nltk.download('stopwords')

#Initiliased the stopwords with assinging the language
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    
#remove the stop word and punchations
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

#preproccess for sentence which we pass as data
preprocess_sentences = [preprocess(sentence) for sentence in sentences]

#feature extraction
vectorizer = TfidfVectorizer()
x = vectorizer.transform(preprocess_sentences)

#split data into training and test data for model training
x_train,x_test,y_train,y_test = train_test_split(x,labels, test_size=0.2, random_state=42)

#train naive bayes classifier
classifier = MultinomialNB()
classifier.fit(x_train,y_train)

#code of prediction y from x
y_pred = classifier.predict(x_test)

#evaluating model

accuracy = accuracy_score(y_test,y_pred)
report = classification_report(y_test,y_pred)

print(f"Accuracy:{accuracy}")
print("classification Report")
print(report)
