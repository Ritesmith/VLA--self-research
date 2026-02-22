import os
import fitz

# 处理2602.03310v1.pdf文件
pdf_file = "PDFs\\2602.03310v1.pdf"
output_file = "PDFs\\2602.03310v1.txt"

if os.path.exists(pdf_file):
    print(f"Processing {pdf_file}...")
    try:
        # 打开PDF文件
        pdf_document = fitz.open(pdf_file)
        text = ""
        
        # 提取每一页的文本
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += "\n--- Page " + str(page_num + 1) + " ---\n"
            text += page.get_text()
            text += "\n"
        
        # 关闭PDF文件
        pdf_document.close()
        
        # 保存提取的文本
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"✓ Successfully processed {pdf_file} -> {output_file}")
        print("\nFirst 5000 characters:")
        print(text[:5000])
    except Exception as e:
        print(f"✗ Error processing {pdf_file}: {e}")
else:
    print(f"✗ File not found: {pdf_file}")

print("\nProcessing completed!")