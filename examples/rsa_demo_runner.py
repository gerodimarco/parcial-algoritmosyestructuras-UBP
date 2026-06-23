from advanced_algorithms.rsa_demo import RSADemo


def main():

    print("=" * 50)
    print("DEMO - RSA EDUCATIVO")
    print("=" * 50)

    rsa = RSADemo()

    message = "ALERTA"

    print("\nMensaje original:")
    print(message)

    print("\nClave pública:")
    print(rsa.public_key())

    print("\nClave privada:")
    print(rsa.private_key())

    encrypted = rsa.encrypt(message)

    print("\nMensaje cifrado:")
    print(encrypted)

    decrypted = rsa.decrypt(encrypted)

    print("\nMensaje descifrado:")
    print(decrypted)

    print("\nVerificación:")

    if decrypted == message:
        print("✓ El mensaje fue recuperado correctamente.")
    else:
        print("✗ Error en el proceso de cifrado/descifrado.")


if __name__ == "__main__":
    main()
    