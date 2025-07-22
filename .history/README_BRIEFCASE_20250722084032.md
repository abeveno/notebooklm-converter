# NotebookLM Converter - Briefcase Project

A cross-platform desktop application to convert ebooks to formats optimized for Google NotebookLM.

## Features

- **Multi-format support**: EPUB, MOBI, AZW/KFX, iBooks, CBR/CBZ
- **NotebookLM optimization**: Outputs PDF, TXT, and Markdown formats specially formatted for AI analysis
- **Batch processing**: Convert multiple files at once
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Clean interface**: Simple, intuitive design

## Installation

### For End Users

Download the latest release for your platform:
- **Windows**: Download `.msi` installer
- **macOS**: Download `.dmg` installer
- **Linux**: Download `.AppImage` or use package manager

### For Developers

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/notebooklm-converter.git
   cd notebooklm-converter
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Briefcase** (for building):
   ```bash
   pip install briefcase
   ```

4. **Install Calibre** (optional, for MOBI/AZW support):
   - Download from: https://calibre-ebook.com/download

## Development

### Running from Source

```bash
cd src
python -m notebooklm_converter.app
```

### Building with Briefcase

1. **Create the application**:
   ```bash
   briefcase create
   ```

2. **Build the application**:
   ```bash
   briefcase build
   ```

3. **Run the built application**:
   ```bash
   briefcase run
   ```

4. **Package for distribution**:
   ```bash
   briefcase package
   ```

### Platform-Specific Instructions

#### Windows
- Briefcase will create an MSI installer
- Requires Visual Studio Build Tools or Visual Studio

#### macOS
- Briefcase will create a DMG installer
- Requires Xcode command line tools
- May need to sign the application for distribution

#### Linux
- Briefcase will create an AppImage
- Requires system packages (automatically handled)

## Usage

1. **Launch the application**
2. **Select files**:
   - Click "Select Single File" for one ebook
   - Click "Select Multiple Files" for batch processing
3. **Choose output format**:
   - **PDF**: Best for reading and sharing
   - **TXT**: Plain text for AI processing
   - **Markdown**: Structured format with metadata
4. **Convert**: Click "Convert for NotebookLM"
5. **Find your files**: Converted files are saved in the same directory as the original files with "_NotebookLM" suffix

## Supported Formats

### Input Formats
- **EPUB**: Standard ebook format
- **MOBI/AZW/AZW3**: Amazon Kindle formats (requires Calibre)
- **KFX**: Amazon Kindle format (requires Calibre with KFX plugin)
- **iBooks/IBA**: Apple iBooks format
- **CBR/CBZ**: Comic book archives

### Output Formats
- **PDF**: Formatted document with proper styling
- **TXT**: Clean plain text optimized for AI
- **Markdown**: Structured text with metadata headers

## Requirements

### System Requirements
- **Windows**: Windows 10 or later
- **macOS**: macOS 10.14 or later
- **Linux**: Ubuntu 18.04+ or equivalent

### Optional Dependencies
- **Calibre**: For MOBI/AZW/KFX format support
- **rarfile**: For CBR archive support

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

- **Issues**: Report bugs on GitHub Issues
- **Documentation**: Check the README and code comments
- **Community**: Join discussions in GitHub Discussions

## Changelog

### Version 1.0.0
- Initial release with Briefcase support
- Multi-file batch processing
- Complete English interface
- NotebookLM optimization features
- Cross-platform compatibility
