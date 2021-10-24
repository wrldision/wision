import uuid

#Generate Unid code : Code unique qu
def autogenref():
    inter = uuid.uuid4()
    code = str(inter).replace('-', '')[:12]
    return code