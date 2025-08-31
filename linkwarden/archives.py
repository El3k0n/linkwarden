#! -- coding: utf-8 --

from .base import Base
from typing import Dict, Any, BinaryIO
import os

class Archives(Base):
    """
    Class for managing archives
    """
    def __init__(self, api_key: str, base_url: str="https://cloud.linkwarden.app", api_version: str="v1"):
        super().__init__(api_key, base_url, api_version)
        self.archives_endpoint = "/archives"


    def get_archive_by_link_id(self, 
                               link_id: int,
                               format: int
                            ) -> Dict[str, Any]:
        """
        Get an archive file by link ID

        Args:
            link_id (int, required): The ID of the link to get the archive for
            format (int, required): The format of the archive to get (0 = PNG, 1 = JPEG, 2 = PDF, 3 = JSON, 4 = HTML)
            NOTE: The API also supports a preview parameter, but I still wasn't able to get how it works. When I pass it, it only returns JPEGs

        Returns:
            Archive in the selected format

        Raises:
            APIError: If the API request fails
            ValueError: If the format is invalid
        """
        if format not in [0, 1, 2, 3, 4]:
            raise ValueError("Invalid format. Valid formats are: 0 = PNG, 1 = JPEG, 2 = PDF, 3 = JSON, 4 = HTML")
        
        return self._make_request("GET", f"{self.archives_endpoint}/{link_id}", params={"format": format})
    

    def upload_file_to_archive(self, 
                               link_id: int,
                               file_path: str,
                               format: int
                               ) -> Dict[str, Any]:
        """
        Upload a file to an archive providing file path

        Args:
            link_id: The ID of the link to upload the file to
            file_path: The path to the file to upload
            format: The format of the file to upload (0 = PNG, 1 = JPEG, 2 = PDF)

        Returns:
            Archive file

        Raises:
            APIError: If the API request fails
            ValueError: If the format is invalid
        """
        if format not in [0, 1, 2]:
            raise ValueError("Invalid format. Valid formats are: 0 = PNG, 1 = JPEG, 2 = PDF")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if not os.path.isfile(file_path):
            raise ValueError(f"Path is not a file: {file_path}")

        with open(file_path, 'rb') as file_object:
            files = {
                'file': (
                    os.path.basename(file_path),  
                    file_object,                   
                    'application/octet-stream'  
                )
            }
            
            params = {"format": format}
            
            return self._make_request("POST", f"{self.archives_endpoint}/{link_id}", files=files, params=params)
        
    
    def upload_file_object_to_archive(self, 
                                      link_id: int,
                                      file_object: BinaryIO,
                                      filename: str,
                                      format: int,
                                      ) -> Dict[str, Any]:
        """
        Upload a file to an archive providing file object

        Args:
            link_id: The ID of the link to upload the file to
            file_object: The file object to upload
            filename: The name of the file to upload
            format: The format of the file to upload (0 = PNG, 1 = JPEG, 2 = PDF)

        Returns:
            Archive file

        Raises:
            APIError: If the API request fails
            ValueError: If the format is invalid
        """
        if format not in [0, 1, 2]:
            raise ValueError("Invalid format. Valid formats are: 0 = PNG, 1 = JPEG, 2 = PDF")
        
        if not hasattr(file_object, 'read'):
            raise ValueError("File_object must be a readable file object")
        
        if 'b' not in getattr(file_object, 'mode', ''):
            raise ValueError("File must be opened in binary mode ('rb')")
        
        files = {
            'file': (
                filename,
                file_object,
                'application/octet-stream'
            )
        }
        
        params = {"format": format}
        
        return self._make_request("POST", f"{self.archives_endpoint}/{link_id}", files=files, params=params)

    
    def update_archive_file(self):
        pass