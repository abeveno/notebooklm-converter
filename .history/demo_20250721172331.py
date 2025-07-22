#!/usr/bin/env python3
"""
Demo script để test các chức năng chuyển đổi của EPUB All-in-One Converter
"""

import os
from main import EbookAllInOneConverterApp
import tkinter as tk

def create_demo_window():
    """
    Tạo cửa sổ demo đơn giản
    """
    demo_root = tk.Tk()
    demo_root.title("EPUB Converter Demo")
    demo_root.geometry("400x300")
    
    # Label thông tin
    info_label = tk.Label(demo_root, text="EPUB All-in-One Converter Demo", 
                         font=("Arial", 16, "bold"))
    info_label.pack(pady=20)
    
    # Hướng dẫn
    instruction = """
    Để test ứng dụng:
    
    1. Chuẩn bị file EPUB mẫu
    2. Nhấn 'Launch Converter' để mở ứng dụng chính
    3. Test chuyển đổi sang các định dạng khác nhau
    
    Các định dạng hỗ trợ:
    • PDF - Tài liệu PDF
    • TXT - Văn bản thuần túy  
    • Markdown - Định dạng Markdown
    • HTML - Trang web HTML
    • DOCX - Tài liệu Word
    • MOBI - Kindle (cần Calibre)
    """
    
    instruction_label = tk.Label(demo_root, text=instruction, justify=tk.LEFT, 
                                font=("Arial", 10))
    instruction_label.pack(pady=10, padx=20)
    
    def launch_converter():
        converter_root = tk.Tk()
        app = EbookAllInOneConverterApp(converter_root)
        converter_root.mainloop()
    
    # Button để mở converter
    launch_button = tk.Button(demo_root, text="Launch Converter", 
                             command=launch_converter, 
                             bg="#007bff", fg="white", 
                             font=("Arial", 12, "bold"),
                             padx=20, pady=10)
    launch_button.pack(pady=20)
    
    demo_root.mainloop()

if __name__ == "__main__":
    create_demo_window()
