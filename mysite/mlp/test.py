from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Assume that you have a list of news articles `articles` and a corresponding list of labels `labels`
# where the label is 1 if the article is fake and 0 if it is real

# First, you need to convert the articles into a numerical representation
# One way to do this is to use the TfidfVectorizer to compute the tf-idf vectors for the articles
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(articles)

# Next, you can train the PassiveAggressiveClassifier on the vectors and labels
classifier = PassiveAggressiveClassifier()
classifier.fit(X, labels)

# Now you can use the classifier to predict the labels for new articles
new_articles = ['This is a fake news article', 'This is a real news article']
new_X = vectorizer.transform(new_articles)
predictions = classifier.predict(new_X)

print(predictions)  # Outputs: [1, 0]



#Tfid

from sklearn.feature_extraction.text import TfidfVectorizer
from pythainlp.tokenize import word_tokenize
from pythainlp.corpus import stopwords
from pythainlp.stem import ThaiStemmer

def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stop words
    stop_words = stopwords.words('thai')
    tokens = [token for token in tokens if token not in stop_words]
    
    # Stem the tokens
    stemmer = ThaiStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    # Join the tokens back into a single string
    return ' '.join(tokens)

# Assume that you have a list of Thai texts `texts`
texts_preprocessed = [preprocess(text) for text in texts]

# Vectorize the texts using TfidfVectorizer
vectorizer = TfidfVectorizer(analyzer='word')
X = vectorizer.fit_transform(texts_preprocessed)
