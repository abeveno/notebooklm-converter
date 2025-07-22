# 🍎 Hướng dẫn toàn diện: Tạo phiên bản macOS cho NotebookLM Converter

## 📋 Tổng quan

Có nhiều cách để tạo phiên bản macOS cho ứng dụng NotebookLM Converter của bạn. Dưới đây là tất cả các phương pháp từ dễ đến khó:

## 🎯 Phương pháp 1: GitHub Actions (Khuyến nghị - Tự động)

### Ưu điểm:
- ✅ Hoàn toàn miễn phí
- ✅ Tự động build khi push code
- ✅ Build cho cả Windows, macOS, Linux cùng lúc
- ✅ Không cần máy Mac

### Cách thực hiện:

1. **Push code lên GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/username/notebooklm-converter.git
   git push -u origin main
   ```

2. **File workflow đã được tạo tại**: `.github/workflows/build.yml`

3. **Kích hoạt build**:
   - Push code lên GitHub
   - Hoặc vào Actions tab và click "Run workflow"

4. **Tải về kết quả**:
   - Vào tab "Actions" trong GitHub repo
   - Click vào build job mới nhất
   - Tải về "macos-installer" artifact
   - Bên trong sẽ có file `.dmg` cho macOS

## 🖥️ Phương pháp 2: Build trực tiếp trên macOS

### Yêu cầu:
- Máy Mac (macOS 10.14+)
- Python 3.8+
- Xcode Command Line Tools

### Cách thực hiện:

1. **Chuẩn bị môi trường**:
   ```bash
   # Cài đặt Xcode Command Line Tools
   xcode-select --install
   
   # Clone hoặc copy project về Mac
   cd /path/to/project
   ```

2. **Chạy script tự động**:
   ```bash
   # Cấp quyền thực thi
   chmod +x build_macos.sh
   
   # Chạy script build
   ./build_macos.sh
   ```

3. **Hoặc build thủ công**:
   ```bash
   # Cài đặt dependencies
   pip install briefcase
   pip install -r requirements.txt
   
   # Tạo icon
   cd src/notebooklm_converter/resources
   python create_icon.py
   cd ../../..
   
   # Build process
   briefcase create macOS
   briefcase build macOS
   briefcase package macOS
   ```

4. **Kết quả**:
   - App: `build/notebooklm-converter/macOS/app/NotebookLM Converter.app`
   - DMG: `dist/NotebookLM Converter-1.0.0.dmg`

## ☁️ Phương pháp 3: macOS Cloud Services

### Các dịch vụ khả dụng:

1. **GitHub Codespaces**:
   - Tạo macOS codespace
   - Chạy build commands trong browser

2. **MacStadium**:
   - Thuê macOS cloud instance
   - Remote desktop để build

3. **AWS EC2 Mac**:
   - macOS instances trên AWS
   - Tính phí theo giờ

### Ưu điểm:
- Không cần máy Mac vật lý
- Có thể build occasional

### Nhược điểm:
- Có phí
- Cần setup phức tạp hơn

## 🖥️ Phương pháp 4: macOS Virtual Machine

### ⚠️ Lưu ý pháp lý:
- Chỉ được phép chạy macOS VM trên phần cứng Apple
- Cần license macOS hợp lệ

### Cách thực hiện (trên Mac hardware):

1. **VMware Fusion** hoặc **Parallels Desktop**
2. **Tạo macOS VM**
3. **Cài đặt development tools**
4. **Chạy build process**

## 🤝 Phương pháp 5: Nhờ người khác build

### Cách thực hiện:

1. **Chuẩn bị code**:
   ```bash
   # Tạo archive của project
   zip -r notebooklm-converter.zip . -x "*.git*" "build/*" "dist/*"
   ```

2. **Gửi cho người có Mac** kèm hướng dẫn:
   ```
   1. Unzip file
   2. cd notebooklm-converter
   3. chmod +x build_macos.sh
   4. ./build_macos.sh
   5. Gửi lại file trong thư mục dist/
   ```

## 📊 So sánh các phương pháp

| Phương pháp | Chi phí | Độ khó | Tự động | Thời gian |
|-------------|---------|--------|---------|-----------|
| GitHub Actions | Miễn phí | Dễ | ✅ | 10-15 phút |
| Mac trực tiếp | Có Mac | Trung bình | ❌ | 5-10 phút |
| Cloud Service | $$ | Khó | Một phần | 15-30 phút |
| Virtual Machine | Mac hardware | Khó | ❌ | 20-40 phút |
| Nhờ người khác | Miễn phí | Dễ | ❌ | Tùy thuộc |

## 🎯 Khuyến nghị

### Cho developer cá nhân:
1. **GitHub Actions** (phương pháp 1) - Tốt nhất cho hầu hết trường hợp
2. **Nhờ bạn bè có Mac** (phương pháp 5) - Nếu có người quen

### Cho team/công ty:
1. **GitHub Actions** cho CI/CD
2. **Mac mini** trong văn phòng cho development
3. **MacStadium** cho scale lớn

## 🔧 Troubleshooting

### Lỗi thường gặp:

1. **"xcode-select: error: tool 'xcodebuild' requires Xcode"**:
   ```bash
   xcode-select --install
   ```

2. **"Permission denied"**:
   ```bash
   chmod +x build_macos.sh
   ```

3. **"Module not found"**:
   ```bash
   pip install -r requirements.txt
   ```

4. **"Code signing failed"**:
   ```bash
   # Tạm thời skip code signing
   briefcase package macOS --adhoc-sign
   ```

## 📱 Test ứng dụng macOS

### Sau khi build thành công:

1. **Test DMG**:
   ```bash
   open "dist/NotebookLM Converter-1.0.0.dmg"
   ```

2. **Test App**:
   ```bash
   open "build/notebooklm-converter/macOS/app/NotebookLM Converter.app"
   ```

3. **Test các tính năng**:
   - File selection (single/multiple)
   - Conversion (PDF/TXT/Markdown)
   - Error handling
   - UI responsiveness

## 🚀 Phân phối

### Cho người dùng cuối:

1. **Upload DMG lên**:
   - GitHub Releases
   - Google Drive / Dropbox
   - Website riêng

2. **Hướng dẫn cài đặt**:
   ```
   1. Download file .dmg
   2. Double-click để mount
   3. Drag "NotebookLM Converter" vào Applications
   4. Launch từ Applications folder
   ```

3. **Xử lý Gatekeeper**:
   - Người dùng có thể cần right-click → Open lần đầu
   - Hoặc System Preferences → Security → Allow

## 🎉 Kết luận

**GitHub Actions** là phương pháp tốt nhất cho việc tạo phiên bản macOS của NotebookLM Converter. Nó miễn phí, tự động, và không yêu cầu phần cứng Mac.

Với workflow đã setup, mỗi lần bạn push code, GitHub sẽ tự động tạo ra file DMG cho macOS sẵn sàng phân phối!
