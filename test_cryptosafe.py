# test_cryptosafe.py
"""
Tests for CryptoSafe module.
"""

import unittest
from cryptosafe import CryptoSafe

class TestCryptoSafe(unittest.TestCase):
    """Test cases for CryptoSafe class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoSafe()
        self.assertIsInstance(instance, CryptoSafe)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoSafe()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
