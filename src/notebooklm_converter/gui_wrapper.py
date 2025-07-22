"""
Windows GUI wrapper to ensure tkinter GUI is displayed.
"""

import sys
import os

def force_gui_mode():
    """Force GUI mode for Windows applications."""
    try:
        # Force import tkinter to test availability
        import tkinter as tk
        
        # Set environment variables to ensure GUI mode
        os.environ['DISPLAY'] = ':0'
        
        # Import and run GUI application
        from notebooklm_converter.gui import NotebookLMConverterApp
        
        print("Starting NotebookLM Converter GUI...")
        
        root = tk.Tk()
        root.title("NotebookLM Converter")
        
        # Ensure window is visible and brought to front
        root.lift()
        root.attributes('-topmost', True)
        root.after_idle(root.attributes, '-topmost', False)
        
        app = NotebookLMConverterApp(root)
        root.mainloop()
        
    except ImportError as e:
        print(f"GUI mode not available: {e}")
        print("Falling back to console mode...")
        from notebooklm_converter.console import console_main
        console_main()
    except Exception as e:
        print(f"Error starting GUI: {e}")
        sys.exit(1)


if __name__ == "__main__":
    force_gui_mode()
