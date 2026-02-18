import os
import shutil

pdf_mapping = {
    "2212.06817v2.pdf": "第三周补充/RT-1_2022.txt",
    "2403.01823v2.pdf": "第三周补充/RT-H_2024.3.txt",
    "2406.09246v3.pdf": "第一周重点/OpenVLA_2024.6.txt",
    "2410.07864v2.pdf": "第二周深入/RDT-1B_2024.10.txt",
    "2410.24164v4.pdf": "第一周重点/Pi_0_2025.2.txt",
    "4775_PaLM_E_An_Embodied_Multim.pdf": "第三周补充/PaLM-E_2023.3.txt",
    "zitkovich23a.pdf": "第一周重点/RT-2_2023.7.txt",
}

print("PDF文件映射关系:")
for pdf, txt in pdf_mapping.items():
    print(f"  {pdf} -> {txt}")

print("\n开始重新整理文件...")

for pdf_file, output_file in pdf_mapping.items():
    if os.path.exists(pdf_file):
        print(f"✓ {pdf_file} 存在")
    else:
        print(f"✗ {pdf_file} 不存在")

print("\n文件整理完成!")
