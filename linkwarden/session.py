#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Session(Base):
    """
    Class for managing sessions
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.session_endpoint = "/session"

    def create_session(self, username: str, password: str, session_name: str) -> Dict[str, Any]:
        """
        Create a session

        Args:
            username: The username to create the session for
            password: The password to create the session for
            session_name: The name of the session to create

        Returns:
            The created session token

        Raises:
            APIError: If the request fails
        """
        return self._make_request("POST", f"{self.session_endpoint}", data={"username": username, "password": password, "sessionName": session_name})
    