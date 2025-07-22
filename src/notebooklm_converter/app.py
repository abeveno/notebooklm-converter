"""
NotebookLM Converter Application
Main entry point for the Briefcase-compatible application.
"""

import sys

# Try to import tkinter for GUI mode
TKINTER_AVAILABLE = False
try:
    import tkinter as tk
    TKINTER_AVAILABLE = True
except ImportError:
    try:
        import Tkinter as tk  # Python 2 fallback
        TKINTER_AVAILABLE = True
    except ImportError:
        print("Warning: tkinter not available, running in console mode")
        TKINTER_AVAILABLE = False

if TKINTER_AVAILABLE:
    from .gui import NotebookLMConverterApp
else:
    from .console import console_main


def main():
    """
    Main entry point for the NotebookLM Converter application.
    Falls back to console mode if GUI is not available.
    """
    try:
        if TKINTER_AVAILABLE:
            # GUI mode
            root = tk.Tk()
            app = NotebookLMConverterApp(root)
            root.mainloop()
        else:
            # Console mode
            print("Starting NotebookLM Converter in console mode...")
            console_main()
    except Exception as e:
        print(f"Error starting NotebookLM Converter: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
