#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Search(Base):
    """
    Class for searching
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.search_endpoint = "/search"

    
    def search_links(self, query: str, cursor: int = 0) -> Dict[str, Any]:
        """
        Search for links

        Args:
            query: The query to search for
            cursor: The cursor to use for pagination
            NOTE: the API documentation features a "sort" int parameter, but its possible values are nowhere to be found. 
            I decided to not include it for now.

        Returns:
            Search results
        
        Raises:
            APIError: If the request fails
        """
        return self._make_request("GET", f"{self.search_endpoint}", params={"searchQueryString": query, "cursor": cursor})
    
    