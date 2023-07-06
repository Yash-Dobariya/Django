import uuid


IDENTIFIER = {}

def id_for(key):
    if id not in IDENTIFIER:
        IDENTIFIER[key] = str(uuid.uuid4())
    return IDENTIFIER[key]
