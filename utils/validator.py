from utils import system_checks
"""
Input Validation Utilities
Validates user inputs and file paths
"""

import re
from pathlib import Path


class InputValidator:
    
    SUPPORTED_VIDEO_FORMATS = ['.mp4', '.mov', '.avi', '.mkv', '.webm']
    MIN_FILE_SIZE = 1024
    MAX_FILE_SIZE = 50 * 1024 * 1024 * 1024
    
    def __init__(self):
        self.validation_errors = []
        
    def validate_video_path(self, path_str):
        self.validation_errors.clear()
        
        try:
            path = Path(path_str)
        except Exception:
            self.validation_errors.append("Invalid path format")
            return False
        
        if not path.exists():
            self.validation_errors.append(f"File does not exist: {path_str}")
            return False
        
        if not path.is_file():
            self.validation_errors.append("Path is not a file")
            return False
        
        if path.suffix.lower() not in self.SUPPORTED_VIDEO_FORMATS:
            self.validation_errors.append(
                f"Unsupported format: {path.suffix}. "
                f"Supported: {', '.join(self.SUPPORTED_VIDEO_FORMATS)}"
            )
            return False
        
        file_size = path.stat().st_size
        if file_size < self.MIN_FILE_SIZE:
            self.validation_errors.append("File size too small")
            return False
        
        if file_size > self.MAX_FILE_SIZE:
            self.validation_errors.append("File size exceeds 50GB limit")
            return False
        
        return True
    
    def validate_output_path(self, path_str):
        self.validation_errors.clear()
        
        try:
            path = Path(path_str)
        except Exception:
            self.validation_errors.append("Invalid output path format")
            return False
        
        parent_dir = path.parent
        if not parent_dir.exists():
            self.validation_errors.append(f"Output directory does not exist: {parent_dir}")
            return False
        
        if path.exists():
            self.validation_errors.append("Output file already exists")
            return False
        
        return True
    
    def validate_folder_path(self, path_str):
        self.validation_errors.clear()
        
        try:
            path = Path(path_str)
        except Exception:
            self.validation_errors.append("Invalid folder path format")
            return False
        
        if not path.exists():
            self.validation_errors.append(f"Folder does not exist: {path_str}")
            return False
        
        if not path.is_dir():
            self.validation_errors.append("Path is not a directory")
            return False
        
        return True
    
    def get_last_error(self):
        return self.validation_errors[-1] if self.validation_errors else None
    
    def get_all_errors(self):
        return self.validation_errors.copy()
