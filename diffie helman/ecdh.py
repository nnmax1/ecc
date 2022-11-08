
# Diffie hellman key exchange 

class ECDH(object):
    def __init__(self, keypair):
        self.keypair = keypair

    def get_secret(self, keypair):
        # Don;t check if both keypairs are on the same curve. Should raise a warning only
        if self.keypair.can_sign and keypair.can_encrypt:
            secret = self.keypair.priv * keypair.pub
        elif self.keypair.can_encrypt and keypair.can_sign:
            secret = self.keypair.pub * keypair.priv
        else:
            raise ValueError("Missing data to generate DH secret")
        return secret