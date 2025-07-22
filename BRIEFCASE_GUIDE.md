# Briefcase Build Guide for NotebookLM Converter

This guide explains how to use Briefcase to build cross-platform distributables for the NotebookLM Converter application.

## Prerequisites

1. **Python 3.8+** installed
2. **Briefcase** installed: `pip install briefcase`
3. **Platform-specific tools**:
   - **Windows**: Visual Studio Build Tools
   - **macOS**: Xcode command line tools
   - **Linux**: System packages (handled automatically)

## Quick Start

1. **Setup development environment**:
   ```bash
   python setup_dev.py
   ```

2. **Create the application structure**:
   ```bash
   briefcase create
   ```

3. **Build the application**:
   ```bash
   briefcase build
   ```

4. **Run the built application**:
   ```bash
   briefcase run
   ```

5. **Package for distribution**:
   ```bash
   briefcase package
   ```

## Detailed Commands

### Create Application Structure
```bash
briefcase create
```
This creates the platform-specific app structure in the `build/` directory.

### Build Application
```bash
briefcase build
```
Compiles the application for your current platform.

### Run Application
```bash
briefcase run
```
Runs the built application for testing.

### Package for Distribution
```bash
briefcase package
```
Creates distributable installers:
- **Windows**: `.msi` installer
- **macOS**: `.dmg` installer
- **Linux**: `.AppImage` or system packages

### Update Application
```bash
briefcase update
```
Updates the application with changes from source code.

## Platform-Specific Notes

### Windows
- **Output**: `NotebookLM Converter.msi` installer
- **Requirements**: Visual Studio Build Tools
- **Installation**: Double-click MSI to install
- **Location**: Installs to Program Files

### macOS
- **Output**: `NotebookLM Converter.dmg` installer
- **Requirements**: Xcode command line tools
- **Installation**: Mount DMG and drag to Applications
- **Signing**: May need code signing for distribution

### Linux
- **Output**: `NotebookLM Converter.AppImage`
- **Requirements**: System packages (auto-installed)
- **Installation**: Make executable and run
- **Compatibility**: Works on most Linux distributions

## Troubleshooting

### Common Issues

1. **Import errors during build**:
   ```bash
   # Make sure all dependencies are installed
   pip install -r requirements.txt
   ```

2. **Missing platform tools**:
   - Windows: Install Visual Studio Build Tools
   - macOS: Run `xcode-select --install`
   - Linux: Briefcase handles dependencies

3. **Permission errors**:
   ```bash
   # On Linux/macOS, make sure you have write permissions
   chmod +x briefcase
   ```

4. **Icon issues**:
   ```bash
   # Create icon files if missing
   cd src/notebooklm_converter/resources
   python create_icon.py
   ```

### Build from Scratch
If you encounter issues, try rebuilding from scratch:
```bash
# Remove build directory
rm -rf build/

# Recreate application
briefcase create
briefcase build
briefcase package
```

## Configuration Files

The main configuration is in `pyproject.toml`:

### Key Sections:
- **[project]**: Basic project metadata
- **[tool.briefcase]**: Global Briefcase settings
- **[tool.briefcase.app.notebooklm-converter]**: App-specific settings
- **[tool.briefcase.app.notebooklm-converter.windows]**: Windows-specific settings
- **[tool.briefcase.app.notebooklm-converter.macOS]**: macOS-specific settings
- **[tool.briefcase.app.notebooklm-converter.linux]**: Linux-specific settings

## Customization

### Changing App Information
Edit `pyproject.toml`:
```toml
[tool.briefcase.app.notebooklm-converter]
formal_name = "Your App Name"
description = "Your app description"
author = "Your Name"
author_email = "your.email@example.com"
```

### Adding Dependencies
Add to the `requires` list in `pyproject.toml`:
```toml
requires = [
    "your-new-dependency>=1.0.0",
]
```

### Custom Icons
Replace icon files in `src/notebooklm_converter/resources/`:
- `icon.ico` (Windows)
- `icon.icns` (macOS)
- `icon.png` (Linux)

## Distribution

### For Testing
- Share the built application directly from `build/` directory
- Use `briefcase run` to test locally

### For Release
1. **Package the application**:
   ```bash
   briefcase package
   ```

2. **Find distributables in**:
   - Windows: `dist/NotebookLM Converter-1.0.0.msi`
   - macOS: `dist/NotebookLM Converter-1.0.0.dmg`
   - Linux: `dist/NotebookLM Converter-1.0.0.AppImage`

3. **Upload to releases** (GitHub, website, etc.)

### Continuous Integration
For automated builds, you can use GitHub Actions or similar CI/CD systems:

```yaml
# Example GitHub Actions workflow
name: Build
on: [push, pull_request]
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [windows-latest, macos-latest, ubuntu-latest]
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install briefcase
        pip install -r requirements.txt
    - name: Build app
      run: briefcase package
```

## Next Steps

1. **Test thoroughly** on target platforms
2. **Create proper icons** for professional appearance
3. **Set up code signing** for distribution (especially macOS)
4. **Create installation guides** for end users
5. **Set up automated builds** for releases

## Resources

- [Briefcase Documentation](https://briefcase.readthedocs.io/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Platform-specific packaging guides](https://briefcase.readthedocs.io/en/stable/how-to/)
