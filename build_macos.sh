#!/bin/bash

# macOS Build Script for NotebookLM Converter
# Script tự động để build ứng dụng macOS

echo "🍎 NotebookLM Converter - macOS Build Script"
echo "============================================"

# Kiểm tra hệ điều hành
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Script này chỉ chạy trên macOS"
    exit 1
fi

# Kiểm tra Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "🐍 Python version: $python_version"

# Kiểm tra Xcode Command Line Tools
if ! command -v xcode-select &> /dev/null; then
    echo "❌ Xcode Command Line Tools chưa được cài đặt"
    echo "Chạy: xcode-select --install"
    exit 1
fi

echo "✅ Xcode Command Line Tools đã được cài đặt"

# Tạo virtual environment (khuyến nghị)
if [ ! -d "venv" ]; then
    echo "📦 Tạo virtual environment..."
    python3 -m venv venv
fi

echo "🔧 Kích hoạt virtual environment..."
source venv/bin/activate

# Cài đặt dependencies
echo "📥 Cài đặt dependencies..."
pip install --upgrade pip
pip install briefcase
pip install -r requirements.txt

# Tạo icon (nếu chưa có)
if [ ! -f "src/notebooklm_converter/resources/icon.icns" ]; then
    echo "🎨 Tạo icon cho macOS..."
    cd src/notebooklm_converter/resources
    python create_icon.py
    cd ../../..
fi

# Build process
echo "🏗️ Bắt đầu build process..."

# Step 1: Create
echo "1️⃣ Creating macOS app structure..."
briefcase create macOS

if [ $? -ne 0 ]; then
    echo "❌ Lỗi khi tạo app structure"
    exit 1
fi

# Step 2: Build
echo "2️⃣ Building macOS app..."
briefcase build macOS

if [ $? -ne 0 ]; then
    echo "❌ Lỗi khi build app"
    exit 1
fi

# Step 3: Test run (optional)
echo "3️⃣ Testing built app..."
echo "Bạn có muốn test ứng dụng trước khi package? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    briefcase run macOS
fi

# Step 4: Package
echo "4️⃣ Creating DMG package..."
briefcase package macOS

if [ $? -ne 0 ]; then
    echo "❌ Lỗi khi tạo package"
    exit 1
fi

# Hiển thị kết quả
echo ""
echo "🎉 BUILD THÀNH CÔNG!"
echo "=================="
echo "📱 App file: build/notebooklm-converter/macOS/app/NotebookLM Converter.app"
echo "💿 DMG file: dist/NotebookLM Converter-1.0.0.dmg"
echo ""
echo "🚀 Các bước tiếp theo:"
echo "1. Test ứng dụng: open 'build/notebooklm-converter/macOS/app/NotebookLM Converter.app'"
echo "2. Test DMG: open 'dist/NotebookLM Converter-1.0.0.dmg'"
echo "3. Chia sẻ DMG với người dùng khác"
echo ""

# Mở thư mục chứa kết quả
if command -v open &> /dev/null; then
    echo "📂 Mở thư mục chứa file build..."
    open dist/
fi

echo "✅ Hoàn thành!"
