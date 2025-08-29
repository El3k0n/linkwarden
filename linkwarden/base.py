#! -- coding: utf-8 --

import requests
from typing import Dict, Any

class APIError(Exception):
    """Custom exception for API errors"""
    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class Base:
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        self.api_key = api_key
        self.api_version = api_version
        self.base_url = base_url + "/api/" + api_version
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Generic method to make HTTP requests with error handling"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                raise APIError(f"API request failed: {e}", e.response.status_code)
            raise APIError(f"Network error: {e}")

        
