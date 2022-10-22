import jwt

from jwt.algorithms import get_default_algorithms


def get_id_from_jwt(token):
    result = token.split(' ');
    #print(result)
    print(result[1])
    get_default_algorithms()
    id = jwt.decode(result[1], '109ejaovnlxnvqaiofqwjeofjmdslknvbubnqwpofjlsknvmxn013i419ur8iufghjoidf812374iuyewhfi92hids', algorithms='HS512')
    print(id)

