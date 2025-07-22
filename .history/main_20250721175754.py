# File: notebooklm_converter.py
# Description: A GUI NotebookLM Converter application to convert ebooks to formats optimized for NotebookLM.
# Input support: EPUB, MOBI, AZW/KFX, IBA, CBR/CBZ
# Output support: PDF, TXT, Markdown
#
# Installation guide for required libraries:
# Open Command Prompt (cmd) or PowerShell and run:
# pip install EbookLib beautifulsoup4 lxml xhtml2pdf markdown pillow rarfile

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
        Initialize the NotebookLM Converter application.
        """
        self.root = root
        self.root.title("NotebookLM Converter")
        self.root.geometry("650x450")
        self.root.configure(bg="#f0f0f0")

        self.input_paths = []  # Changed to support multiple files
        self.output_format = tk.StringVar(value="PDF")

        # --- Main Frame ---
        main_frame = tk.Frame(self.root, padx=20, pady=20, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # --- Title ---
        title_label = tk.Label(main_frame, text="NotebookLM Converter", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(main_frame, text="Convert ebooks to formats optimized for NotebookLM", font=("Helvetica", 10), bg="#f0f0f0", fg="#666")
        subtitle_label.pack(pady=(0, 5))
        
        format_support_label = tk.Label(main_frame, text="Input: EPUB, MOBI, AZW/KFX, iBooks, CBR/CBZ • Output: PDF, TXT, Markdown", font=("Helvetica", 9), bg="#f0f0f0", fg="#888")
        format_support_label.pack(pady=(0, 20))

        # --- File Selection Frame ---
        file_frame = tk.Frame(main_frame, bg="#f0f0f0")
        file_frame.pack(fill=tk.X, pady=10)

        # --- File Selection Buttons ---
        button_frame = tk.Frame(file_frame, bg="#f0f0f0")
        button_frame.pack(side=tk.LEFT)
        
        select_single_button = tk.Button(button_frame, text="1. Select Single File", command=self.select_single_file, font=("Helvetica", 11), bg="#007bff", fg="white", relief=tk.FLAT, padx=12, pady=6)
        select_single_button.pack(side=tk.TOP, pady=(0, 5))
        
        select_multiple_button = tk.Button(button_frame, text="1. Select Multiple Files", command=self.select_multiple_files, font=("Helvetica", 11), bg="#17a2b8", fg="white", relief=tk.FLAT, padx=12, pady=6)
        select_multiple_button.pack(side=tk.TOP)

        # --- Selected Files Display ---
        self.file_label = tk.Label(file_frame, text="No files selected", font=("Helvetica", 10, "italic"), bg="#f0f0f0", fg="#555")
        self.file_label.pack(side=tk.LEFT, padx=(15, 0))

        # --- Output Format Frame ---
        format_frame = tk.LabelFrame(main_frame, text="2. Select Output Format for NotebookLM", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="#333", padx=10, pady=10)
        format_frame.pack(fill=tk.X, pady=20)

        # --- Radio buttons for formats ---
        formats = [
            ("PDF", "PDF", "Portable Document Format - Optimized for NotebookLM with proper formatting"),
            ("TXT", "TXT", "Plain Text - Clean text optimized for AI processing"),
            ("Markdown", "MD", "Markdown - Structured format with metadata for AI analysis")
        ]

        # Create layout for radio buttons
        for i, (display_name, value, description) in enumerate(formats):
            frame = tk.Frame(format_frame, bg="#f0f0f0")
            frame.pack(anchor="w", padx=10, pady=8)
            
            radio = tk.Radiobutton(frame, text=display_name, variable=self.output_format, value=value, 
                                 font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="#333")
            radio.pack(anchor="w")
            
            desc_label = tk.Label(frame, text=description, font=("Helvetica", 9), bg="#f0f0f0", fg="#666")
            desc_label.pack(anchor="w", padx=(25, 0))

        # --- Convert Button ---
        self.convert_button = tk.Button(main_frame, text="3. Convert for NotebookLM", command=self.start_conversion_thread, 
                                      font=("Helvetica", 14, "bold"), bg="#28a745", fg="white", relief=tk.FLAT, 
                                      padx=20, pady=10, state=tk.DISABLED)
        self.convert_button.pack(pady=30)
        
        # --- Progress bar ---
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=10)
        
        # --- Status Display ---
        self.status_label = tk.Label(main_frame, text="Ready - Select ebook files to begin", font=("Helvetica", 11), bg="#f0f0f0", fg="#333")
        self.status_label.pack(pady=10, side=tk.BOTTOM, fill=tk.X)

    def select_single_file(self):
        """
        Select a single ebook file for conversion.
        """
        file_types = [
            ('All supported formats', '*.epub;*.mobi;*.azw;*.azw3;*.kfx;*.ibooks;*.iba;*.cbr;*.cbz'),
            ('EPUB files', '*.epub'),
            ('Kindle formats', '*.mobi;*.azw;*.azw3;*.kfx'),
            ('iBooks format', '*.ibooks;*.iba'),
            ('Comic book archives', '*.cbr;*.cbz'),
            ('All files', '*.*')
        ]
        
        file_path = filedialog.askopenfilename(
            title="Select an ebook file",
            filetypes=file_types,
            initialdir=os.path.expanduser("~/Documents")
        )
        
        if file_path:
            self.input_paths = [file_path]
            filename = os.path.basename(file_path)
            self.file_label.config(text=f"Selected: {filename}")
            self.convert_button.config(state=tk.NORMAL)
            self.status_label.config(text=f"Ready to convert: {filename}")

    def select_multiple_files(self):
        """
        Select multiple ebook files for batch conversion.
        """
        file_types = [
            ('All supported formats', '*.epub;*.mobi;*.azw;*.azw3;*.kfx;*.ibooks;*.iba;*.cbr;*.cbz'),
            ('EPUB files', '*.epub'),
            ('Kindle formats', '*.mobi;*.azw;*.azw3;*.kfx'),
            ('iBooks format', '*.ibooks;*.iba'),
            ('Comic book archives', '*.cbr;*.cbz'),
            ('All files', '*.*')
        ]
        
        file_paths = filedialog.askopenfilenames(
            title="Select ebook files",
            filetypes=file_types,
            initialdir=os.path.expanduser("~/Documents")
        )
        
        if file_paths:
            self.input_paths = list(file_paths)
            num_files = len(file_paths)
            
            if num_files == 1:
                filename = os.path.basename(file_paths[0])
                self.file_label.config(text=f"Selected: {filename}")
                self.status_label.config(text=f"Ready to convert: {filename}")
            else:
                self.file_label.config(text=f"Selected {num_files} files")
                self.status_label.config(text=f"Ready to convert {num_files} files")
            
            self.convert_button.config(state=tk.NORMAL)
            self.convert_button.config(state=tk.DISABLED)

    def start_conversion_thread(self):
        """
        Start the conversion process in a separate thread to prevent UI freezing.
        """
        if not self.input_paths:
            messagebox.showerror("Error", "Please select at least one ebook file first.")
            return
        
        # Disable the convert button during conversion
        self.convert_button.config(state=tk.DISABLED)
        self.progress.start()
        self.status_label.config(text="Converting files for NotebookLM...")
        
        # Start conversion in a separate thread
        conversion_thread = threading.Thread(target=self.convert_files)
        conversion_thread.daemon = True
        conversion_thread.start()

    def convert_files(self):
        """
        Convert all selected files to the chosen format optimized for NotebookLM.
        """
        output_format = self.output_format.get()
        successful_conversions = 0
        total_files = len(self.input_paths)
        errors = []
        
        for i, input_path in enumerate(self.input_paths, 1):
            try:
                # Update status for current file
                filename = os.path.basename(input_path)
                self.root.after(0, lambda f=filename, curr=i, total=total_files: 
                               self.status_label.config(text=f"Converting {curr}/{total}: {f}"))
                
                # Determine output file path
                base_name = os.path.splitext(os.path.basename(input_path))[0]
                directory = os.path.dirname(input_path)
                
                if output_format == "PDF":
                    output_path = os.path.join(directory, f"{base_name}_NotebookLM.pdf")
                elif output_format == "TXT":
                    output_path = os.path.join(directory, f"{base_name}_NotebookLM.txt")
                elif output_format == "MD":
                    output_path = os.path.join(directory, f"{base_name}_NotebookLM.md")
                
                # Convert the file
                if self.convert_ebook(input_path, output_path, output_format):
                    successful_conversions += 1
                else:
                    errors.append(f"Failed to convert: {filename}")
                    
            except Exception as e:
                error_msg = f"Error converting {os.path.basename(input_path)}: {str(e)}"
                errors.append(error_msg)
        
        # Stop progress bar and update UI
        self.root.after(0, self.progress.stop)
        self.root.after(0, lambda: self.convert_button.config(state=tk.NORMAL))
        
        # Show completion message
        if successful_conversions == total_files:
            if total_files == 1:
                message = f"Successfully converted 1 file for NotebookLM!"
            else:
                message = f"Successfully converted all {total_files} files for NotebookLM!"
            self.root.after(0, lambda: messagebox.showinfo("Conversion Complete", message))
            self.root.after(0, lambda: self.status_label.config(text="Conversion completed successfully!"))
        elif successful_conversions > 0:
            message = f"Converted {successful_conversions} out of {total_files} files.\n\nErrors:\n" + "\n".join(errors)
            self.root.after(0, lambda: messagebox.showwarning("Partial Success", message))
            self.root.after(0, lambda: self.status_label.config(text=f"Partial success: {successful_conversions}/{total_files} files converted"))
        else:
            message = f"Failed to convert any files.\n\nErrors:\n" + "\n".join(errors)
            self.root.after(0, lambda: messagebox.showerror("Conversion Failed", message))
            self.root.after(0, lambda: self.status_label.config(text="Conversion failed"))

    def convert_ebook(self, input_path, output_path, output_format):
        """
        Convert a single ebook file to the specified format optimized for NotebookLM.
        """
        try:
            # Determine input file type
            file_ext = os.path.splitext(input_path)[1].lower()
            
            if file_ext == '.epub':
                book_content = self.extract_from_epub(input_path)
            elif file_ext in ['.mobi', '.azw', '.azw3']:
                book_content = self.extract_from_mobi(input_path)
            elif file_ext == '.kfx':
                book_content = self.extract_from_kfx(input_path)
            elif file_ext in ['.ibooks', '.iba']:
                book_content = self.extract_from_ibooks(input_path)
            elif file_ext in ['.cbr', '.cbz']:
                book_content = self.extract_from_comic(input_path)
            else:
                raise Exception(f"Unsupported file format: {file_ext}")
            
            # Convert to output format
            if output_format == "PDF":
                self.create_notebooklm_pdf(book_content, output_path)
            elif output_format == "TXT":
                self.create_notebooklm_txt(book_content, output_path)
            elif output_format == "MD":
                self.create_notebooklm_markdown(book_content, output_path)
            
            return True

        except Exception as e:
            print(f"Error converting {input_path}: {str(e)}")
            return False

    def extract_from_epub(self, epub_path):
        """
        Extract content from EPUB file.
        """
        try:
            book = epub.read_epub(epub_path)
            return self.extract_text_content_from_epub(book)
        except Exception as e:
            raise Exception(f"Error reading EPUB file: {str(e)}")

    def extract_from_mobi(self, mobi_path):
        """
        Extract content from MOBI/AZW/AZW3 file using Calibre.
        """
        try:
            # Convert MOBI to temporary EPUB for extraction
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_epub = os.path.join(temp_dir, "temp.epub")
                
                result = subprocess.run(['ebook-convert', mobi_path, temp_epub], 
                                      capture_output=True, text=True, shell=True)
                if result.returncode != 0:
                    raise Exception(f"MOBI conversion error: {result.stderr}")
                
                return self.extract_from_epub(temp_epub)
        except FileNotFoundError:
            raise Exception("Calibre is not installed. Please install Calibre to process MOBI/AZW files.")

    def extract_from_kfx(self, kfx_path):
        """
        Extract content from KFX file (requires Calibre with KFX plugin).
        """
        try:
            # Similar to MOBI, requires Calibre
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_epub = os.path.join(temp_dir, "temp.epub")
                
                result = subprocess.run(['ebook-convert', kfx_path, temp_epub], 
                                      capture_output=True, text=True, shell=True)
                if result.returncode != 0:
                    raise Exception(f"KFX conversion error: {result.stderr}")
                
                return self.extract_from_epub(temp_epub)
        except FileNotFoundError:
            raise Exception("Calibre with KFX plugin is not installed.")

    def extract_from_ibooks(self, ibooks_path):
        """
        Extract content from iBooks file.
        """
        try:
            # iBooks files are essentially EPUB files
            return self.extract_from_epub(ibooks_path)
        except Exception as e:
            raise Exception(f"Error reading iBooks file: {str(e)}")

    def extract_from_comic(self, comic_path):
        """
        Extract content from comic book archive (CBR/CBZ).
        """
        try:
            import zipfile
            from PIL import Image
            import io
            
            file_ext = os.path.splitext(comic_path)[1].lower()
            image_files = []
            
            if file_ext == '.cbz':
                with zipfile.ZipFile(comic_path, 'r') as zip_file:
                    for file_info in zip_file.infolist():
                        if file_info.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                            image_data = zip_file.read(file_info.filename)
                            image_files.append((file_info.filename, image_data))
            
            elif file_ext == '.cbr':
                try:
                    import rarfile
                    with rarfile.RarFile(comic_path, 'r') as rar_file:
                        for file_info in rar_file.infolist():
                            if file_info.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                                image_data = rar_file.read(file_info.filename)
                                image_files.append((file_info.filename, image_data))
                except ImportError:
                    raise Exception("rarfile library is not installed. Please install it with: pip install rarfile")
            
            # Convert images to text representation for NotebookLM
            content = {
                'title': os.path.splitext(os.path.basename(comic_path))[0],
                'author': 'Unknown',
                'chapters': []
            }
            
            # Sort by filename
            image_files.sort(key=lambda x: x[0])
            
            for i, (filename, image_data) in enumerate(image_files, 1):
                content['chapters'].append({
                    'title': f'Page {i}',
                    'content': f'[Image: {filename}]\n\nThis is page {i} of the comic book. The original content is visual and cannot be converted to text format suitable for NotebookLM analysis.'
                })
            
            return content
            
        except Exception as e:
            raise Exception(f"Error reading comic file: {str(e)}")

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
        Extract text content from EPUB book object optimized for NotebookLM.
        """
        text_content = ""
        
        # Add metadata headers for NotebookLM
        title = book.get_metadata('DC', 'title')
        creator = book.get_metadata('DC', 'creator')
        
        if title:
            text_content += f"# {title[0][0]}\n\n"
        if creator:
            text_content += f"**Author:** {creator[0][0]}\n\n"
        
        text_content += "---\n\n"
        
        for item_id in book.spine:
            item = book.get_item_with_id(item_id[0])
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_content(), 'lxml')
                # Remove script and style tags
                for script in soup(["script", "style"]):
                    script.decompose()
                
                # Special processing for NotebookLM optimization
                text = soup.get_text()
                # Clean text for NotebookLM
                text = re.sub(r'\n\s*\n', '\n\n', text)  # Remove excessive blank lines
                text = re.sub(r' +', ' ', text)  # Remove excessive spaces
                text_content += text + "\n\n"
        
        return text_content

    def create_notebooklm_pdf(self, content, output_path):
        """
        Create PDF optimized for NotebookLM.
        """
        try:
            # Create HTML with CSS optimized for NotebookLM
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
                raise Exception(f"Error creating PDF: {pisa_status.err}")
                
        except Exception as e:
            raise Exception(f"Error creating PDF for NotebookLM: {str(e)}")

    def create_notebooklm_txt(self, content, output_path):
        """
        Create TXT optimized for NotebookLM.
        """
        try:
            # Clean and format text for NotebookLM
            optimized_content = self.optimize_text_for_notebooklm(content)
            
            with open(output_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(optimized_content)
                
        except Exception as e:
            raise Exception(f"Error creating TXT for NotebookLM: {str(e)}")

    def create_notebooklm_markdown(self, content, output_path):
        """
        Create Markdown optimized for NotebookLM.
        """
        try:
            # Convert content to structured Markdown
            markdown_content = self.format_content_for_markdown(content)
            
            with open(output_path, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_content)
                
        except Exception as e:
            raise Exception(f"Error creating Markdown for NotebookLM: {str(e)}")

    def optimize_text_for_notebooklm(self, content):
        """
        Optimize text for NotebookLM analysis.
        """
        # Clean content
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line:  # Skip empty lines
                # Remove unnecessary special characters
                line = re.sub(r'[^\w\s\.\,\!\?\:\;\-\(\)\[\]\{\}\"\'\/]', '', line)
                cleaned_lines.append(line)
        
        # Reassemble with structure suitable for AI
        optimized_content = '\n\n'.join(cleaned_lines)
        
        # Add header for NotebookLM
        header = f"""DOCUMENT OPTIMIZED FOR NOTEBOOKLM
Generated: {self.get_current_timestamp()}
Content Length: {len(optimized_content)} characters

---

"""
        
        return header + optimized_content

    def format_content_for_html(self, content):
        """
        Format content for HTML output.
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
        Format content for Markdown output optimized for NotebookLM.
        """
        # Add metadata for NotebookLM
        markdown_header = f"""---
title: "Document for NotebookLM"
format: "Markdown"
generated: "{self.get_current_timestamp()}"
---

# Document for NotebookLM Analysis

"""
        
        # Improve Markdown structure
        lines = content.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if line:
                # Detect and format headers
                if line.startswith('#'):
                    formatted_lines.append(line)
                elif len(line) > 50 and not line.endswith('.'):
                    # Might be a title
                    formatted_lines.append(f"## {line}")
                else:
                    formatted_lines.append(line)
                    
        return markdown_header + '\n\n'.join(formatted_lines)

    def get_current_timestamp(self):
        """
        Get current timestamp.
        """
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotebookLMConverterApp(root)
    root.mainloop()
