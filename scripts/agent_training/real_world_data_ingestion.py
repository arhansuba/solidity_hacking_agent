import requests

class DataIngestion:
    def __init__(self):
        self.data_sources = [
            "https://api.example.com/data-source-1",
            "https://api.example.com/data-source-2"
        ]

    def ingest_data(self):
        all_data = []
        for source in self.data_sources:
            response = requests.get(source)
            if response.status_code == 200:
                data = response.json()
                all_data.extend(data)
            else:
                print(f"Failed to fetch data from {source}")
        return all_data

if __name__ == "__main__":
    data_ingestion = DataIngestion()
    data = data_ingestion.ingest_data()
    print("Ingested Data:")
    print(data)
