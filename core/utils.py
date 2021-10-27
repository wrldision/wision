import uuid
from partenaire.models import Partenaire

#Generate Unid code : Code unique qu
def autogenref():
    inter = uuid.uuid4()
    code = str(inter).replace('-', '')[:12]
    return code

def get_partner_image_from_id(val):
    partner = Partenaire.objects.get(id=val)
    return vendeur.user.username

