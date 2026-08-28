# test_sparkquill.py
"""
Tests for SparkQuill module.
"""

import unittest
from sparkquill import SparkQuill

class TestSparkQuill(unittest.TestCase):
    """Test cases for SparkQuill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SparkQuill()
        self.assertIsInstance(instance, SparkQuill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SparkQuill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
