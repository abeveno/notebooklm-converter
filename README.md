# NotebookLM Converter 🍎

Ứng dụng chuyển đổi EPUB thành các định dạng phù hợp với NotebookLM, hỗ trợ đa nền tảng (Windows, macOS, Linux).

## Tính năng

✅ **Input Formats - Hỗ trợ đầu vào:**
- **EPUB** - Electronic Publication
- **MOBI** - Amazon Kindle Format
- **AZW/AZW3** - Amazon Kindle Advanced Format
- **KFX** - Kindle Format X (yêu cầu Calibre + Plugin)
- **iBooks** - Apple iBooks Format
- **CBR/CBZ** - Comic Book Archive

✅ **Output Formats - Tối ưu cho NotebookLM:**
- **PDF** - Định dạng tài liệu với typography tối ưu
- **TXT** - Văn bản thuần túy được làm sạch cho AI
- **Markdown** - Cấu trúc văn bản có metadata cho AI analysis

## Yêu cầu hệ thống

- Python 3.7 trở lên
- Windows/macOS/Linux
- Calibre (cho MOBI, AZW, KFX formats)

## Cài đặt

### 1. Cài đặt Python dependencies

```bash
pip install EbookLib beautifulsoup4 lxml xhtml2pdf markdown pillow rarfile
```

Hoặc sử dụng file requirements:
```bash
pip install -r requirements.txt
```

### 2. Cài đặt Calibre (tùy chọn)

Cần thiết cho: MOBI, AZW/AZW3, KFX formats
- Tải và cài đặt [Calibre](https://calibre-ebook.com/download)
- Đảm bảo Calibre được thêm vào PATH

## Cách sử dụng

1. **Chạy ứng dụng:**
   ```bash
   python main.py
   ```

2. **Chọn file sách điện tử:**
   - Nhấp vào "1. Chọn file sách điện tử"
   - Hỗ trợ: EPUB, MOBI, AZW/AZW3, KFX, iBooks, CBR/CBZ

3. **Chọn định dạng đầu ra:**
   - **PDF**: Tài liệu được format đẹp cho NotebookLM
   - **TXT**: Văn bản sạch, tối ưu cho AI processing
   - **Markdown**: Cấu trúc có metadata cho AI analysis

4. **Chọn tối ưu hóa:**
   - **Chuẩn**: Chuyển đổi thông thường
   - **NotebookLM**: Tối ưu đặc biệt cho NotebookLM
   - **AI-Ready**: Chuẩn bị tối ưu cho AI systems

5. **Chuyển đổi:**
   - Nhấp "3. Chuyển đổi cho NotebookLM"
   - Chọn vị trí lưu file
   - Chờ quá trình hoàn tất

## Tối ưu hóa cho NotebookLM

### PDF Output
- Typography tối ưu cho đọc và phân tích
- Cấu trúc heading rõ ràng
- Font và spacing phù hợp cho AI processing

### TXT Output
- Loại bỏ ký tự đặc biệt không cần thiết
- Cấu trúc đoạn văn tối ưu
- Metadata header cho NotebookLM
- Làm sạch encoding và formatting

### Markdown Output
- YAML frontmatter với metadata
- Cấu trúc heading có logic
- Formatting tối ưu cho AI analysis
- Timestamp và quality info

## Input Format Support

| Format | Hỗ trợ | Yêu cầu đặc biệt |
|--------|--------|------------------|
| EPUB | ✅ Full | Built-in |
| MOBI | ✅ Full | Calibre |
| AZW/AZW3 | ✅ Full | Calibre |
| KFX | ⚠️ Limited | Calibre + KFX Plugin |
| iBooks | ✅ Good | Built-in (như EPUB) |
| CBR/CBZ | ⚠️ Basic | Chỉ extract info cơ bản |

## Troubleshooting

### Lỗi thường gặp

**1. ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**2. Lỗi MOBI/AZW conversion**
- Cài đặt Calibre: https://calibre-ebook.com/download
- Thêm Calibre vào system PATH

**3. Lỗi KFX format**
- Cài đặt Calibre KFX Input Plugin
- Restart Calibre sau khi cài plugin

**4. Lỗi CBR files**
- Cài đặt WinRAR hoặc 7-Zip
- Thêm vào system PATH

## NotebookLM Integration Tips

1. **Cho PDF**: Upload trực tiếp vào NotebookLM
2. **Cho TXT**: Copy-paste hoặc upload as text file
3. **Cho Markdown**: Upload hoặc convert sang PDF trong NotebookLM

## Benchmark Performance

- **EPUB → PDF**: ~30-60 giây cho sách 300 trang
- **EPUB → TXT**: ~10-20 giây cho sách 300 trang  
- **EPUB → Markdown**: ~15-30 giây cho sách 300 trang
- **MOBI → Any**: +10-30 giây (do conversion step)

## Changelog

### v2.0 - NotebookLM Optimization
- Chuyển từ All-in-One Converter
- Tối ưu hóa đặc biệt cho NotebookLM
- Hỗ trợ multiple input formats
- AI-ready text processing
