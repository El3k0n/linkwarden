#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any, Optional

class Tokens(Base):
    """
    Class for managing tokens
    """

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.tokens_endpoint = "/tokens"


    def get_tokens(self) -> Dict[str, Any]:
        """
        Get all tokens for the current user

        Returns:
            List of token dictionaries

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", self.tokens_endpoint)
    

    def create_token(self, name: str, expires: int) -> Dict[str, Any]:
        """
        Create a new token

        Args:
            name: The name of the token
            expires: The number of seconds until the token expires, 0 for no expiration

        Returns:
            Token dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("POST", self.tokens_endpoint, json={"name": name, "expires": expires})
    

    def revoke_token(self, token_id: int) -> Dict[str, Any]:
        """
        Revoke a token

        Args:
            token_id: The ID of the token to revoke

        Returns:
            Token dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("DELETE", f"{self.tokens_endpoint}/{token_id}")