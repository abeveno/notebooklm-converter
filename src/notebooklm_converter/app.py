"""
NotebookLM Converter Application
Main entry point for the Briefcase-compatible application.
"""

import sys
import platform

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
        # Force GUI mode for Windows builds
        if platform.system() == "Windows" and TKINTER_AVAILABLE:
            print("Starting Windows GUI mode...")
            root = tk.Tk()
            root.title("NotebookLM Converter")
            
            # Windows-specific window configuration
            root.lift()
            root.attributes('-topmost', True)
            root.after_idle(root.attributes, '-topmost', False)
            
            # Ensure window is visible
            root.state('normal')
            root.focus_force()
            
            app = NotebookLMConverterApp(root)
            root.mainloop()
            
        elif TKINTER_AVAILABLE:
            # GUI mode for other platforms
            print("Starting GUI mode...")
            root = tk.Tk()
            app = NotebookLMConverterApp(root)
            root.mainloop()
        else:
            # Console mode fallback
            print("Starting console mode...")
            console_main()
    except Exception as e:
        print(f"Error starting NotebookLM Converter: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
