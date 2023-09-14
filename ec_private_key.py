from jwcrypto.jwk import JWK
import jwcrypto
import random
import string
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
def generate_ephemeral_keys(use):

    kid = _random_alphanumeric_string(40)
    keypair = jwcrypto.jwk.JWK.generate(kty='EC', crv='P-256', kid=kid, use=use, alg='ES256')

    return keypair


def _random_alphanumeric_string(length):
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(length)
    )

key_pair = generate_ephemeral_keys(use='sig')
private_key_pem = key_pair.export_to_pem(private_key=True, password=None)

print(key_pair.export_private(as_dict=True))
print(private_key_pem)
print(private_key_pem.decode())

private_key_pem = serialization.load_pem_private_key(
    private_key_pem,
    password=None,
    backend=default_backend()
).private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)
print(private_key_pem.decode())

