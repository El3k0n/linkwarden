#! -- coding: utf-8 --

from base import Base
from typing import Dict, Any

class Search(Base):
    """
    Class for searching
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.search_endpoint = "/search"