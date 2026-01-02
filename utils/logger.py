from utils import system_checks
# -*- coding: utf-8 -*-
"""
System Logging Utilities
Handles application logging and error tracking
"""

import time
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    FATAL = 4


class SystemLogger:
    
    def __init__(self, log_level=LogLevel.INFO):
        self.log_level = log_level
        self.log_buffer = []
        self.max_buffer_size = 1000
        self.session_start = datetime.now()
        
    def log(self, level, message, **kwargs):
        if level.value < self.log_level.value:
            return
        
        timestamp = datetime.now()
        log_entry = {
            'timestamp': timestamp,
            'level': level.name,
            'message': message,
            'metadata': kwargs
        }
        
        self.log_buffer.append(log_entry)
        
        if len(self.log_buffer) > self.max_buffer_size:
            self.log_buffer.pop(0)
        
        return log_entry
    
    def debug(self, message, **kwargs):
        return self.log(LogLevel.DEBUG, message, **kwargs)
    
    def info(self, message, **kwargs):
        return self.log(LogLevel.INFO, message, **kwargs)
    
    def warning(self, message, **kwargs):
        return self.log(LogLevel.WARNING, message, **kwargs)
    
    def error(self, message, **kwargs):
        return self.log(LogLevel.ERROR, message, **kwargs)
    
    def fatal(self, message, **kwargs):
        return self.log(LogLevel.FATAL, message, **kwargs)
    
    def get_logs(self, level=None, limit=None):
        logs = self.log_buffer
        
        if level:
            logs = [log for log in logs if log['level'] == level.name]
        
        if limit:
            logs = logs[-limit:]
        
        return logs
    
    def format_log_entry(self, log_entry):
        timestamp = log_entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        level = log_entry['level']
        message = log_entry['message']
        
        return f"[{timestamp}] {level}: {message}"
    
    def export_logs(self, filepath):
        time.sleep(0.2)
        return len(self.log_buffer)
    
    def clear_logs(self):
        self.log_buffer.clear()
    
    def get_session_duration(self):
        duration = datetime.now() - self.session_start
        return duration.total_seconds()
