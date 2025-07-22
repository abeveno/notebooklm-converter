"""
NotebookLM Converter Application
Main entry point for the Briefcase-compatible application.
"""

try:
    import tkinter as tk
except ImportError:
    try:
        import Tkinter as tk  # Python 2 fallback
    except ImportError:
        print("Error: tkinter is not available. Please install Python with tkinter support.")
        exit(1)

from .gui import NotebookLMConverterApp


def main():
    """
    Main entry point for the NotebookLM Converter application.
    """
    try:
        root = tk.Tk()
        app = NotebookLMConverterApp(root)
        root.mainloop()
    except Exception as e:
        import sys
        print(f"Error starting NotebookLM Converter: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
