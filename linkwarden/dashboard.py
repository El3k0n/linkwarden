#! -- coding: utf-8 --

from typing import Dict, Any
from .base import Base


class Dashboard(Base):
    """Get Dashboard data for the user"""

    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.dashboard_endpoint = "/dashboard"


    def get_current_user_dashboard(self) -> Dict[str, Any]:
        """
        Get Dashboard data for the user

        Returns:
            Dashboard data

        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", self.dashboard_endpoint)