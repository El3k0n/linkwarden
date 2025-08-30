#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any, Optional, List

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
                    name: str, 
                    url: str, 
                    collection: Dict[str, Any],
                    tags: List[Dict[str, Any]] = [],
                    description: Optional[str] = None, 
                    icon: Optional[str] = None,
                    iconWeight: Optional[str] = None,
                    color: Optional[str] = None,
                    pinnedBy: Optional[List[int]] = None,
                ) -> Dict[str, Any]:
        """
        Update a link by ID

        Args:
            id (int, required): The ID of the link to update
            name (str, required): The name of the link
            url (str, required): The URL of the link
            collection (Dict[str, Any], required): The collection of the link, must include id, name and ownerId
            tags (List[Dict[str, Any]], required): The tags of the link
            description (str, optional): The description of the link
            icon (str, optional): The icon of the link
            iconWeight (str, optional): The weight of the icon
            color (str, optional): The color of the link
            pinnedBy (List[int], optional): The user who pinned the link

            NOTE: some fields are in camelCase because that's what the API expects

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        payload = {k: v for k, v in locals().items() if k != "self" and v is not None}

        print(payload)
        
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


    def bulk_update_links(self, 
                    links: list[Dict[str, Any]], 
                    collection_id: int, 
                    remove_previous_tags: bool = False, 
                    new_tags: list[Dict[str, Any]] = None,
                    ) -> Dict[str, Any]:
        """
        Bulk update links

        Args:
            links: List of link objects
            remove_previous_tags: Whether to remove previous tags
            collection_id: The ID of the collection to update
            new_tags: List of tag objects

        Returns:
            API response
        
        Raises:
            APIError: If the request fails
        """
        payload = {
            "links": links,
            "removePreviousTags": remove_previous_tags,
            "newData": {
                "collectionId": collection_id,
                "tags": new_tags
            }
        }
        return self._make_request("PUT", self.links_endpoint, json=payload)