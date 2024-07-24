import pandas as pd

# Load and process adversarial attack datasets
def load_adversarial_datasets(filepath):
    try:
        data = pd.read_csv(filepath)
        print(f"Loaded dataset with {len(data)} records.")
        
        # Check for expected columns (example columns: 'contract_id', 'attack_type', 'severity')
        expected_columns = ['contract_id', 'attack_type', 'severity', 'details']
        missing_columns = [col for col in expected_columns if col not in data.columns]
        if missing_columns:
            print(f"Warning: Missing expected columns: {', '.join(missing_columns)}")
        
        # Display basic statistics
        print("\nBasic statistics of the dataset:")
        print(data.describe(include='all'))
        
        # Display a sample of the dataset
        print("\nSample data:")
        print(data.head())
        
        return data
    except FileNotFoundError:
        print("Dataset file not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("The dataset is empty. Please check the file.")
    except pd.errors.ParserError:
        print("Error parsing the dataset. Please check the file format.")
    except Exception as e:
        print("Failed to load dataset:", e)

# Example usage
if __name__ == "__main__":
    dataset_path = './adversarial_dataset.csv'
    data = load_adversarial_datasets(dataset_path)
