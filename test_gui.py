"""
Standalone GUI test for NotebookLM Converter.
Run this to test if GUI works on your system.
"""

import sys
import traceback

def test_tkinter():
    """Test basic tkinter functionality."""
    try:
        print("Testing tkinter import...")
        import tkinter as tk
        print("✓ tkinter imported successfully")
        
        print("Testing window creation...")
        root = tk.Tk()
        root.title("NotebookLM Converter - GUI Test")
        root.geometry("400x300")
        
        # Create test widgets
        label = tk.Label(root, text="GUI Test Successful!", font=("Arial", 16))
        label.pack(pady=20)
        
        button = tk.Button(root, text="Close Test", command=root.quit)
        button.pack(pady=10)
        
        text = tk.Text(root, height=5, width=40)
        text.pack(pady=10)
        text.insert("1.0", "If you see this window, tkinter is working!\n\nNotebookLM Converter GUI should work on your system.")
        
        print("✓ Test window created successfully")
        print("✓ Opening GUI test window...")
        
        # Show window
        root.lift()
        root.focus_force()
        root.mainloop()
        
        print("✓ GUI test completed successfully")
        return True
        
    except Exception as e:
        print(f"✗ tkinter test failed: {e}")
        traceback.print_exc()
        return False

def test_notebooklm_gui():
    """Test NotebookLM Converter GUI components."""
    try:
        print("\nTesting NotebookLM Converter GUI...")
        
        # Add src to path
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
        
        from src.notebooklm_converter.gui import NotebookLMConverterApp
        print("✓ NotebookLM GUI module imported successfully")
        
        import tkinter as tk
        root = tk.Tk()
        root.title("NotebookLM Converter")
        
        print("✓ Creating NotebookLM Converter app...")
        app = NotebookLMConverterApp(root)
        print("✓ NotebookLM Converter app created successfully")
        
        # Show window
        root.lift()
        root.focus_force()
        root.mainloop()
        
        print("✓ NotebookLM Converter GUI test completed")
        return True
        
    except Exception as e:
        print(f"✗ NotebookLM GUI test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all GUI tests."""
    print("NotebookLM Converter - GUI Test Suite")
    print("=" * 40)
    
    # Test 1: Basic tkinter
    success1 = test_tkinter()
    
    if success1:
        # Test 2: NotebookLM GUI
        success2 = test_notebooklm_gui()
    else:
        print("Skipping NotebookLM GUI test due to tkinter failure")
        success2 = False
    
    print("\n" + "=" * 40)
    print("Test Results:")
    print(f"tkinter test: {'PASS' if success1 else 'FAIL'}")
    print(f"NotebookLM GUI test: {'PASS' if success2 else 'FAIL'}")
    
    if success1 and success2:
        print("\n✓ All tests passed! GUI should work properly.")
    elif success1:
        print("\n⚠ tkinter works but NotebookLM GUI has issues.")
    else:
        print("\n✗ GUI tests failed. Check tkinter installation.")

if __name__ == "__main__":
    main()
