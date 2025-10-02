# test_thresholdsignature.py
"""
Tests for ThresholdSignature module.
"""

import unittest
from thresholdsignature import ThresholdSignature

class TestThresholdSignature(unittest.TestCase):
    """Test cases for ThresholdSignature class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThresholdSignature()
        self.assertIsInstance(instance, ThresholdSignature)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThresholdSignature()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
