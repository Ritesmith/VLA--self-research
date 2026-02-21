# OCR iRe-VLA PDF
import fitz

pdf_file = r"d:\Stazica\my_files\University_works\self study\VLA--self-research\PDFs\iRe-VLA_ICRA2025\2501.16664v1.pdf"
output_file = r"d:\Stazica\my_files\University_works\self study\VLA--self-research\第五天前沿技术深入研究\iRe-VLA\iRe-VLA_2025.txt"

# 打开PDF
doc = fitz.open(pdf_file)

# 提取所有页面的文本
full_text = ""
for page_num, page in enumerate(doc):
    text = page.get_text()
    full_text += f"\n{'='*80}\n"
    full_text += f"Page {page_num + 1}\n"
    full_text += f"{'='*80}\n"
    full_text += text + "\n"

# 保存到文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(full_text)

total_pages = len(doc)

doc.close()

print("[OK] OCR complete!")
print(f"[Input] {pdf_file}")
print(f"[Output] {output_file}")
print(f"[Total pages] {total_pages}")
