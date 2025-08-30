#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any, Optional

class Public(Base):
    """
    Class for managing public endpoints
    """

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.public_endpoint = "/public"


    def get_links_from_collection(self, 
                                  collection_id: int,
                                  sort: Optional[int] = None,
                                  cursor: Optional[int] = None,
                                  pinnedOnly: Optional[bool] = None,
                                  searchQueryString: Optional[str] = None,
                                  searchByName: Optional[bool]   = None,
                                  searchByUrl: Optional[bool] = None,
                                  searchByDescription: Optional[bool] = None,
                                  searchByTextContent: Optional[bool] = None,
                                  searchByTags: Optional[bool] = None
                                  ) -> Dict[str, Any]:
        """
        Get links from a specific collection

        Args:
            collection_id: The ID of the collection to get links from (required)
            sort: The sort order of the links (optional)
            cursor: The cursor to get the next page of links (optional)
            pinnedOnly: Whether to only get pinned links (optional)
            searchQueryString: The search query string (optional)
            searchByName: Whether to search by name (optional)
            searchByUrl: Whether to search by URL (optional)
            searchByDescription: Whether to search by description (optional)
            searchByTextContent: Whether to search by text content (optional)
            searchByTags: Whether to search by tags (optional)

        Returns:
            List of link dictionaries (each link is a dictionary)

        Raises:
            APIError: If the API request fails
        """
        parameters = {k: v for k, v in locals().items() if k != "self" and v is not None}

        return self._make_request("GET", f"{self.public_endpoint}/collections/links", params=parameters)
    

    def get_tags_from_collection(self, collection_id: int) -> Dict[str, Any]:
        """
        Get tags from a specific collection

        Args:
            collection_id: The ID of the collection to get tags from (required)

        Returns:
            List of tag dictionaries (each tag is a dictionary)

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.public_endpoint}/collections/tags", params={"collectionId": collection_id})


    def get_user_by_id(self, user_id: int) -> Dict[str, Any]:
        """
        Get a user by ID

        Args:
            user_id: The ID of the user to get (required)

        Returns:
            User dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.public_endpoint}/users/{user_id}")


    def get_link_by_id(self, link_id: int) -> Dict[str, Any]:
        """
        Get a link by ID

        Args:
            link_id: The ID of the link to get (required)

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.public_endpoint}/links/{link_id}")


    def get_collection_by_id(self, collection_id: int) -> Dict[str, Any]:
        """
        Get a collection by ID

        Args:
            collection_id: The ID of the collection to get (required)

        Returns:
            Collection dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.public_endpoint}/collections/{collection_id}")