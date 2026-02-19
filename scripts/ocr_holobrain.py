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

# OCR HoloBrain-0 PDF
pdf_file = r"d:\Stazica\my_files\University_works\self study\VLA--self-research\PDFs\2602.12062v1.pdf"
output_file = r"d:\Stazica\my_files\University_works\self study\VLA--self-research\第五天前沿技术深入研究\HoloBrain-0\HoloBrain-0_2025.txt"

print(f"Processing {pdf_file}...")

if os.path.exists(pdf_file):
    try:
        ocr_pdf(pdf_file, output_file)
        print(f"Successfully processed {pdf_file} -> {output_file}")
    except Exception as e:
        print(f"Error processing {pdf_file}: {e}")
else:
    print(f"File not found: {pdf_file}")

print("\nDone!")
