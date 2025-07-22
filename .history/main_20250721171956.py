# Tên file: epub_all_in_one_converter.py
# Mô tả: Một ứng dụng GUI All-in-one để chuyển đổi file EPUB sang nhiều định dạng khác nhau.
# Hỗ trợ: PDF, TXT, Markdown, HTML, MOBI/AZW3, DOCX
#
# Hướng dẫn cài đặt các thư viện cần thiết:
# Mở Command Prompt (cmd) hoặc PowerShell và chạy lệnh sau:
# pip install EbookLib beautifulsoup4 lxml xhtml2pdf python-docx markdown

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from xhtml2pdf import pisa
from docx import Document
from docx.shared import Inches
import markdown
import os
import base64
import threading
import re
import subprocess
import sys

class EbookConverterApp:
    def __init__(self, root):
        """
        Khởi tạo giao diện người dùng cho ứng dụng.
        """
        self.root = root
        self.root.title("Công cụ chuyển đổi EPUB sang PDF")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.epub_path = None

        # --- Frame chính ---
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # --- Tiêu đề ---
        title_label = tk.Label(main_frame, text="Chuyển đổi EPUB sang PDF", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=(0, 20))

        # --- Nút chọn file ---
        select_button = tk.Button(main_frame, text="1. Chọn file EPUB", command=self.select_epub_file, font=("Helvetica", 12), bg="#007bff", fg="white", relief=tk.FLAT, padx=10, pady=5)
        select_button.pack(pady=10)

        # --- Nhãn hiển thị file đã chọn ---
        self.file_label = tk.Label(main_frame, text="Chưa có file nào được chọn", font=("Helvetica", 10, "italic"), bg="#f0f0f0", fg="#555")
        self.file_label.pack(pady=5)

        # --- Nút chuyển đổi ---
        self.convert_button = tk.Button(main_frame, text="2. Chuyển đổi sang PDF", command=self.start_conversion_thread, font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", relief=tk.FLAT, padx=10, pady=5, state=tk.DISABLED)
        self.convert_button.pack(pady=20)
        
        # --- Vùng hiển thị trạng thái ---
        self.status_label = tk.Label(main_frame, text="Sẵn sàng", font=("Helvetica", 10), bg="#f0f0f0", fg="#333")
        self.status_label.pack(pady=10, side=tk.BOTTOM, fill=tk.X)

    def select_epub_file(self):
        """
        Mở hộp thoại để người dùng chọn một file .epub.
        """
        self.epub_path = filedialog.askopenfilename(
            title="Chọn một file EPUB",
            filetypes=[("EPUB files", "*.epub")]
        )
        if self.epub_path:
            # Lấy tên file để hiển thị
            filename = os.path.basename(self.epub_path)
            self.file_label.config(text=f"Đã chọn: {filename}", font=("Helvetica", 10, "normal"))
            self.convert_button.config(state=tk.NORMAL) # Kích hoạt nút chuyển đổi
            self.status_label.config(text="Đã chọn file. Sẵn sàng để chuyển đổi.")
        else:
            self.file_label.config(text="Chưa có file nào được chọn", font=("Helvetica", 10, "italic"))
            self.convert_button.config(state=tk.DISABLED)

    def start_conversion_thread(self):
        """
        Bắt đầu quá trình chuyển đổi trong một luồng riêng để không làm treo giao diện.
        """
        if not self.epub_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn một file EPUB trước.")
            return

        pdf_path = filedialog.asksaveasfilename(
            title="Lưu file PDF",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )

        if not pdf_path:
            self.status_label.config(text="Hủy bỏ lưu file.")
            return
            
        # Vô hiệu hóa các nút trong khi xử lý
        self.convert_button.config(state=tk.DISABLED)
        
        self.status_label.config(text="Đang chuyển đổi, vui lòng chờ...")
        self.root.update_idletasks() # Cập nhật giao diện

        # Chạy chuyển đổi trong một luồng khác
        conversion_thread = threading.Thread(
            target=self.convert_epub_to_pdf,
            args=(self.epub_path, pdf_path)
        )
        conversion_thread.start()

    def convert_epub_to_pdf(self, epub_path, pdf_path):
        """
        Hàm chính thực hiện việc đọc EPUB, xử lý nội dung và tạo file PDF.
        """
        try:
            book = epub.read_epub(epub_path)
            
            # Lấy tất cả các mục (html, css, images) từ sách
            items = list(book.get_items())
            
            # Tạo một từ điển để lưu trữ hình ảnh dưới dạng base64
            images_base64 = {}
            for item in items:
                if item.get_type() == ebooklib.ITEM_IMAGE:
                    # Lấy nội dung và mã hóa base64
                    content = item.get_content()
                    encoded_image = base64.b64encode(content).decode('utf-8')
                    # Lấy media_type (ví dụ: 'image/jpeg')
                    media_type = item.get_media_type()
                    # Tạo chuỗi data URI
                    images_base64[item.get_name()] = f"data:{media_type};base64,{encoded_image}"

            # Lấy tất cả CSS và gộp lại
            css_content = ""
            for item in items:
                if item.get_type() == ebooklib.ITEM_STYLE:
                    css_content += item.get_content().decode('utf-8', 'ignore')

            # Bắt đầu nội dung HTML
            full_html_content = f"<html><head><style>{css_content}</style></head><body>"

            # Lấy nội dung theo thứ tự đọc (spine)
            for item_id in book.spine:
                item = book.get_item_with_id(item_id[0])
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    # Sử dụng BeautifulSoup để phân tích và xử lý HTML
                    soup = BeautifulSoup(item.get_content(), 'lxml')
                    
                    # Thay thế đường dẫn hình ảnh bằng dữ liệu base64
                    for img_tag in soup.find_all('img'):
                        src = img_tag.get('src')
                        if src:
                            # Đường dẫn có thể là tương đối, cần chuẩn hóa
                            img_path = os.path.normpath(os.path.join(os.path.dirname(item.get_name()), src))
                            # Chuyển đổi dấu \ thành / cho key trong từ điển
                            img_key = img_path.replace('\\', '/')
                            if img_key in images_base64:
                                img_tag['src'] = images_base64[img_key]

                    full_html_content += str(soup)
            
            full_html_content += "</body></html>"

            # Tạo file PDF
            with open(pdf_path, "w+b") as pdf_file:
                pisa_status = pisa.CreatePDF(full_html_content, dest=pdf_file, encoding='UTF-8')

            if pisa_status.err:
                raise Exception(f"Lỗi khi tạo PDF: {pisa_status.err}")
            
            # Cập nhật giao diện khi thành công
            self.root.after(0, self.conversion_successful, pdf_path)

        except Exception as e:
            # Cập nhật giao diện khi có lỗi
            self.root.after(0, self.conversion_failed, e)

    def conversion_successful(self, pdf_path):
        """
        Hiển thị thông báo khi chuyển đổi thành công.
        """
        self.status_label.config(text=f"Chuyển đổi thành công! Đã lưu tại: {pdf_path}")
        messagebox.showinfo("Hoàn tất", f"File PDF đã được tạo thành công!")
        self.convert_button.config(state=tk.NORMAL) # Kích hoạt lại nút

    def conversion_failed(self, error):
        """
        Hiển thị thông báo khi có lỗi xảy ra.
        """
        self.status_label.config(text=f"Lỗi: {error}")
        messagebox.showerror("Lỗi chuyển đổi", f"Đã có lỗi xảy ra:\n{error}")
        self.convert_button.config(state=tk.NORMAL) # Kích hoạt lại nút

if __name__ == "__main__":
    root = tk.Tk()
    app = EbookConverterApp(root)
    root.mainloop()
