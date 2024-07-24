from ead import ElasticNetAttacks
from elliptic_curve_tools import ECDSA
from cosPGD import CosPGD
from membership_inference_attacks import MembershipInference

def perform_elastic_net_attack(model, data):
    """
    Perform an Elastic-Net attack on a machine learning model.
    
    Parameters:
        model (object): The machine learning model to attack.
        data (object): The data used for the attack.
    """
    attack = ElasticNetAttacks(model, data)
    results = attack.attack()
    print("Elastic-Net Attack results:", results)

def perform_ecdsa_attack(data):
    """
    Perform an ECDSA attack using elliptic curve tools.
    
    Parameters:
        data (object): The data to use for the attack.
    """
    ecdsa = ECDSA()
    result = ecdsa.attack(data)
    print("ECDSA Attack result:", result)

def perform_cospgd_attack(model, data):
    """
    Perform a CosPGD attack on a machine learning model.
    
    Parameters:
        model (object): The machine learning model to attack.
        data (object): The data used for the attack.
    """
    cospgd = CosPGD(model, data)
    results = cospgd.attack()
    print("CosPGD Attack results:", results)

def perform_membership_inference_attack(model, data):
    """
    Perform a Membership Inference attack on a machine learning model.
    
    Parameters:
        model (object): The machine learning model to attack.
        data (object): The data used for the attack.
    """
    mia = MembershipInference(model, data)
    results = mia.attack()
    print("Membership Inference Attack results:", results)

if __name__ == "__main__":
    # Example usage
    model = 'Your Model Here'  # Replace with actual model instance
    data = 'Your Data Here'    # Replace with actual data

    perform_elastic_net_attack(model, data)
    perform_ecdsa_attack(data)
    perform_cospgd_attack(model, data)
    perform_membership_inference_attack(model, data)
