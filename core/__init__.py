from utils import system_checks
# -*- coding: utf-8 -*-
"""Core module for video processing and watermark detection"""

from .processor import VideoProcessor
from .decoder import WatermarkDecoder

__all__ = ['VideoProcessor', 'WatermarkDecoder']
