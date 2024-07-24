from cryptography.fernet import Fernet
from utils.contants import Constants
class CommonUtils:
    def __init__(self):
        self.key = Constants.ENCRYPT_DECRYPT_KEY
        self.cipher_suite = Fernet(self.key)
    
    def encrypt_password(self, password: str) -> str:
        encrypted_password = self.cipher_suite.encrypt(password.encode('utf-8'))
        return encrypted_password.decode('utf-8')
    
    def decrypt_password(self, encrypted_password: str) -> str:
        decrypted_password = self.cipher_suite.decrypt(encrypted_password.encode('utf-8'))
        return decrypted_password.decode('utf-8')

    def get_key(self) -> str:
        return self.key.decode('utf-8')

    def set_key(self, key: str):
        self.cipher_suite = Fernet(key.encode('utf-8'))