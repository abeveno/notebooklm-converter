# Quick Start Script cho macOS
# Chạy script này để build nhanh ứng dụng macOS

param(
    [switch]$SkipTest = $false
)

Write-Host "🍎 NotebookLM Converter - Quick macOS Build" -ForegroundColor Green
Write-Host "=========================================="

# Kiểm tra nếu đang chạy trên Windows
if ($IsWindows -or $env:OS -eq "Windows_NT") {
    Write-Host "⚠️  Script này dành cho macOS build. Trên Windows hãy dùng:" -ForegroundColor Yellow
    Write-Host "   briefcase create windows"
    Write-Host "   briefcase build windows"  
    Write-Host "   briefcase package windows"
    Write-Host ""
    Write-Host "🍎 Để build cho macOS, bạn cần:"
    Write-Host "1. Máy Mac hoặc macOS virtual machine"
    Write-Host "2. Chạy script build_macos.sh trên macOS"
    Write-Host "3. Hoặc sử dụng GitHub Actions để build tự động"
    exit 1
}

# Hướng dẫn cho Windows users
Write-Host "📋 Hướng dẫn build macOS từ Windows:" -ForegroundColor Cyan
Write-Host ""
Write-Host "Option 1: Sử dụng GitHub Actions (Khuyến nghị)"
Write-Host "1. Push code lên GitHub repository"
Write-Host "2. Tạo .github/workflows/build.yml"
Write-Host "3. GitHub sẽ tự động build cho macOS, Windows, Linux"
Write-Host ""
Write-Host "Option 2: Sử dụng macOS Virtual Machine"
Write-Host "1. Cài đặt VMware/VirtualBox"
Write-Host "2. Tạo macOS VM (cần license hợp lệ)"
Write-Host "3. Chạy build script trong VM"
Write-Host ""
Write-Host "Option 3: Thuê macOS cloud service"
Write-Host "1. MacStadium, AWS EC2 Mac, GitHub Codespaces"
Write-Host "2. Upload code và build từ xa"
Write-Host ""
Write-Host "Option 4: Tìm người có Mac giúp build"
Write-Host "1. Gửi source code cho người có Mac"
Write-Host "2. Họ chạy build_macos.sh"
Write-Host "3. Nhận file DMG hoàn thành"
