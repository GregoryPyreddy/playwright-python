import bcrypt
from cryptography.fernet import Fernet

# # Function to encrypt a password
# def encrypt_password(password: str) -> str:
#     # Generate a salt
#     salt = bcrypt.gensalt()
#     # Hash the password
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed_password.decode('utf-8')

# # Example usage
# password = "Sid@1806"
# encrypted_password = encrypt_password(password)
# print(f"Encrypted password: {encrypted_password}")


key = "QSrcwaqzESOSuVxoDVN5Z5nEHBuysWicCxie8BfiRek="
_cipher_suite = Fernet(key)
# encrypted_password = _cipher_suite.encrypt("Sid@1806".encode('utf-8'))
# print(encrypted_password)
decrypted_password = _cipher_suite.decrypt("gAAAAABmnwtLgeR74YGFDtsoUwj68toMEDrWa8RgEKnGUa7QKRFcBJk5EuO8W_HiAbjSdUi_zelajQW2I_-R-3mpgJfHtCYKJQ==".encode('utf-8'))
print(decrypted_password.decode('utf-8'))