#! -- coding: utf-8 --

from base import Base
from typing import Dict, Any

class Links(Base):
    """
    Class for managing links
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.links_endpoint = "/links"

    def get_link(self, link_id: str) -> Dict[str, Any]:
        """
        Get a link by ID

        Args:
            link_id: The ID of the link to get

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.links_endpoint}/{link_id}")
    
    def create_link(self, link: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a link

        Args:
            link: Link dictionary

        Returns:
            Link dictionary

        Raises:
            APIError: If the API request fails
        """
        #TODO: Implement
        #TODO: usare variabili del body predefinite invece che un generico dict? con dataclass?
        #name, url, type (url, pdf, image), description, tags [], collection []
        pass