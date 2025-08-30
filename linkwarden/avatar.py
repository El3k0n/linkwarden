#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any
import requests

class Avatar(Base):
    """Class for managing avatars"""
    
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.avatars_endpoint = "/avatar"


    def get_avatar(self, user_id: int) -> Dict[str, Any]:
        """
        Get an avatar by ID

        Args:
            user_id: The ID of the user to get the avatar for

        Returns:
            Binary avatar image

        Raises:
            APIError: If the API request fails
        """
        #We can't use the _make_request method because the response is binary data
        url = f"{self.base_url}/{self.avatars_endpoint}/{user_id}"

        try:
            response = requests.request("GET", url, headers=self.headers)
            response.raise_for_status()
            
            # For avatars, we return binary data instead of JSON
            return response.content
            
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                raise self.APIError(f"API request failed: {e}", e.response.status_code)
            raise self.APIError(f"Network error: {e}")