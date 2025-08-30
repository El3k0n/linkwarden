#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any, Optional

class Links(Base):
    """
    Class for managing links
    """

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.links_endpoint = "/links"


    def get_link(self, id: int) -> Dict[str, Any]:
        """
        Get a link by ID

        Args:
            id: The ID of the link to get

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.links_endpoint}/{id}")
    

    def create_link(self, 
                    name: Optional[str] = None, 
                    url: Optional[str] = None, 
                    type: Optional[str] = None, 
                    description: Optional[str] = None, 
                    tags: Optional[list[Dict[str, Any]]] = None, 
                    collection: Optional[Dict[str, Any]] = None
                    ) -> Dict[str, Any]:
        """
        Create a link
        #TODO: make more user friendly with wrapper classes for tags and collections or TypedDicts

        Args:
            NOTE: all of the arguments are optional
            name: The name of the link
            url: The URL of the link
            type: The type of the link (url, pdf, image)
            description: The description of the link
            tags: List of tag objects with id and name (optional)
            collection: Collection object with id and name (optional)

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        if type and not type in ["url", "pdf", "image"]:
            raise ValueError("Invalid link type")
        
        payload = {k: v for k, v in locals().items() if k != "self" and v is not None}
        
        return self._make_request("POST", self.links_endpoint, json=payload)


    def update_link(self, 
                    id: int, 
                    name: Optional[str] = None, 
                    url: Optional[str] = None, 
                    description: Optional[str] = None, 
                    icon: Optional[str] = None,
                    iconWeight: Optional[str] = None,
                    color: Optional[str] = None,
                    tags: Optional[list[Dict[str, Any]]] = None, 
                    collection: Optional[Dict[str, Any]] = None,
                    pinnedBy: Optional[int] = None,
                    ) -> Dict[str, Any]:
        """
        Update a link by ID

        Args:
            id: The ID of the link to update
            Only the provided fields will be updated
            Updateable fields: 
                - name 
                - url
                - description
                - icon
                - iconWeight
                - color
                - tags
                - collection
                - pinnedBy

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        payload = {k: v for k, v in locals().items() if k != "self" and v is not None}
        
        return self._make_request("PUT", f"{self.links_endpoint}/{id}", json=payload)


    def archive_link(self, id: int) -> Dict[str, Any]:
        """
        Archive a link by ID

        Args:
            id: The ID of the link to archive

        Returns:
            API response

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("PUT", f"{self.links_endpoint}/{id}/archive")
    

    def delete_link(self, id: int) -> Dict[str, Any]:
        """
        Delete a link by ID

        Args:
            id: The ID of the link to delete

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("DELETE", f"{self.links_endpoint}/{id}")

    
    def delete_link_list(self, ids: list[int]) -> Dict[str, Any]:
        """
        Delete a list of links by IDs

        Args:
            ids: List of int IDs of the links to delete

        Returns:
            Count of deleted links

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("DELETE", self.links_endpoint, json={"linkIds": ids})


    def bulk_update_links(self):
        #TODO: implement bulk update links
        pass