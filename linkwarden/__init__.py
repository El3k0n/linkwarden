#! -- coding: utf-8 --
"""
Linkwarden API Python Wrapper

A simple and intuitive Python wrapper for the Linkwarden API.
"""

from .base import Base
from .users import Users
from .tags import Tags
from .collections import Collections
from .avatar import Avatar
from .migration import Migration
from .links import Links
from .search import Search
from .dashboard import Dashboard
from .public import Public

class Api:
    """Main API class"""
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        self.users = Users(api_key, base_url, api_version)
        self.tags = Tags(api_key, base_url, api_version)
        self.collections = Collections(api_key, base_url, api_version)
        self.avatar = Avatar(api_key, base_url, api_version)
        self.migration = Migration(api_key, base_url, api_version)
        self.links = Links(api_key, base_url, api_version)
        self.search = Search(api_key, base_url, api_version)
        self.dashboard = Dashboard(api_key, base_url, api_version)
        self.public = Public(api_key, base_url, api_version)

__all__ = [
    "Api",
    "Base", 
    "Users",
    "Tags",
    "Collections",
    "Avatar",
    "Migration",
    "Links",
    "Search",
    "Dashboard",
    "Public"
]