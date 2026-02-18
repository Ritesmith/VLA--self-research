import os
import fitz

# 确保fitz库已安装
try:
    import fitz
except ImportError:
    print("Error: fitz library not installed. Please run 'pip install PyMuPDF'")
    exit(1)

def ocr_pdf(pdf_path, output_path):
    """Extract text from PDF file"""
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += "\n--- Page " + str(page_num + 1) + " ---\n"
            text += page.get_text()
            text += "\n"
        
        pdf_document.close()
        
        # 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        return text
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None

# RT-X论文处理
pdf_file = "RT-X_2023.10\\2310.08864v9.pdf"
output_file = "../第二周深入/RT-X_2023.10.txt"

if os.path.exists(pdf_file):
    print(f"Processing RT-X paper...")
    try:
        text = ocr_pdf(pdf_file, output_file)
        if text:
            print(f"✓ Successfully processed RT-X paper -> {output_file}")
        else:
            print(f"✗ Failed to process RT-X paper")
    except Exception as e:
        print(f"✗ Error processing RT-X paper: {e}")
else:
    print(f"✗ File not found: {pdf_file}")

print("\nRT-X PDF processed!")