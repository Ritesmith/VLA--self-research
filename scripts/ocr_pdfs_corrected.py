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
    ("2212.06817v2.pdf", "第三周补充/RT-1_2022.txt"),
    ("2403.01823v2.pdf", "第三周补充/RT-H_2024.3.txt"),
    ("2406.09246v3.pdf", "第一周重点/OpenVLA_2024.6.txt"),
    ("2410.07864v2.pdf", "第二周深入/RDT-1B_2024.10.txt"),
    ("2410.24164v4.pdf", "第一周重点/Pi_0_2025.2.txt"),
    ("4775_PaLM_E_An_Embodied_Multim.pdf", "第三周补充/PaLM-E_2023.3.txt"),
    ("zitkovich23a.pdf", "第一周重点/RT-2_2023.7.txt"),
]

print("正确的PDF文件映射关系:")
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
