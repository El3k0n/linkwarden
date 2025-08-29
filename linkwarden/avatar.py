#! -- coding: utf-8 --

from base import Base
from typing import Dict, Any

class Avatar(Base):
    """Class for managing avatars"""
    
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.avatars_endpoint = "/avatar"

    def get_avatar(self, user_id: str) -> Dict[str, Any]:
        """
        Get an avatar by ID

        Args:
            user_id: The ID of the user to get the avatar for

        Returns:
            Avatar image

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.avatars_endpoint}/{user_id}")