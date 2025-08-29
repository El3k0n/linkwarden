#! -- coding: utf-8 --

from base import Base
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
    
    def get_collection(self, collection_id: str) -> Dict[str, Any]:
        """
        Get a collection by ID

        Args:
            collection_id: The ID of the collection to get

        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.collections_endpoint}/{collection_id}")
    
    def create_collection(self, collection: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a collection

        Args:
            collection: Collection dictionary

        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """
        #TODO: Anche qui usare variabili del body predefinite invece che un generico dict? con dataclass?
        #name, description, color, icon, iconWeight, parentId