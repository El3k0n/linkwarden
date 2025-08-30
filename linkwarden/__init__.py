#! -- coding: utf-8 --
"""
Linkwarden API Python Wrapper
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
from .tokens import Tokens
from .archives import Archives
from .session import Session
from .auth import Auth
from .logins import Logins

class Api:
    """
    Main API client for Linkwarden

    This class provides access to all Linkwarden API resources through
    specialized classes for each endpoint.

    Attributes:
        users: Users management (create, read, update, delete users)
        links: Links management (create, read, update, delete links)
        collections: Collections management (create, read, update, delete collections)
        tags: Tags management (read, update, delete tags)
        archives: Archive management (upload, download files)
        search: Search functionality
        avatar: User avatar management
        migration: Data export/import
        dashboard: Current user's dashboard information
        public: Public endpoints (no authentication required)
        tokens: API token management
        auth: Authentication (password reset, email verification)
        session: Session management
        logins: Login configuration
    """
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
        self.tokens = Tokens(api_key, base_url, api_version)
        self.archives = Archives(api_key, base_url, api_version)
        self.session = Session(api_key, base_url, api_version)
        self.auth = Auth(api_key, base_url, api_version)
        self.logins = Logins(api_key, base_url, api_version)

    def __dir__(self):
        return [
            'users', 'links', 'collections', 'tags', 'archives',
            'search', 'avatar', 'migration', 'dashboard', 'public',
            'tokens', 'auth', 'session', 'logins'
        ]


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
    "Public",
    "Tokens",
    "Archives",
    "Session",
    "Auth",
    "Logins"
]