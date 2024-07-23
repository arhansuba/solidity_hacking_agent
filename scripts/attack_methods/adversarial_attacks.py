from ead import ElasticNetAttacks
from elliptic_curve_tools import ECDSA
from cosPGD import CosPGD
from membership_inference_attacks import MembershipInference

# Initialize and use Elastic-Net Attacks
def perform_elastic_net_attack(model, data):
    attack = ElasticNetAttacks(model, data)
    results = attack.attack()
    print("Elastic-Net Attack results:", results)

# Initialize and use ECDSA Tools
def perform_ecdsa_attack(data):
    ecdsa = ECDSA()
    result = ecdsa.attack(data)
    print("ECDSA Attack result:", result)

# Initialize and use CosPGD
def perform_cospgd_attack(model, data):
    cospgd = CosPGD(model, data)
    results = cospgd.attack()
    print("CosPGD Attack results:", results)

# Initialize and use Membership Inference Attacks
def perform_membership_inference_attack(model, data):
    mia = MembershipInference(model, data)
    results = mia.attack()
    print("Membership Inference Attack results:", results)

# Example usage
if __name__ == "__main__":
    model = 'Your Model Here'
    data = 'Your Data Here'

    perform_elastic_net_attack(model, data)
    perform_ecdsa_attack(data)
    perform_cospgd_attack(model, data)
    perform_membership_inference_attack(model, data)
