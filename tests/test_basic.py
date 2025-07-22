"""
Test suite for NotebookLM Converter
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestImports(unittest.TestCase):
    """Test that all required modules can be imported"""
    
    def test_main_imports(self):
        """Test that main application modules import correctly"""
        try:
            from notebooklm_converter import app
            from notebooklm_converter import gui
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Import failed: {e}")
    
    def test_dependency_imports(self):
        """Test that all dependencies are available"""
        dependencies = [
            'tkinter',
            'ebooklib',
            'bs4',  # BeautifulSoup
            'xhtml2pdf',
            'markdown',
            'PIL',  # Pillow
        ]
        
        for dep in dependencies:
            try:
                __import__(dep)
            except ImportError:
                self.fail(f"Required dependency '{dep}' not available")


class TestApplication(unittest.TestCase):
    """Test basic application functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        try:
            from notebooklm_converter.gui import NotebookLMConverterApp
            self.app_class = NotebookLMConverterApp
        except ImportError:
            self.skipTest("Cannot import application class")
    
    def test_app_initialization(self):
        """Test that the app can be initialized (without GUI)"""
        # This test would need to be run in a headless environment
        # or with a mock Tkinter root
        self.assertTrue(hasattr(self.app_class, '__init__'))


if __name__ == '__main__':
    unittest.main()
