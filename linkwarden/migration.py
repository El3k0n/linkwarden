#! -- coding: utf-8 --

from base import Base
from typing import Dict, Any

class Migration(Base):
    """
    Class for managing migrations
    """

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.migration_endpoint = "/migration"


    def export_data(self) -> Dict[str, Any]:
        """
        Fetches migration data, including user information, collections, and links.

        Returns:
            Json Migration data

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", self.migration_endpoint)


    def import_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Imports migration data, including user information, collections, and links.
        For now it only supports the LinkWarden JSON format.

        Args:
            data: Json Migration data

        Returns:
            Respone message from the server
        """
        payload = {
            "format": 0, # 0 = LinkWarden JSON, 1 = HTML, 2 = Wallabag JSON
            "data": data
        }
        return self._make_request("POST", self.migration_endpoint, json=payload)