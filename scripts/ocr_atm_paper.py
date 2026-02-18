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

pdf_file = "PDFs/ATM_RSS2024/2401.00025v3.pdf"
output_file = "第四天前沿/ATM_RSS2024.txt"

print(f"处理ATM论文: {pdf_file} -> {output_file}")

if os.path.exists(pdf_file):
    print(f"Processing {pdf_file}...")
    try:
        ocr_pdf(pdf_file, output_file)
        print(f"✓ Successfully processed {pdf_file} -> {output_file}")
    except Exception as e:
        print(f"✗ Error processing {pdf_file}: {e}")
else:
    print(f"✗ File not found: {pdf_file}")

print("\nATM论文OCR处理完成!")
