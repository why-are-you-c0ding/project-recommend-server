from jose import jwt
import base64
import math
import secret

def get_id_from_jwt(token):
    result = token.split(' ')
    key = secret.SECRET_KEY

    code = key.ljust((int)(math.ceil(len(key) / 4)) * 4, '=')

    id = jwt.decode(result[1], base64.b64decode(code), algorithms=['HS256'])
    return id

