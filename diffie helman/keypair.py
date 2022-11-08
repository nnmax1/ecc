
# generate private and public key
class Keypair(object):
    def __init__(self, curve, priv=None, pub=None):
        if priv is None and pub is None:
            raise ValueError("Private and/or public key must be provided")
        self.curve = curve
        self.can_sign = True
        self.can_encrypt = True
        if priv is None:
            self.can_sign = False
        self.priv = priv
        self.pub = pub
        if pub is None:
            self.pub = self.priv * self.curve.g

