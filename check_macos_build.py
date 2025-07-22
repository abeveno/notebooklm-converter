#!/usr/bin/env python3
"""
macOS Build Checker and Guide
Kiểm tra môi trường và hướng dẫn build cho macOS
"""

import sys
import os
import platform
import subprocess
import shutil

def check_platform():
    """Kiểm tra platform hiện tại"""
    current_os = platform.system()
    print(f"🖥️  Hệ điều hành hiện tại: {current_os}")
    
    if current_os == "Darwin":
        print("✅ Đang chạy trên macOS - Có thể build trực tiếp!")
        return "macos"
    elif current_os == "Windows":
        print("🪟 Đang chạy trên Windows - Cần phương pháp khác")
        return "windows"
    elif current_os == "Linux":
        print("🐧 Đang chạy trên Linux - Cần phương pháp khác")
        return "linux"
    else:
        print(f"❓ Hệ điều hành không xác định: {current_os}")
        return "unknown"

def check_macos_requirements():
    """Kiểm tra yêu cầu cho macOS build"""
    print("\n🔍 Kiểm tra yêu cầu macOS build:")
    
    # Kiểm tra Python
    try:
        python_version = sys.version_info
        print(f"🐍 Python {python_version.major}.{python_version.minor}.{python_version.micro}")
        if python_version >= (3, 8):
            print("✅ Python version đủ yêu cầu")
        else:
            print("❌ Cần Python 3.8 trở lên")
            return False
    except:
        print("❌ Không tìm thấy Python")
        return False
    
    # Kiểm tra Xcode Command Line Tools
    try:
        result = subprocess.run(['xcode-select', '--print-path'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Xcode Command Line Tools: {result.stdout.strip()}")
        else:
            print("❌ Xcode Command Line Tools chưa được cài đặt")
            print("   Chạy: xcode-select --install")
            return False
    except FileNotFoundError:
        print("❌ Xcode Command Line Tools không có")
        return False
    
    # Kiểm tra Briefcase
    try:
        import briefcase
        print(f"✅ Briefcase đã cài đặt: {briefcase.__version__}")
    except ImportError:
        print("⚠️  Briefcase chưa cài đặt")
        print("   Chạy: pip install briefcase")
    
    return True

def show_github_actions_guide():
    """Hiển thị hướng dẫn GitHub Actions"""
    print("""
🎯 PHƯƠNG PHÁP KHUYẾN NGHỊ: GitHub Actions (Tự động)

📋 Các bước thực hiện:

1️⃣  Tạo GitHub Repository:
   - Vào github.com và tạo repository mới
   - Tên gợi ý: notebooklm-converter

2️⃣  Upload code lên GitHub:
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/USERNAME/notebooklm-converter.git
   git push -u origin main

3️⃣  Kích hoạt GitHub Actions:
   - File .github/workflows/build.yml đã được tạo sẵn
   - GitHub sẽ tự động build khi bạn push code
   - Hoặc vào tab "Actions" và click "Run workflow"

4️⃣  Tải về kết quả:
   - Vào tab "Actions" trong GitHub repo
   - Click vào build job mới nhất  
   - Tải về "macos-installer" artifact
   - Bên trong có file .dmg cho macOS

✅ Ưu điểm:
   - Hoàn toàn miễn phí
   - Tự động build khi có thay đổi
   - Build cho Windows, macOS, Linux cùng lúc
   - Không cần máy Mac

🎉 Đây là cách dễ nhất và hiệu quả nhất!
""")

def show_direct_build_guide():
    """Hiển thị hướng dẫ build trực tiếp trên macOS"""
    print("""
🛠️  BUILD TRỰC TIẾP TRÊN macOS

📋 Các bước thực hiện:

1️⃣  Cài đặt dependencies:
   pip install briefcase
   pip install -r requirements.txt

2️⃣  Tạo icon:
   cd src/notebooklm_converter/resources
   python create_icon.py
   cd ../../..

3️⃣  Build ứng dụng:
   briefcase create macOS
   briefcase build macOS
   briefcase package macOS

4️⃣  Hoặc chạy script tự động:
   chmod +x build_macos.sh
   ./build_macos.sh

📁 Kết quả:
   - App: build/notebooklm-converter/macOS/app/NotebookLM Converter.app
   - DMG: dist/NotebookLM Converter-1.0.0.dmg

✅ Ưu điểm:
   - Build nhanh (5-10 phút)
   - Kiểm soát hoàn toàn
   - Test ngay lập tức
""")

def show_alternative_methods():
    """Hiển thị các phương pháp thay thế"""
    print("""
🔄 CÁC PHƯƠNG PHÁP THAY THẾ:

1️⃣  Nhờ người có Mac:
   - Gửi source code cho bạn bè/đồng nghiệp có Mac
   - Họ chạy script build_macos.sh
   - Nhận lại file DMG

2️⃣  macOS Cloud Services:
   - GitHub Codespaces (macOS)
   - MacStadium
   - AWS EC2 Mac instances

3️⃣  macOS Virtual Machine:
   - Chỉ hợp pháp trên phần cứng Apple
   - VMware Fusion / Parallels Desktop
   - Cần license macOS

📊 Khuyến nghị:
   👑 GitHub Actions - Tốt nhất cho hầu hết trường hợp
   🥈 Build trực tiếp - Nếu có Mac
   🥉 Nhờ người khác - Giải pháp tạm thời
""")

def main():
    """Main function"""
    print("🍎 NotebookLM Converter - macOS Build Guide")
    print("=" * 50)
    
    current_platform = check_platform()
    
    if current_platform == "macos":
        # Đang chạy trên macOS
        if check_macos_requirements():
            print("\n🎉 Môi trường sẵn sàng cho build trực tiếp!")
            show_direct_build_guide()
        else:
            print("\n⚠️  Môi trường chưa đủ yêu cầu")
            print("Hãy cài đặt các dependency cần thiết")
    else:
        # Đang chạy trên platform khác
        print(f"\n💡 Đang chạy trên {current_platform}, không thể build macOS trực tiếp")
        show_github_actions_guide()
        show_alternative_methods()
    
    print("\n📖 Tài liệu chi tiết:")
    print("   - MACOS_COMPLETE_GUIDE.md - Hướng dẫn toàn diện")
    print("   - MACOS_BUILD_GUIDE.md - Hướng dẫn build chi tiết")
    print("   - .github/workflows/build.yml - GitHub Actions workflow")
    
    print("\n🚀 Chúc bạn build thành công!")

if __name__ == "__main__":
    main()
