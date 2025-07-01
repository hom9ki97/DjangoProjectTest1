from ecdsa import SigningKey, NIST256p
from ecdsa.util import randrange_from_seed__trytryagain
import hashlib
import base64

def generate_keys(data:dict):
    user_data_str = (f'{data.get('name')}{data.get('surname')}'
                     f'{data.get('email')}{data.get('card_number')}'
                     f'{data.get('date')}')
    seed = hashlib.sha256(user_data_str.encode()).digest()

    private_key = create_private_key(seed)
    print(private_key)
    public_key = private_key.get_verifying_key()
    print(public_key)
    base64_public_key = decode_base64_key(public_key)
    base64_private_key = decode_base64_key(private_key)

    return base64_public_key, base64_private_key


def create_private_key(seed):
    secexp = randrange_from_seed__trytryagain(seed, NIST256p.order)
    return SigningKey.from_secret_exponent(secexp, curve=NIST256p)


def decode_base64_key(key):
    raw_key = key.to_pem()
    base64_key = base64.b64encode(raw_key).decode('utf-8')
    return base64_key