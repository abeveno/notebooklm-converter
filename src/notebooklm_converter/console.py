"""
Console version of NotebookLM Converter for environments without GUI support.
"""

import os
import sys
from pathlib import Path
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


class NotebookLMConverterConsole:
    """Console version of the NotebookLM Converter."""
    
    def __init__(self):
        self.supported_formats = ['.epub', '.mobi', '.azw', '.azw3']
        self.output_formats = ['pdf', 'txt', 'markdown']
    
    def convert_file(self, input_file, output_format='pdf'):
        """Convert a single ebook file."""
        try:
            input_path = Path(input_file)
            if not input_path.exists():
                print(f"Error: File {input_file} not found")
                return False
            
            if input_path.suffix.lower() not in self.supported_formats:
                print(f"Error: Unsupported format {input_path.suffix}")
                return False
            
            # Read the ebook
            if input_path.suffix.lower() == '.epub':
                content = self._read_epub(input_path)
            else:
                print(f"Format {input_path.suffix} not yet supported in console mode")
                return False
            
            # Generate output
            output_path = input_path.with_suffix(f'.{output_format}')
            
            if output_format == 'txt':
                self._save_as_txt(content, output_path)
            elif output_format == 'pdf':
                self._save_as_pdf(content, output_path)
            elif output_format == 'markdown':
                self._save_as_markdown(content, output_path)
            
            print(f"Successfully converted {input_file} to {output_path}")
            return True
            
        except Exception as e:
            print(f"Error converting {input_file}: {e}")
            return False
    
    def _read_epub(self, epub_path):
        """Read EPUB file and extract text content."""
        book = epub.read_epub(str(epub_path))
        content = []
        
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_content(), 'html.parser')
                text = soup.get_text()
                if text.strip():
                    content.append(text.strip())
        
        return '\n\n'.join(content)
    
    def _save_as_txt(self, content, output_path):
        """Save content as plain text."""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _save_as_pdf(self, content, output_path):
        """Save content as PDF."""
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            from reportlab.lib.utils import simpleSplit
            
            c = canvas.Canvas(str(output_path), pagesize=letter)
            width, height = letter
            
            # Split content into lines that fit the page
            lines = content.split('\n')
            y_position = height - 50
            
            for line in lines:
                if y_position < 50:  # Start new page
                    c.showPage()
                    y_position = height - 50
                
                # Split long lines
                wrapped_lines = simpleSplit(line, "Helvetica", 12, width - 100)
                for wrapped_line in wrapped_lines:
                    if y_position < 50:
                        c.showPage()
                        y_position = height - 50
                    
                    c.drawString(50, y_position, wrapped_line)
                    y_position -= 15
            
            c.save()
        except Exception as e:
            print(f"Error creating PDF: {e}")
            # Fallback to text
            self._save_as_txt(content, output_path.with_suffix('.txt'))
    
    def _save_as_markdown(self, content, output_path):
        """Save content as Markdown."""
        # Simple markdown conversion
        markdown_content = f"# {output_path.stem}\n\n{content}"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)


def console_main():
    """Main function for console version."""
    print("NotebookLM Converter - Console Mode")
    print("===================================")
    
    converter = NotebookLMConverterConsole()
    
    if len(sys.argv) < 2:
        print("Usage: python -m notebooklm_converter <input_file> [output_format]")
        print("Output formats: pdf, txt, markdown (default: pdf)")
        return
    
    input_file = sys.argv[1]
    output_format = sys.argv[2] if len(sys.argv) > 2 else 'pdf'
    
    if output_format not in converter.output_formats:
        print(f"Invalid output format: {output_format}")
        print(f"Supported formats: {', '.join(converter.output_formats)}")
        return
    
    success = converter.convert_file(input_file, output_format)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    console_main()
