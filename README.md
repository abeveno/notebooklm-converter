# NotebookLM Converter 📚➡️🤖

A professional cross-platform desktop application that converts ebooks to formats optimized for Google NotebookLM. Transform your digital library into AI-ready content for enhanced research and analysis.

[![Build Status](https://github.com/abeveno/notebooklm-converter/actions/workflows/simple-build.yml/badge.svg)](https://github.com/abeveno/notebooklm-converter/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ Features

### 📖 Input Formats Support
- **EPUB** - Electronic Publication standard
- **MOBI** - Amazon Kindle format  
- **AZW/AZW3** - Amazon Kindle Advanced format
- **CBZ** - Comic Book Archive (ZIP)
- **iBooks** - Apple Books format

### 🎯 NotebookLM-Optimized Output
- **TXT** - Clean plain text perfect for AI processing
- **PDF** - Formatted documents with preserved structure
- **DOCX** - Microsoft Word format for easy editing
- **Markdown** - Structured text with metadata for enhanced analysis

### 🚀 Key Capabilities
- ✅ **Batch Processing** - Convert multiple files simultaneously
- ✅ **Cross-Platform** - Native apps for Windows, macOS, and Linux
- ✅ **User-Friendly GUI** - Intuitive interface with progress tracking
- ✅ **Content Optimization** - Text cleaning and formatting for AI readability
- ✅ **Multi-File Selection** - Drag-and-drop support for bulk operations
- ✅ **Error Handling** - Robust processing with detailed error reporting

## 🛠️ Installation

### Option 1: Download Pre-built Apps (Recommended)

#### For macOS 🍎
1. Go to [Releases](https://github.com/abeveno/notebooklm-converter/releases)
2. Download `NotebookLM-Converter-macOS.dmg`
3. Open the DMG file and drag the app to Applications folder
4. Launch from Applications or Spotlight

#### For Windows 🪟
1. Go to [Releases](https://github.com/abeveno/notebooklm-converter/releases)
2. Download `NotebookLM-Converter-Windows.msi`
3. Double-click the MSI file to install
4. Launch from Start Menu or Desktop shortcut

#### For Linux 🐧
1. Go to [Releases](https://github.com/abeveno/notebooklm-converter/releases)
2. Download `NotebookLM-Converter-Linux.AppImage`
3. Make executable: `chmod +x NotebookLM-Converter-Linux.AppImage`
4. Run: `./NotebookLM-Converter-Linux.AppImage`

### Option 2: Run from Source

```bash
# Clone the repository
git clone https://github.com/abeveno/notebooklm-converter.git
cd notebooklm-converter

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 3: Development Setup with Briefcase

```bash
# Install Briefcase
pip install briefcase

# Install project dependencies
pip install -e .

# Run in development mode
briefcase dev

# Or build native app
briefcase create
briefcase build
briefcase package
```

## 📱 Usage Guide

### Quick Start
1. **Launch the application**
2. **Select Input Files**
   - Click "Select Files" button
   - Choose one or multiple ebook files
   - Supported: EPUB, MOBI, AZW, CBZ files
3. **Choose Output Format**
   - TXT: For AI processing and analysis
   - PDF: For reading and sharing
   - DOCX: For editing and collaboration
4. **Select Output Directory**
   - Choose where to save converted files
5. **Click Convert**
   - Monitor progress in real-time
   - Files will be saved with "_converted" suffix

### Advanced Tips
- **Batch Processing**: Select multiple files for bulk conversion
- **Format Selection**: Choose the best format for your NotebookLM workflow
- **File Naming**: Converted files maintain original names with format suffix
- **Error Recovery**: Check logs if conversion fails for specific files

## 🏗️ Technical Architecture

### Project Structure
```
notebooklm-converter/
├── src/notebooklm_converter/     # Main application package
│   ├── app.py                    # Application entry point
│   ├── gui.py                    # GUI implementation
│   └── resources/                # Icons and assets
├── .github/workflows/            # CI/CD automation
├── main.py                       # Standalone script
├── pyproject.toml               # Project configuration
└── README.md                    # This file
```

### Dependencies
- **Core**: Python 3.8+, tkinter (GUI framework)
- **Ebook Processing**: EbookLib, BeautifulSoup4, lxml
- **Document Generation**: ReportLab (PDF), python-docx (Word)
- **Packaging**: Briefcase (cross-platform apps)

### Build System
- **Automated Builds**: GitHub Actions for all platforms
- **Package Management**: Modern Python packaging with pyproject.toml
- **Cross-Platform**: Native installers for Windows, macOS, Linux

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/notebooklm-converter.git
cd notebooklm-converter

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest

# Start development server
briefcase dev
```

### Code Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes
- Include tests for new features
- Update documentation as needed

### Submitting Changes
1. Create a feature branch: `git checkout -b feature/amazing-feature`
2. Make your changes and add tests
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to your fork: `git push origin feature/amazing-feature`
5. Create a Pull Request

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **RAM**: 512 MB
- **Storage**: 100 MB free space
- **Python**: 3.8+ (for source installation)

### Recommended
- **OS**: Latest versions of supported operating systems
- **RAM**: 2 GB or more
- **Storage**: 1 GB free space
- **Display**: 1024x768 or higher resolution

## 🔧 Troubleshooting

### Common Issues

**Q: Application won't start on macOS**
A: Right-click the app and select "Open" to bypass Gatekeeper restrictions.

**Q: Conversion fails with "Permission denied" error**
A: Ensure you have write permissions to the output directory.

**Q: Some EPUB files don't convert properly**
A: Try converting to TXT format first, which has better compatibility.

**Q: Windows Defender flags the application**
A: This is common with unsigned applications. Add an exception if needed.

### Getting Help
1. Check the [Issues](https://github.com/abeveno/notebooklm-converter/issues) page
2. Search existing discussions
3. Create a new issue with detailed information:
   - Operating system and version
   - Input file format and size
   - Error messages or unexpected behavior
   - Steps to reproduce the issue

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **EbookLib** - Excellent EPUB processing library
- **ReportLab** - Professional PDF generation
- **Briefcase** - Cross-platform Python app packaging
- **BeautifulSoup** - HTML/XML parsing capabilities
- **NotebookLM Team** - Inspiration for AI-optimized content formats

## 🔗 Related Projects

- [Google NotebookLM](https://notebooklm.google.com/) - AI-powered research assistant
- [Calibre](https://calibre-ebook.com/) - Comprehensive ebook management
- [Pandoc](https://pandoc.org/) - Universal document converter

---

**Made with ❤️ for the AI research community**

Transform your ebook library into NotebookLM-ready content and supercharge your research workflow!
