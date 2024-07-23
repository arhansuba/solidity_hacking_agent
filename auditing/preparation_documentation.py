import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentationPreparation:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()
        self.documents = {
            'requirements': [],
            'processes': [],
            'audit': [],
            'compliance': [],
            'reviews': []
        }

    def load_config(self):
        """
        Load configuration settings from a JSON file.
        """
        if not os.path.isfile(self.config_path):
            logging.error(f"Configuration file {self.config_path} not found.")
            raise FileNotFoundError(f"Configuration file {self.config_path} not found.")
        
        with open(self.config_path, 'r') as file:
            config = json.load(file)
        
        logging.info(f"Configuration loaded from {self.config_path}.")
        return config

    def gather_requirements(self):
        """
        Gather and document project requirements.
        """
        logging.debug("Gathering project requirements.")
        requirements = self.config.get('requirements', [])
        
        if not requirements:
            logging.warning("No requirements found in the configuration.")
        
        for requirement in requirements:
            self.documents['requirements'].append({
                'requirement': requirement,
                'timestamp': datetime.now().isoformat()
            })
        
        logging.info(f"Requirements gathered: {len(requirements)} entries.")

    def document_processes(self):
        """
        Document processes based on the project configuration.
        """
        logging.debug("Documenting project processes.")
        processes = self.config.get('processes', [])
        
        if not processes:
            logging.warning("No processes found in the configuration.")
        
        for process in processes:
            self.documents['processes'].append({
                'process': process,
                'timestamp': datetime.now().isoformat()
            })
        
        logging.info(f"Processes documented: {len(processes)} entries.")

    def prepare_audit_info(self):
        """
        Prepare documentation for audit purposes.
        """
        logging.debug("Preparing audit information.")
        audit_info = self.config.get('audit', [])
        
        if not audit_info:
            logging.warning("No audit information found in the configuration.")
        
        for info in audit_info:
            self.documents['audit'].append({
                'audit_info': info,
                'timestamp': datetime.now().isoformat()
            })
        
        logging.info(f"Audit information prepared: {len(audit_info)} entries.")

    def ensure_compliance(self):
        """
        Ensure and document compliance requirements.
        """
        logging.debug("Ensuring compliance requirements.")
        compliance_info = self.config.get('compliance', [])
        
        if not compliance_info:
            logging.warning("No compliance information found in the configuration.")
        
        for info in compliance_info:
            self.documents['compliance'].append({
                'compliance_info': info,
                'timestamp': datetime.now().isoformat()
            })
        
        logging.info(f"Compliance information ensured: {len(compliance_info)} entries.")

    def conduct_reviews(self):
        """
        Conduct and document reviews based on project requirements.
        """
        logging.debug("Conducting reviews.")
        reviews = self.config.get('reviews', [])
        
        if not reviews:
            logging.warning("No review information found in the configuration.")
        
        for review in reviews:
            self.documents['reviews'].append({
                'review': review,
                'timestamp': datetime.now().isoformat()
            })
        
        logging.info(f"Reviews conducted: {len(reviews)} entries.")

    def save_documentation(self, output_dir):
        """
        Save the gathered documentation to the specified output directory.
        """
        if not os.path.isdir(output_dir):
            logging.error(f"Output directory {output_dir} does not exist.")
            raise FileNotFoundError(f"Output directory {output_dir} does not exist.")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f'documentation_{timestamp}.json')
        
        with open(output_file, 'w') as file:
            json.dump(self.documents, file, indent=4)
        
        logging.info(f"Documentation saved to {output_file}.")

def main():
    config_path = 'config/preparation_documentation_config.json'
    output_dir = 'doc'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Prepare documentation
    prep_doc = DocumentationPreparation(config_path)
    prep_doc.gather_requirements()
    prep_doc.document_processes()
    prep_doc.prepare_audit_info()
    prep_doc.ensure_compliance()
    prep_doc.conduct_reviews()
    prep_doc.save_documentation(output_dir)

if __name__ == '__main__':
    main()
