import os
import fitz

def ocr_pdf(pdf_path, output_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += f"\n--- Page {page_num + 1} ---\n"
        text += page.get_text()
        text += "\n"
    
    pdf_document.close()
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    return text

pdf_files = [
    ("PDFs/ATM_RSS2024/2402.15467v1.pdf", "第四天前沿/ATM_RSS2024.txt"),
    ("PDFs/DecisionNCE_ICML2024/2402.18137v2.pdf", "第四天前沿/DecisionNCE_ICML2024.txt"),
    ("PDFs/ConRFT_RSS2025/2502.05450v2.pdf", "第四天前沿/ConRFT_RSS2025.txt"),
    ("PDFs/GeminiRobotics_2025/2503.20020v1.pdf", "第四天前沿/GeminiRobotics_2025.txt"),
    ("PDFs/FiS-VLA_2025/2506.01953v1.pdf", "第四天前沿/FiS-VLA_2025.txt"),
]

print("第四天前沿论文OCR处理:")
for pdf, txt in pdf_files:
    print(f"  {pdf} -> {txt}")

print("\n开始OCR处理...")

for pdf_file, output_file in pdf_files:
    pdf_path = pdf_file
    output_path = output_file
    
    if os.path.exists(pdf_path):
        print(f"Processing {pdf_file}...")
        try:
            ocr_pdf(pdf_path, output_path)
            print(f"✓ Successfully processed {pdf_file} -> {output_file}")
        except Exception as e:
            print(f"✗ Error processing {pdf_file}: {e}")
    else:
        print(f"✗ File not found: {pdf_file}")

print("\nAll PDFs processed!")
