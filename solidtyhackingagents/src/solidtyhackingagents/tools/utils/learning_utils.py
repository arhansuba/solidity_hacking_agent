# learning_utils.py

from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2):
    """
    Split data into training and testing sets.
    """
    return train_test_split(X, y, test_size=test_size)

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a model using test data.
    """
    from sklearn.metrics import accuracy_score
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

def save_model(model, file_path: str):
    """
    Save a trained model to a file.
    """
    import joblib
    joblib.dump(model, file_path)
