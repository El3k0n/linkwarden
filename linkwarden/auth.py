#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Auth(Base):
    """
    Class for managing authentication
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.auth_endpoint = "/auth"
    
    
    def forgot_password(self, email: str) -> Dict[str, Any]:
        """
        Forgot password

        Args:
            email: The email to reset the password for

        Returns:
            API response
        
        Raises:
            APIError: If the request fails
        """
        return self._make_request("POST", f"{self.auth_endpoint}/forgot-password", data={"email": email})
    
    
    def reset_password(self, token: str, new_password: str) -> Dict[str, Any]:
        """
        Reset password

        Args:
            token: The password reset token
            new_password: The new password to set

        Returns:
            API response
        
        Raises:
            APIError: If the request fails
        """
        return self._make_request("POST", f"{self.auth_endpoint}/reset-password", data={"token": token, "password": new_password})


    def verify_email(self, token: str) -> Dict[str, Any]:
        """
        Verify email

        Args:
            token: The email verification token

        Returns:
            API response
        
        Raises:
            APIError: If the request fails
        """
        return self._make_request("POST", f"{self.auth_endpoint}/verify-email", data={"token": token})