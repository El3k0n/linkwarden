#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Tags(Base):
    """Class for managing tags"""

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.tags_endpoint = "/tags"

    def get_tags(self) -> Dict[str, Any]:
        """
        Get all tags

        Returns:
            List of tag dictionaries

        Raises:
            APIError: If the API request fails
        """ 
        return self._make_request("GET", self.tags_endpoint)

    def get_tag(self, tag_id: str) -> Dict[str, Any]:
        """
        Get a tag by ID

        Args:
            tag_id: The ID of the tag to get

        Returns:
            Tag dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.tags_endpoint}/{tag_id}")
    
    def update_tag(self, tag_id: str, name: str) -> Dict[str, Any]:
        """
        Update a tag name by ID

        Args:
            tag_id: The ID of the tag to update
            name: The new name of the tag

        Returns:
            Tag dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("PUT", f"{self.tags_endpoint}/{tag_id}", json={"name": name})
    
    def delete_tag(self, tag_id: str) -> Dict[str, Any]:
        """
        Delete a tag

        Args:
            tag_id: The ID of the tag to delete

        Returns:
            Tag dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("DELETE", f"{self.tags_endpoint}/{tag_id}")