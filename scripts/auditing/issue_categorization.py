import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample training data for issue categorization
TRAINING_DATA = [
    ("Reentrancy attack vulnerability", "Reentrancy"),
    ("Unchecked low-level call", "Low-level Call"),
    ("Integer overflow and underflow", "Integer Overflow"),
    ("Unrestricted access control", "Access Control"),
    ("Front-running vulnerability", "Front-running"),
    ("Denial of service attack", "DoS"),
    # Add more examples as needed
]

# Prepare training data
texts, labels = zip(*TRAINING_DATA)

# Create a text classification pipeline
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),  # Convert text to feature vectors
    ('classifier', MultinomialNB())      # Naive Bayes classifier
])

# Train the model
pipeline.fit(texts, labels)

def categorize_issue(issue_description):
    """Categorize the given issue description into predefined categories."""
    category = pipeline.predict([issue_description])[0]
    return category

def issue_categorization(issues):
    """Categorize a list of issues."""
    categorized_issues = {}
    for issue in issues:
        category = categorize_issue(issue['description'])
        if category not in categorized_issues:
            categorized_issues[category] = []
        categorized_issues[category].append(issue)
    return categorized_issues

# Usage example
if __name__ == "__main__":
    # Example issues to categorize
    issues = [
        {"description": "Reentrancy attack vulnerability in function XYZ"},
        {"description": "Unchecked low-level call in contract ABC"},
        {"description": "Potential integer overflow in function DEF"},
        {"description": "Unrestricted access control in function GHI"},
        {"description": "Denial of service attack potential in function JKL"}
    ]

    categorized_issues = issue_categorization(issues)
    
    # Print categorized issues
    print(json.dumps(categorized_issues, indent=2))
