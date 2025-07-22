# Hướng dẫn tạo phiên bản macOS cho NotebookLM Converter

## 🍎 Yêu cầu để build cho macOS

### 1. Môi trường phát triển
- **macOS**: Phải chạy trên máy Mac (macOS 10.14 trở lên)
- **Python 3.8+**: Đã cài đặt Python
- **Xcode Command Line Tools**: Cần thiết cho việc build

### 2. Cài đặt Xcode Command Line Tools
```bash
xcode-select --install
```

### 3. Cài đặt Briefcase và dependencies
```bash
# Cài đặt Briefcase
pip install briefcase

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

## 🚀 Các bước tạo ứng dụng macOS

### Bước 1: Thiết lập môi trường
```bash
# Chuyển đến thư mục dự án
cd /path/to/notebooklm-converter

# Chạy script thiết lập
python setup_dev.py
```

### Bước 2: Tạo cấu trúc ứng dụng macOS
```bash
briefcase create macOS
```

### Bước 3: Build ứng dụng
```bash
briefcase build macOS
```

### Bước 4: Chạy thử ứng dụng
```bash
briefcase run macOS
```

### Bước 5: Tạo file DMG để phân phối
```bash
briefcase package macOS
```

## 📦 Kết quả

Sau khi hoàn thành, bạn sẽ có:
- **Ứng dụng**: `build/notebooklm-converter/macOS/app/NotebookLM Converter.app`
- **DMG installer**: `dist/NotebookLM Converter-1.0.0.dmg`

## 🔧 Cấu hình macOS-specific trong pyproject.toml

File `pyproject.toml` đã được cấu hình với các thông số cho macOS:

```toml
[tool.briefcase.app.notebooklm-converter.macOS]
requires = [
    "toga-cocoa~=0.4.0",
    "std-nslog~=1.0.0"
]
```

## 🎨 Tùy chỉnh cho macOS

### 1. Icon cho macOS
Tạo file icon.icns cho macOS:
```bash
cd src/notebooklm_converter/resources
python create_icon.py

# Chuyển đổi PNG thành ICNS (nếu cần)
iconutil -c icns icon.iconset
```

### 2. App Bundle Information
Cấu hình thông tin ứng dụng trong pyproject.toml:
```toml
[tool.briefcase.app.notebooklm-converter]
formal_name = "NotebookLM Converter"
description = "Convert ebooks to formats optimized for NotebookLM"
bundle = "com.notebooklm.converter"
```

### 3. Permissions (nếu cần)
Thêm permissions vào Info.plist nếu ứng dụng cần truy cập file:
```xml
<key>NSDocumentsFolderUsageDescription</key>
<string>This app needs access to documents to convert ebook files.</string>
```

## 🚨 Xử lý lỗi thường gặp

### 1. Lỗi Xcode Command Line Tools
```bash
# Kiểm tra xem đã cài đặt chưa
xcode-select -p

# Nếu chưa có, cài đặt
xcode-select --install
```

### 2. Lỗi permission denied
```bash
# Cấp quyền thực thi
chmod +x briefcase
```

### 3. Lỗi missing dependencies
```bash
# Cài đặt lại dependencies
pip install --upgrade briefcase
pip install -r requirements.txt
```

### 4. Lỗi code signing (nếu muốn phân phối rộng rãi)
```bash
# Tạm thời skip code signing cho test
briefcase package macOS --adhoc-sign
```

## 📱 Tính năng macOS-specific

### 1. App Bundle Structure
```
NotebookLM Converter.app/
├── Contents/
│   ├── Info.plist
│   ├── MacOS/
│   │   └── NotebookLM Converter
│   ├── Resources/
│   │   ├── icon.icns
│   │   └── app/
│   └── Frameworks/
```

### 2. Native macOS Integration
- **File associations**: Có thể mở file EPUB/MOBI bằng cách double-click
- **Spotlight search**: Ứng dụng xuất hiện trong Spotlight
- **Dock integration**: Icon hiển thị trong Dock
- **Menu bar**: Native macOS menu

## 🔒 Code Signing và Notarization (Tùy chọn)

### Để phân phối rộng rãi, bạn cần:

1. **Apple Developer Account**: $99/năm
2. **Code Signing Certificate**: Từ Apple Developer
3. **Notarization**: Xác thực từ Apple

```bash
# Code signing (cần Developer Certificate)
codesign --force --verify --verbose --sign "Developer ID Application: Your Name" "NotebookLM Converter.app"

# Notarization (cần Apple ID)
xcrun altool --notarize-app --primary-bundle-id "com.notebooklm.converter" --username "your@apple.id" --password "@keychain:AC_PASSWORD" --file "NotebookLM Converter.dmg"
```

## 🎯 Testing trên macOS

### 1. Test cơ bản
```bash
# Chạy từ source
python src/notebooklm_converter/app.py

# Chạy built app
briefcase run macOS
```

### 2. Test file associations
- Kéo thả file EPUB vào ứng dụng
- Kiểm tra tất cả định dạng file được hỗ trợ
- Test batch conversion

### 3. Test UI trên macOS
- Kiểm tra giao diện trên macOS
- Test keyboard shortcuts
- Kiểm tra menu bar

## 📋 Checklist hoàn thành

- [ ] Cài đặt Xcode Command Line Tools
- [ ] Chạy `python setup_dev.py` thành công
- [ ] `briefcase create macOS` thành công
- [ ] `briefcase build macOS` thành công  
- [ ] `briefcase run macOS` chạy được ứng dụng
- [ ] Test tất cả tính năng conversion
- [ ] `briefcase package macOS` tạo được DMG
- [ ] Test cài đặt từ DMG

## 🎉 Kết quả cuối cùng

Sau khi hoàn thành, bạn sẽ có:
1. **NotebookLM Converter.app** - Ứng dụng macOS native
2. **NotebookLM Converter.dmg** - File installer để phân phối
3. Ứng dụng tích hợp đầy đủ với macOS ecosystem

File DMG có thể được chia sẻ với người dùng macOS khác để cài đặt và sử dụng!
