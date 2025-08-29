#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any

class Users(Base):
    """
    Class for managing users
    For now it only manages basic user data like name, password, email and username.
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.users_endpoint = "/users"
        
    def get_users(self):
        """
        Get all users
        
        Returns:
            List of user dictionaries
            
        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", self.users_endpoint)


    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        Get a user by ID
        
        Args:
            user_id: The user ID to get
            
        
        Returns:
            User dictionary
            
        Raises:
            APIError: If the API request fails
        """
        return self._make_request("GET", f"{self.users_endpoint}/{user_id}")


    def create_user(self, name: str, password: str, email: str="", username: str="", invite: bool=False) -> Dict[str, Any]:
        """
        Create a new user
        
        Args:
            name: User's name (max 50 chars)
            password: User's password (min 8 chars)
            email: User's email (optional, max 255 chars)
            username: User's username (optional, 3-50 chars)
            invite: Whether to send an invite email
            
        Returns:
            Created user dictionary
            
        Raises:
            ValueError: If validation fails
            APIError: If the API request fails
        """
        self._validate_user_data(name, password, email, username)
        
        payload = {
            "name": name,
            "password": password,
            "email": email,
            "username": username,
            "invite": invite
        }
        
        return self._make_request("POST", self.users_endpoint, json=payload)

        
    def update_user(self, user_id: str, **kwargs) -> Dict[str, Any]:
        """
        Update a user
        
        Args:
            user_id: The user ID to update
            **kwargs: Fields to update (name, password, email, username)
            
        Returns:
            Updated user dictionary
            
        Raises:
            ValueError: If validation fails
            APIError: If the API request fails
        """
        # Validate only the fields that are being updated
        if 'name' in kwargs:
            self._validate_name(kwargs['name'])
        if 'password' in kwargs:
            self._validate_password(kwargs['password'])
        if 'email' in kwargs:
            self._validate_email(kwargs['email'])
        if 'username' in kwargs:
            self._validate_username(kwargs['username'])
        
        return self._make_request("PUT", f"{self.users_endpoint}/{user_id}", json=kwargs)


    def delete_user(self, user_id: str) -> Dict[str, Any]:
        """
        Delete a user
        
        Args:
            user_id: The user ID to delete
            
        Returns:
            Deleted user dictionary
            
        Raises:
            APIError: If the API request fails
        """
        return self._make_request("DELETE", f"{self.users_endpoint}/{user_id}")


    def _validate_user_data(self, name: str, password: str, email: str = "", username: str = ""):
        """Validate user data for creation"""
        if not email or username:
            raise ValueError("At least one of email or username is required")
        
        self._validate_name(name)
        self._validate_password(password)
        if email:
            self._validate_email(email)
        if username:
            self._validate_username(username)
    

    def _validate_name(self, name: str):
        """Validate user name"""
        if not name:
            raise ValueError("Name cannot be empty")
        if len(name) > 50:
            raise ValueError("Name must be less than 50 characters")
    

    def _validate_password(self, password: str):
        """Validate user password"""
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
    

    def _validate_email(self, email: str):
        """Validate email address"""
        if len(email) > 255:
            raise ValueError("Email must be less than 255 characters")
        #TODO: Add more mail validation ?
    

    def _validate_username(self, username: str):
        """Validate username"""
        if len(username) < 3 or len(username) > 50:
            raise ValueError("Username must be between 3 and 50 characters")