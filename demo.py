#!/usr/bin/env python3
"""
Demo script để test các chức năng chuyển đổi của NotebookLM Converter
"""

import os
from main import NotebookLMConverterApp
import tkinter as tk

def create_demo_window():
    """
    Tạo cửa sổ demo đơn giản
    """
    demo_root = tk.Tk()
    demo_root.title("NotebookLM Converter Demo")
    demo_root.geometry("500x400")
    demo_root.configure(bg="#f8f9fa")
    
    # Label thông tin
    info_label = tk.Label(demo_root, text="NotebookLM Converter Demo", 
                         font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#2c3e50")
    info_label.pack(pady=20)
    
    # Hướng dẫn
    instruction = """
    🚀 NotebookLM Converter - Tối ưu cho AI Analysis
    
    📚 INPUT FORMATS SUPPORTED:
    • EPUB - Electronic Publication
    • MOBI - Amazon Kindle Format  
    • AZW/AZW3 - Amazon Advanced Format
    • KFX - Kindle Format X (cần Calibre)
    • iBooks - Apple iBooks
    • CBR/CBZ - Comic Book Archive
    
    📄 OUTPUT FOR NOTEBOOKLM:
    • PDF - Typography tối ưu cho AI
    • TXT - Cleaned text cho AI processing
    • Markdown - Structured format với metadata
    
    ⚙️ OPTIMIZATION MODES:
    • Chuẩn - Standard conversion
    • NotebookLM - Optimized for NotebookLM
    • AI-Ready - Best for AI systems
    
    🎯 WORKFLOW:
    1. Chọn file sách điện tử
    2. Chọn format output (PDF/TXT/MD)
    3. Chọn optimization mode
    4. Convert và upload vào NotebookLM!
    """
    
    instruction_label = tk.Label(demo_root, text=instruction, justify=tk.LEFT, 
                                font=("Arial", 9), bg="#f8f9fa", fg="#34495e")
    instruction_label.pack(pady=10, padx=20)
    
    def launch_converter():
        converter_root = tk.Tk()
        app = NotebookLMConverterApp(converter_root)
        converter_root.mainloop()
    
    # Button để mở converter
    launch_button = tk.Button(demo_root, text="🚀 Launch NotebookLM Converter", 
                             command=launch_converter, 
                             bg="#3498db", fg="white", 
                             font=("Arial", 12, "bold"),
                             padx=20, pady=10, relief=tk.FLAT)
    launch_button.pack(pady=20)
    
    # Footer info
    footer_label = tk.Label(demo_root, text="Convert any ebook to NotebookLM-ready format!", 
                           font=("Arial", 10, "italic"), bg="#f8f9fa", fg="#7f8c8d")
    footer_label.pack(side=tk.BOTTOM, pady=10)
    
    demo_root.mainloop()

if __name__ == "__main__":
    create_demo_window()
