# 📄 Files - Universal PDF Converter

<div align="center">

![Files Logo](https://img.shields.io/badge/Files-PDF%20Converter-blue?style=for-the-badge&logo=files&logoColor=white)

**Transform any file into PDF with just one click!**

[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=flat-square&logo=vercel)](https://vercel.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=flat-square&logo=flask)](https://flask.palletsprojects.com)

</div>

## ✨ Features

- 🖼️ **Image Conversion** - PNG, JPG, JPEG, BMP, TIFF, GIF
- 📝 **Text Files** - TXT, Markdown (MD)
- 📄 **Word Documents** - DOCX format
- 📊 **Excel Spreadsheets** - XLSX, XLS formats
- 🚀 **Batch Processing** - Convert multiple files at once
- 💨 **Lightning Fast** - Instant conversion and download
- 📱 **Responsive Design** - Works on all devices
- 🔒 **Privacy First** - Files processed temporarily and deleted

## 🎯 Quick Start

### Online Usage
Visit the deployed application and start converting files instantly!

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd convert-to-pdf
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **PDF Generation**: ReportLab
- **Image Processing**: Pillow (PIL)
- **Document Processing**: python-docx, openpyxl
- **Deployment**: Vercel

## 📁 Project Structure

```
Files/
├── app.py                    # Flask application
├── file_to_pdf_converter.py  # Core conversion logic
├── templates/
│   └── index.html           # Web interface
├── requirements.txt         # Python dependencies
├── vercel.json             # Vercel configuration
└── README.md               # Project documentation
```

## 🚀 Deployment

This project is optimized for **Vercel** deployment:

1. Fork this repository
2. Connect to Vercel
3. Deploy with one click!

The `vercel.json` configuration handles everything automatically.

## 📋 Supported Formats

| Category | Formats |
|----------|---------|
| **Images** | PNG, JPG, JPEG, BMP, TIFF, GIF |
| **Text** | TXT, MD (Markdown) |
| **Documents** | DOCX (Word) |
| **Spreadsheets** | XLSX, XLS (Excel) |

## 🎨 Features Showcase

- **Modern UI/UX** - Beautiful gradient design with smooth animations
- **Drag & Drop** - Intuitive file selection
- **Real-time Feedback** - Loading states and error handling
- **Mobile Responsive** - Perfect on all screen sizes
- **Batch Processing** - Handle multiple files efficiently

## 🔧 API Endpoints

- `GET /` - Main application interface
- `POST /convert` - Single file conversion
- `POST /batch-convert` - Multiple file conversion

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

**Umar J Dev**
- Passionate about creating useful web applications
- Focused on clean code and user experience

---

<div align="center">

**Made with ❤️ by Umar J Dev**

*Transform your files, simplify your workflow*

</div>