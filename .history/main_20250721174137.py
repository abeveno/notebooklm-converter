# Tên file: notebooklm_converter.py
# Mô tả: Một ứng dụng GUI NotebookLM Converter để chuyển đổi sách điện tử sang định dạng tối ưu cho NotebookLM.
# Input hỗ trợ: EPUB, MOBI, AZW/KFX, IBA, CBR/CBZ
# Output hỗ trợ: PDF, TXT, Markdown
#
# Hướng dẫn cài đặt các thư viện cần thiết:
# Mở Command Prompt (cmd) hoặc PowerShell và chạy lệnh sau:
# pip install EbookLib beautifulsoup4 lxml xhtml2pdf markdown pillow rarfile patoolib

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from xhtml2pdf import pisa
import markdown
import os
import base64
import threading
import re
import subprocess
import sys
import zipfile
import tempfile
from PIL import Image
import io

class NotebookLMConverterApp:
    def __init__(self, root):
        """
        Khởi tạo giao diện người dùng cho ứng dụng NotebookLM Converter.
        """
        self.root = root
        self.root.title("NotebookLM Converter")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f0f0")

        self.input_path = None
        self.output_format = tk.StringVar(value="PDF")
        self.quality_var = tk.StringVar(value="normal")

        # --- Frame chính ---
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # --- Tiêu đề ---
        title_label = tk.Label(main_frame, text="NotebookLM Converter", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(main_frame, text="Chuyển đổi sách điện tử sang định dạng tối ưu cho NotebookLM", font=("Helvetica", 10), bg="#f0f0f0", fg="#666")
        subtitle_label.pack(pady=(0, 5))
        
        format_support_label = tk.Label(main_frame, text="Input: EPUB, MOBI, AZW/KFX, IBA, CBR/CBZ • Output: PDF, TXT, Markdown", font=("Helvetica", 9), bg="#f0f0f0", fg="#888")
        format_support_label.pack(pady=(0, 20))

        # --- Frame cho việc chọn file ---
        file_frame = tk.Frame(main_frame, bg="#f0f0f0")
        file_frame.pack(fill=tk.X, pady=10)

        # --- Nút chọn file ---
        select_button = tk.Button(file_frame, text="1. Chọn file sách điện tử", command=self.select_input_file, font=("Helvetica", 12), bg="#007bff", fg="white", relief=tk.FLAT, padx=15, pady=8)
        select_button.pack(side=tk.LEFT)

        # --- Nhãn hiển thị file đã chọn ---
        self.file_label = tk.Label(file_frame, text="Chưa có file nào được chọn", font=("Helvetica", 10, "italic"), bg="#f0f0f0", fg="#555")
        self.file_label.pack(side=tk.LEFT, padx=(15, 0))

        # --- Frame cho việc chọn định dạng ---
        format_frame = tk.LabelFrame(main_frame, text="2. Chọn định dạng đầu ra cho NotebookLM", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="#333", padx=10, pady=10)
        format_frame.pack(fill=tk.X, pady=20)

        # --- Radio buttons cho các định dạng ---
        formats = [
            ("PDF", "PDF", "Portable Document Format - Tối ưu cho NotebookLM, giữ nguyên định dạng"),
            ("TXT", "TXT", "Plain Text - Văn bản thuần túy, dễ phân tích cho AI"),
            ("Markdown", "MD", "Markdown - Định dạng có cấu trúc, tối ưu cho AI processing")
        ]

        # Tạo layout cho radio buttons
        for i, (display_name, value, description) in enumerate(formats):
            frame = tk.Frame(format_frame, bg="#f0f0f0")
            frame.pack(anchor="w", padx=10, pady=8)
            
            radio = tk.Radiobutton(frame, text=display_name, variable=self.output_format, value=value, 
                                 font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="#333")
            radio.pack(anchor="w")
            
            desc_label = tk.Label(frame, text=description, font=("Helvetica", 9), bg="#f0f0f0", fg="#666")
            desc_label.pack(anchor="w", padx=(25, 0))

        # --- Advanced Options Frame ---
        advanced_frame = tk.LabelFrame(main_frame, text="Tùy chọn NotebookLM", font=("Helvetica", 10), bg="#f0f0f0", fg="#666", padx=10, pady=5)
        advanced_frame.pack(fill=tk.X, pady=10)
        
        # Quality options for NotebookLM optimization
        self.quality_var = tk.StringVar(value="notebooklm")
        quality_frame = tk.Frame(advanced_frame, bg="#f0f0f0")
        quality_frame.pack(anchor="w")
        
        tk.Label(quality_frame, text="Tối ưu hóa:", font=("Helvetica", 9), bg="#f0f0f0").pack(side=tk.LEFT)
        tk.Radiobutton(quality_frame, text="Chuẩn", variable=self.quality_var, value="standard", bg="#f0f0f0", font=("Helvetica", 8)).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(quality_frame, text="NotebookLM", variable=self.quality_var, value="notebooklm", bg="#f0f0f0", font=("Helvetica", 8)).pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(quality_frame, text="AI-Ready", variable=self.quality_var, value="ai_ready", bg="#f0f0f0", font=("Helvetica", 8)).pack(side=tk.LEFT, padx=5)

        # --- Nút chuyển đổi ---
        self.convert_button = tk.Button(main_frame, text="3. Chuyển đổi cho NotebookLM", command=self.start_conversion_thread, 
                                      font=("Helvetica", 14, "bold"), bg="#28a745", fg="white", relief=tk.FLAT, 
                                      padx=20, pady=10, state=tk.DISABLED)
        self.convert_button.pack(pady=30)
        
        # --- Progress bar ---
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=10)
        
        # --- Vùng hiển thị trạng thái ---
        self.status_label = tk.Label(main_frame, text="Sẵn sàng - Chọn file sách điện tử để bắt đầu", font=("Helvetica", 11), bg="#f0f0f0", fg="#333")
        self.status_label.pack(pady=10, side=tk.BOTTOM, fill=tk.X)

    def select_input_file(self):
        """
        Mở hộp thoại để người dùng chọn một file sách điện tử.
        """
        self.input_path = filedialog.askopenfilename(
            title="Chọn file sách điện tử",
            filetypes=[
                ("All supported", "*.epub;*.mobi;*.azw;*.azw3;*.kfx;*.ibooks;*.cbr;*.cbz"),
                ("EPUB files", "*.epub"),
                ("MOBI files", "*.mobi"),
                ("AZW files", "*.azw;*.azw3"),
                ("KFX files", "*.kfx"),
                ("iBooks files", "*.ibooks"),
                ("Comic Book Archive", "*.cbr;*.cbz"),
                ("All files", "*.*")
            ]
        )
        if self.input_path:
            # Lấy tên file để hiển thị
            filename = os.path.basename(self.input_path)
            file_ext = os.path.splitext(filename)[1].lower()
            self.file_label.config(text=f"Đã chọn: {filename} ({file_ext.upper()})", font=("Helvetica", 10, "normal"))
            self.convert_button.config(state=tk.NORMAL) # Kích hoạt nút chuyển đổi
            self.status_label.config(text="Đã chọn file. Sẵn sàng để chuyển đổi cho NotebookLM.")
        else:
            self.file_label.config(text="Chưa có file nào được chọn", font=("Helvetica", 10, "italic"))
            self.convert_button.config(state=tk.DISABLED)

    def start_conversion_thread(self):
        """
        Bắt đầu quá trình chuyển đổi trong một luồng riêng để không làm treo giao diện.
        """
        if not self.input_path:
            messagebox.showerror("Lỗi", "Vui lòng chọn một file sách điện tử trước.")
            return

        # Lấy định dạng đầu ra
        format_choice = self.output_format.get()
        
        # Định nghĩa extension tương ứng cho NotebookLM
        extensions = {
            "PDF": ".pdf",
            "TXT": ".txt", 
            "MD": ".md"
        }
        
        # Định nghĩa file types cho dialog
        file_types = {
            "PDF": [("PDF files", "*.pdf")],
            "TXT": [("Text files", "*.txt")],
            "MD": [("Markdown files", "*.md")]
        }

        output_path = filedialog.asksaveasfilename(
            title=f"Lưu file {format_choice} cho NotebookLM",
            defaultextension=extensions[format_choice],
            filetypes=file_types[format_choice]
        )

        if not output_path:
            self.status_label.config(text="Hủy bỏ lưu file.")
            return
            
        # Vô hiệu hóa các nút và bắt đầu progress bar
        self.convert_button.config(state=tk.DISABLED)
        self.progress.start()
        
        self.status_label.config(text=f"Đang chuyển đổi sang {format_choice} cho NotebookLM, vui lòng chờ...")
        self.root.update_idletasks()

        # Chạy chuyển đổi trong một luồng khác
        conversion_thread = threading.Thread(
            target=self.convert_ebook,
            args=(self.input_path, output_path, format_choice)
        )
        conversion_thread.start()

    def convert_ebook(self, input_path, output_path, output_format):
        """
        Hàm chính thực hiện việc chuyển đổi sách điện tử sang định dạng được chọn cho NotebookLM.
        """
        try:
            # Xác định loại file input
            file_ext = os.path.splitext(input_path)[1].lower()
            
            if file_ext == '.epub':
                book_content = self.extract_from_epub(input_path)
            elif file_ext in ['.mobi', '.azw', '.azw3']:
                book_content = self.extract_from_mobi(input_path)
            elif file_ext == '.kfx':
                book_content = self.extract_from_kfx(input_path)
            elif file_ext == '.ibooks':
                book_content = self.extract_from_ibooks(input_path)
            elif file_ext in ['.cbr', '.cbz']:
                book_content = self.extract_from_comic(input_path)
            else:
                raise Exception(f"Định dạng file không được hỗ trợ: {file_ext}")
            
            # Chuyển đổi sang định dạng đầu ra
            if output_format == "PDF":
                self.create_notebooklm_pdf(book_content, output_path)
            elif output_format == "TXT":
                self.create_notebooklm_txt(book_content, output_path)
            elif output_format == "MD":
                self.create_notebooklm_markdown(book_content, output_path)
            
            # Cập nhật giao diện khi thành công
            self.root.after(0, self.conversion_successful, output_path, output_format)

        except Exception as e:
            # Cập nhật giao diện khi có lỗi
            self.root.after(0, self.conversion_failed, e)

    def extract_from_epub(self, epub_path):
        """
        Trích xuất nội dung từ file EPUB.
        """
        try:
            book = epub.read_epub(epub_path)
            return self.extract_text_content_from_epub(book)
        except Exception as e:
            raise Exception(f"Lỗi đọc file EPUB: {str(e)}")

    def extract_from_mobi(self, mobi_path):
        """
        Trích xuất nội dung từ file MOBI/AZW/AZW3 bằng Calibre.
        """
        try:
            # Chuyển đổi MOBI sang EPUB tạm thời để extract
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_epub = os.path.join(temp_dir, "temp.epub")
                
                result = subprocess.run(['ebook-convert', mobi_path, temp_epub], 
                                      capture_output=True, text=True, shell=True)
                if result.returncode != 0:
                    raise Exception(f"Lỗi chuyển đổi MOBI: {result.stderr}")
                
                return self.extract_from_epub(temp_epub)
        except FileNotFoundError:
            raise Exception("Calibre chưa được cài đặt. Vui lòng cài đặt Calibre để xử lý file MOBI/AZW.")

    def extract_from_kfx(self, kfx_path):
        """
        Trích xuất nội dung từ file KFX (yêu cầu Calibre với plugin KFX).
        """
        try:
            # Tương tự MOBI, cần Calibre
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_epub = os.path.join(temp_dir, "temp.epub")
                
                result = subprocess.run(['ebook-convert', kfx_path, temp_epub], 
                                      capture_output=True, text=True, shell=True)
                if result.returncode != 0:
                    raise Exception(f"Lỗi chuyển đổi KFX: {result.stderr}")
                
                return self.extract_from_epub(temp_epub)
        except FileNotFoundError:
            raise Exception("Calibre với plugin KFX chưa được cài đặt.")

    def extract_from_ibooks(self, ibooks_path):
        """
        Trích xuất nội dung từ file iBooks (thường là EPUB với extension khác).
        """
        try:
            # iBooks thường là EPUB với extension khác
            return self.extract_from_epub(ibooks_path)
        except Exception as e:
            raise Exception(f"Lỗi đọc file iBooks: {str(e)}")

    def extract_from_comic(self, comic_path):
        """
        Trích xuất nội dung từ comic book archive (CBR/CBZ).
        """
        try:
            extracted_text = f"# Comic Book: {os.path.basename(comic_path)}\n\n"
            
            if comic_path.lower().endswith('.cbz'):
                # CBZ là file ZIP
                with zipfile.ZipFile(comic_path, 'r') as zip_ref:
                    file_list = sorted([f for f in zip_ref.namelist() if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))])
                    extracted_text += f"Tổng số trang: {len(file_list)}\n\n"
                    for i, filename in enumerate(file_list, 1):
                        extracted_text += f"## Trang {i}: {filename}\n\n"
            elif comic_path.lower().endswith('.cbr'):
                # CBR là file RAR - cần thư viện xử lý RAR
                extracted_text += "Đây là file comic book RAR. Cần công cụ đặc biệt để trích xuất.\n"
            
            return extracted_text
        except Exception as e:
            raise Exception(f"Lỗi đọc comic book: {str(e)}")

    def extract_text_content_from_epub(self, book):
        """
        Trích xuất nội dung văn bản từ EPUB book object.
        """
        text_content = ""
        
        # Thêm metadata
        title = book.get_metadata('DC', 'title')
        creator = book.get_metadata('DC', 'creator')
        
        if title:
            text_content += f"# {title[0][0]}\n\n"
        if creator:
            text_content += f"**Tác giả:** {creator[0][0]}\n\n"
        
        text_content += "---\n\n"
        
        for item_id in book.spine:
            item = book.get_item_with_id(item_id[0])
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_content(), 'lxml')
                # Loại bỏ các thẻ script và style
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Xử lý đặc biệt cho NotebookLM
                text = soup.get_text()
                # Làm sạch text cho NotebookLM
                text = re.sub(r'\n\s*\n', '\n\n', text)  # Loại bỏ dòng trống thừa
                text = re.sub(r' +', ' ', text)  # Loại bỏ space thừa
                text_content += text + "\n\n"
        
        return text_content

    def create_notebooklm_pdf(self, content, output_path):
        """
        Tạo PDF tối ưu cho NotebookLM.
        """
        try:
            # Tạo HTML với CSS tối ưu cho NotebookLM
            html_content = f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <style>
                    body {{
                        font-family: 'Times New Roman', serif;
                        font-size: 12pt;
                        line-height: 1.6;
                        margin: 2cm;
                        color: #333;
                    }}
                    h1, h2, h3, h4, h5, h6 {{
                        color: #2c3e50;
                        margin-top: 1.5em;
                        margin-bottom: 0.5em;
                    }}
                    h1 {{ font-size: 24pt; border-bottom: 2px solid #3498db; }}
                    h2 {{ font-size: 18pt; }}
                    h3 {{ font-size: 14pt; }}
                    p {{ margin-bottom: 1em; text-align: justify; }}
                    .chapter {{ page-break-before: always; }}
                </style>
            </head>
            <body>
                <div class="content">
                    {self.format_content_for_html(content)}
                </div>
            </body>
            </html>
            """
            
            with open(output_path, "w+b") as pdf_file:
                pisa_status = pisa.CreatePDF(html_content, dest=pdf_file, encoding='UTF-8')

            if pisa_status.err:
                raise Exception(f"Lỗi khi tạo PDF: {pisa_status.err}")
                
        except Exception as e:
            raise Exception(f"Lỗi tạo PDF cho NotebookLM: {str(e)}")

    def create_notebooklm_txt(self, content, output_path):
        """
        Tạo TXT tối ưu cho NotebookLM.
        """
        try:
            # Làm sạch và format text cho NotebookLM
            optimized_content = self.optimize_text_for_notebooklm(content)
            
            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(optimized_content)
                
        except Exception as e:
            raise Exception(f"Lỗi tạo TXT cho NotebookLM: {str(e)}")

    def create_notebooklm_markdown(self, content, output_path):
        """
        Tạo Markdown tối ưu cho NotebookLM.
        """
        try:
            # Convert content to structured Markdown
            markdown_content = self.format_content_for_markdown(content)
            
            with open(output_path, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_content)
                
        except Exception as e:
            raise Exception(f"Lỗi tạo Markdown cho NotebookLM: {str(e)}")

    def optimize_text_for_notebooklm(self, content):
        """
        Tối ưu hóa text cho NotebookLM.
        """
        # Làm sạch content
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line:  # Bỏ qua dòng trống
                # Loại bỏ ký tự đặc biệt không cần thiết
                line = re.sub(r'[^\w\s\.\,\!\?\:\;\-\(\)\[\]\{\}\"\'\/]', '', line)
                cleaned_lines.append(line)
        
        # Ghép lại với cấu trúc phù hợp cho AI
        optimized_content = '\n\n'.join(cleaned_lines)
        
        # Thêm header cho NotebookLM
        quality_mode = self.quality_var.get()
        header = f"""DOCUMENT OPTIMIZED FOR NOTEBOOKLM
Quality Mode: {quality_mode.upper()}
Generated: {self.get_current_timestamp()}
Content Length: {len(optimized_content)} characters

---

"""
        
        return header + optimized_content

    def format_content_for_html(self, content):
        """
        Format content cho HTML output.
        """
        # Convert basic markdown-like syntax to HTML
        html_content = content.replace('\n\n', '</p><p>')
        html_content = f'<p>{html_content}</p>'
        
        # Convert headers
        html_content = re.sub(r'<p># ([^<]+)</p>', r'<h1>\1</h1>', html_content)
        html_content = re.sub(r'<p>## ([^<]+)</p>', r'<h2>\1</h2>', html_content)
        html_content = re.sub(r'<p>### ([^<]+)</p>', r'<h3>\1</h3>', html_content)
        
        # Convert bold/italic
        html_content = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html_content)
        html_content = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html_content)
        
        return html_content

    def format_content_for_markdown(self, content):
        """
        Format content cho Markdown output tối ưu cho NotebookLM.
        """
        # Thêm metadata cho NotebookLM
        quality_mode = self.quality_var.get()
        
        markdown_header = f"""---
title: "Document for NotebookLM"
format: "Markdown"
optimization: "{quality_mode}"
generated: "{self.get_current_timestamp()}"
---

# Document for NotebookLM Analysis

"""
        
        # Cải thiện cấu trúc Markdown
        lines = content.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Detect and format headers
                if line.startswith('#'):
                    formatted_lines.append(line)
                elif len(line) > 50 and not line.endswith('.'):
                    # Có thể là tiêu đề
                    formatted_lines.append(f"## {line}")
                else:
                    formatted_lines.append(line)
                    
        return markdown_header + '\n\n'.join(formatted_lines)

    def get_current_timestamp(self):
        """
        Lấy timestamp hiện tại.
        """
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def conversion_successful(self, output_path, output_format):
        """
        Hiển thị thông báo khi chuyển đổi thành công.
        """
        self.progress.stop()
        self.status_label.config(text=f"Chuyển đổi thành công! Đã lưu tại: {output_path}")
        messagebox.showinfo("Hoàn tất", f"File {output_format} đã được tạo thành công cho NotebookLM!\n\nĐường dẫn: {output_path}")
        self.convert_button.config(state=tk.NORMAL)

    def conversion_failed(self, error):
        """
        Hiển thị thông báo khi có lỗi xảy ra.
        """
        self.progress.stop()
        self.status_label.config(text=f"Lỗi: {error}")
        messagebox.showerror("Lỗi chuyển đổi", f"Đã có lỗi xảy ra:\n{error}")
        self.convert_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookLMConverterApp(root)
    root.mainloop()
