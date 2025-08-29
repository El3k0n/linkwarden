#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Collections(Base):
    """Class for managing collections"""

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.collections_endpoint = "/collections"


    def get_collections(self) -> Dict[str, Any]:
        """
        Get all collections

        Returns:
            List of collection dictionaries

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", self.collections_endpoint)
    

    def get_collection(self, id: int) -> Dict[str, Any]:
        """
        Get a collection by ID

        Args:
            id: The ID of the collection to get

        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.collections_endpoint}/{id}")
    

    def create_collection(self, name: str, description: str = "", 
                            color: str = "", icon: str = "", iconWeight: str = "", 
                            parentId: int = None) -> Dict[str, Any]:
        """
        Create a collection

        Args:
            name: The name of the collection (required)
            description: The description of the collection (optional)
            color: The color of the collection (optional)
            icon: The icon of the collection (optional)
            iconWeight: The weight of the icon (optional)
            parentId: The ID of the parent collection (optional)

        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """
        payload = {
            "name": name,
            "description": description,
            "color": color,
            "icon": icon,
            "iconWeight": iconWeight,
            "parentId": parentId
        }

        return self._make_request("POST", self.collections_endpoint, json=payload)
    

    def update_collection(self, id: int, **kwargs) -> Dict[str, Any]:
        """
        Update a collection by ID

        Args:
            id: The ID of the collection to update
            **kwargs: Fields to update, only the provided fields will be updated
            Updateable fields: 
                - name 
                - description
                - color
                - icon
                - iconWeight
                - parentId 
                - isPublic

        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("PUT", f"{self.collections_endpoint}/{id}", json=kwargs)
    

    def delete_collection(self, id: int) -> Dict[str, Any]:
        """
        Delete a collection by ID

        Args:
            id: The ID of the collection to delete

        Returns:
            API response

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("DELETE", f"{self.collections_endpoint}/{id}")
    
