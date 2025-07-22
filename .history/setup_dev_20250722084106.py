#!/usr/bin/env python3
"""
Setup script for NotebookLM Converter development environment
This script helps set up the development environment and dependencies.
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} is compatible")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\n📦 Installing Python dependencies...")
    
    # Core dependencies
    dependencies = [
        "briefcase>=0.3.16",
        "EbookLib>=0.18",
        "beautifulsoup4>=4.11.0",
        "lxml>=4.9.0", 
        "xhtml2pdf>=0.2.5",
        "markdown>=3.4.0",
        "Pillow>=9.0.0",
        "rarfile>=4.0",
    ]
    
    for dep in dependencies:
        if not run_command(f"pip install {dep}", f"Installing {dep}"):
            return False
    
    return True

def setup_project_structure():
    """Ensure project structure is correct"""
    print("\n📁 Setting up project structure...")
    
    directories = [
        "src/notebooklm_converter",
        "src/notebooklm_converter/resources",
        "tests",
        "docs"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"✅ Created directory: {directory}")
        else:
            print(f"✅ Directory exists: {directory}")
    
    return True

def check_briefcase():
    """Check if Briefcase is working"""
    print("\n🎁 Checking Briefcase installation...")
    return run_command("briefcase --version", "Testing Briefcase")

def platform_specific_setup():
    """Setup platform-specific requirements"""
    current_platform = platform.system().lower()
    print(f"\n🖥️ Setting up for {current_platform}...")
    
    if current_platform == "darwin":  # macOS
        print("📱 macOS detected")
        print("ℹ️  Make sure Xcode command line tools are installed:")
        print("   xcode-select --install")
        
    elif current_platform == "windows":  # Windows
        print("🪟 Windows detected")
        print("ℹ️  Make sure Visual Studio Build Tools are installed")
        print("   Download from: https://visualstudio.microsoft.com/downloads/")
        
    elif current_platform == "linux":  # Linux
        print("🐧 Linux detected")
        print("ℹ️  System packages will be handled by Briefcase")
    
    return True

def check_calibre():
    """Check if Calibre is installed (optional)"""
    print("\n📚 Checking Calibre installation (optional)...")
    if run_command("ebook-convert --version", "Testing Calibre"):
        print("✅ Calibre is available for MOBI/AZW support")
    else:
        print("⚠️  Calibre not found - MOBI/AZW conversion will not work")
        print("   Install from: https://calibre-ebook.com/download")

def main():
    """Main setup function"""
    print("🚀 NotebookLM Converter Development Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup project structure
    if not setup_project_structure():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check Briefcase
    if not check_briefcase():
        print("❌ Briefcase setup failed. Please install it manually:")
        print("   pip install briefcase")
        sys.exit(1)
    
    # Platform-specific setup
    platform_specific_setup()
    
    # Check Calibre (optional)
    check_calibre()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Create the Briefcase app:     briefcase create")
    print("2. Build the application:       briefcase build") 
    print("3. Run the application:         briefcase run")
    print("4. Package for distribution:    briefcase package")
    print("\n🔧 Development commands:")
    print("- Run from source:              python src/notebooklm_converter/app.py")
    print("- Run tests:                    python -m pytest tests/")

if __name__ == "__main__":
    main()
