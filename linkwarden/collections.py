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
    

    def create_collection(self, 
                            name: str, 
                            description: str = None, 
                            color: str = None, 
                            icon: str = None, 
                            iconWeight: str = None, 
                            parentId: int = None
                        ) -> Dict[str, Any]:
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
        payload = {k: v for k, v in locals().items() if k != "self" and v is not None}

        return self._make_request("POST", self.collections_endpoint, json=payload)
    

    def update_collection(self, 
                            id: int, 
                            name: str, 
                            members: list[Dict[str, Any]] = [],
                            description: str = None, 
                            color: str = None, 
                            icon: str = None, 
                            iconWeight: str = None, 
                            parentId: int = None,
                            isPublic: bool = None
                        ) -> Dict[str, Any]:
                        
        """
        Update a collection by ID

        Args:
            id (int, required): The ID of the collection to update
            name (str, required): The name of the collection
            members (List[Dict[str, Any]], required): The members of the collection
            description (str, optional): The description of the collection
            color (str, optional): The color of the collection
            icon (str, optional): The icon of the collection
            iconWeight (str, optional): The weight of the icon
            parentId (int, optional): The ID of the parent collection
            isPublic (bool, optional): Whether the collection is public
            
            NOTE: some fields are in camelCase because that's what the API expects
            
            The members field is a list of dictionaries with the following keys:
                - userId (int, required): The ID of the member
                - canCreate (bool, required): Whether the member can create links
                - canUpdate (bool, required): Whether the member can update links
                - canDelete (bool, required): Whether the member can delete links


        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """

        payload = {k: v for k, v in locals().items() if k != "self" and v is not None}

        return self._make_request("PUT", f"{self.collections_endpoint}/{id}", json=payload)
    

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
    
