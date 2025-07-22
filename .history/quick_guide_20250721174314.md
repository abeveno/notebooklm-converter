# Hướng dẫn nhanh - NotebookLM Converter

## Bắt đầu nhanh

### 1. Cài đặt dependencies
```bash
# Chạy file batch (Windows)
install_dependencies.bat

# Hoặc chạy manual
pip install -r requirements.txt
```

### 2. Chạy ứng dụng
```bash
# Cách 1: Chạy file batch
run_converter.bat

# Cách 2: Chạy trực tiếp
python main.py

# Cách 3: Chạy demo
python demo.py
```

## Input Formats - Định dạng đầu vào

| Định dạng | Mô tả | Yêu cầu đặc biệt |
|-----------|-------|------------------|
| EPUB | Electronic Publication | ✅ Có sẵn |
| MOBI | Amazon Kindle Format | ⚠️ Cần Calibre |
| AZW/AZW3 | Amazon Advanced Format | ⚠️ Cần Calibre |
| KFX | Kindle Format X | ⚠️ Cần Calibre + Plugin |
| iBooks | Apple iBooks | ✅ Có sẵn |
| CBR/CBZ | Comic Book Archive | ⚠️ Hỗ trợ cơ bản |

## Output Formats - Tối ưu cho NotebookLM

| Định dạng | Mô tả | Đặc biệt cho NotebookLM |
|-----------|-------|-------------------------|
| PDF | Tài liệu PDF tối ưu | Typography + Structure tối ưu cho AI |
| TXT | Văn bản thuần túy | Cleaned text + Metadata header |
| Markdown | Cấu trúc Markdown | YAML frontmatter + AI-ready format |

## Tối ưu hóa NotebookLM

### Chế độ tối ưu hóa

**Chuẩn**: Chuyển đổi thông thường
**NotebookLM**: Tối ưu đặc biệt cho NotebookLM
**AI-Ready**: Chuẩn bị tốt nhất cho AI processing

### Tips cho NotebookLM

1. **PDF format** tốt nhất cho upload trực tiếp
2. **Markdown** tốt cho việc edit và customize
3. **TXT** nhanh nhất, phù hợp cho văn bản đơn giản

## Troubleshooting

### Lỗi thường gặp

**1. ModuleNotFoundError**
- Chạy: `pip install -r requirements.txt`

**2. Lỗi MOBI/AZW conversion**
- Cài đặt Calibre: https://calibre-ebook.com/download
- Thêm Calibre vào PATH
- Restart terminal sau khi cài

**3. Lỗi KFX format**
- Cài Calibre KFX Input Plugin
- Restart Calibre
- Thử convert trong Calibre trước

**4. Lỗi Comic Book (CBR)**
- Cài WinRAR hoặc 7-Zip
- Thêm vào system PATH

**5. GUI không hiển thị**
- Kiểm tra Python có hỗ trợ tkinter
- Windows: Thường có sẵn
- Linux: `sudo apt-get install python3-tk`

### Performance Tips

- File lớn (>50MB) có thể mất vài phút
- MOBI/AZW cần thêm thời gian conversion
- PDF output mất thời gian nhất (do typography processing)
- TXT nhanh nhất

## Workflow with NotebookLM

### 1. Chuẩn bị file
```
Sách điện tử → NotebookLM Converter → PDF/TXT/MD
```

### 2. Upload vào NotebookLM
- **PDF**: Upload trực tiếp
- **TXT**: Copy-paste hoặc upload
- **Markdown**: Upload hoặc convert sang PDF

### 3. Tối ưu hóa cho AI
- Chọn mode "NotebookLM" hoặc "AI-Ready"
- File output sẽ có metadata và structure tối ưu

## File Structure

```
converter/
├── main.py                 # NotebookLM Converter chính
├── demo.py                 # Demo script
├── requirements.txt        # Python dependencies (updated)
├── README.md              # Hướng dẫn chi tiết
├── quick_guide.md         # File này
├── run_converter.bat      # Script chạy ứng dụng (Windows)
└── install_dependencies.bat # Script cài đặt (Windows)
```

## Supported Workflows

### Research Papers → NotebookLM
EPUB/PDF → TXT (AI-Ready) → NotebookLM Analysis

### Books → Study Notes
EPUB → Markdown (NotebookLM) → Edit → NotebookLM

### Technical Docs → AI Processing
MOBI → PDF (NotebookLM) → Upload → AI Analysis

## Contact & Support

- Xem README.md để biết thêm chi tiết
- Test với demo.py trước khi dùng file thật
- Báo bug qua Issues
