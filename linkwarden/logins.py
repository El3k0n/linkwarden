#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Logins(Base):
    """
    Class for managing login configuration

    It's initialized with the API key even though it's not needed because 
    I'm lazy and don't want to create a new class for this =)
    If needed, it can safely be initialized with an empty string for the API key
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.logins_endpoint = "/logins"

    def get_login_configuration(self) -> Dict[str, Any]:
        """
        Get the login configuration for the application

        Returns:
            Login configuration dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", self.logins_endpoint)
    
