# nlp_query_processor.py

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

class NLPQueryProcessor:
    def __init__(self):
        self.pipeline = None
        self.label_encoder = LabelEncoder()

    def preprocess_text(self, text):
        """
        Tokenize, remove stopwords, and clean text data.
        """
        stop_words = set(stopwords.words('english'))
        table = str.maketrans('', '', string.punctuation)
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalpha()]
        tokens = [word for word in tokens if word not in stop_words]
        return ' '.join(tokens)

    def train_model(self, data):
        """
        Train a text classification model on the provided data.
        """
        texts = data['text']
        labels = data['label']
        
        self.label_encoder.fit(labels)
        labels_encoded = self.label_encoder.transform(labels)
        
        # Text preprocessing and vectorization
        self.pipeline = Pipeline([
            ('tfidf', TfidfVectorizer(preprocessor=self.preprocess_text)),
            ('clf', MultinomialNB())
        ])
        
        X_train, X_test, y_train, y_test = train_test_split(texts, labels_encoded, test_size=0.2, random_state=42)
        self.pipeline.fit(X_train, y_train)
        accuracy = self.pipeline.score(X_test, y_test)
        print(f'Model trained with accuracy: {accuracy:.2f}')

    def predict_query(self, query):
        """
        Predict the category of a given query.
        """
        if self.pipeline is None:
            raise RuntimeError("Model is not trained yet.")
        preprocessed_query = self.preprocess_text(query)
        prediction = self.pipeline.predict([preprocessed_query])
        return self.label_encoder.inverse_transform(prediction)[0]

# Example usage
if __name__ == "__main__":
    # Example data for training
    data = pd.DataFrame({
        'text': [
            'What is a SQL injection?',
            'How does XSS work?',
            'Explain command injection',
            'What are the common denial of service attacks?',
            'Describe a buffer overflow vulnerability'
        ],
        'label': [
            'SQL Injection',
            'XSS',
            'Command Injection',
            'DoS',
            'Buffer Overflow'
        ]
    })

    nlp_processor = NLPQueryProcessor()
    nlp_processor.train_model(data)

    # Test the model with a new query
    test_query = "Can you explain how cross-site scripting works?"
    category = nlp_processor.predict_query(test_query)
    print(f'The category for the query is: {category}')
