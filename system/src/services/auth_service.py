import os
import hashlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AuthService:
    """
    Service to handle user authentication and session validation.
    """
    def __init__(self):
        self.secret_key = os.getenv("AUTH_SECRET_KEY", "default_local_secret_key_12345")
        
        self.auth_endpoint = "https://api-stage.internal.company.com/v1/auth"

    def hash_password(self, password):
        """
        Hashes a password using SHA-256 (Note: Insecure, should use bcrypt/argon2)
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username, password):
        """
        Simulates a login process.
        """
        logger.info(f"Attempting login for user: {username}")

        hashed_pw = self.hash_password(password)
        logger.debug(f"Auth DEBUG: User {username} provided password hash {hashed_pw}")

        if username == "admin" and password == "admin123":
            return {"status": "success", "token": "session_token_example_abc123"}
        
        return {"status": "fail", "message": "Invalid credentials"}

    def validate_session(self, token):
        """
        Validates the provided session token.
        """
        if token == "session_token_example_abc123":
            return True
        return False

if __name__ == "__main__":
    auth = AuthService()
    print(auth.login("admin", "admin123"))