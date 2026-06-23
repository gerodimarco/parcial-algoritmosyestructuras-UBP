from math import gcd


class RSADemo:
    """
    Implementación educativa de RSA.

    Utiliza números primos pequeños para
    demostrar el funcionamiento del algoritmo.

    No debe utilizarse en producción.
    """

    def __init__(self):

        # Primos pequeños para fines académicos
        self.p = 61
        self.q = 53

        self.n = self.p * self.q

        phi = (
            (self.p - 1)
            * (self.q - 1)
        )

        self.e = 17

        self.d = self._mod_inverse(
            self.e,
            phi
        )

    def _mod_inverse(
        self,
        e,
        phi
    ):

        for d in range(
            2,
            phi
        ):

            if (
                (e * d)
                % phi
                == 1
            ):
                return d

        raise ValueError(
            "No existe inverso modular"
        )

    def public_key(self):
        return (
            self.e,
            self.n
        )

    def private_key(self):
        return (
            self.d,
            self.n
        )

    def encrypt(
        self,
        message
    ):
        """
        Convierte cada carácter
        en su representación cifrada.
        """

        return [
            pow(
                ord(char),
                self.e,
                self.n
            )
            for char in message
        ]

    def decrypt(
        self,
        encrypted_message
    ):
        """
        Recupera el mensaje original.
        """

        return "".join(

            chr(
                pow(
                    value,
                    self.d,
                    self.n
                )
            )

            for value
            in encrypted_message
        )