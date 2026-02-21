"""
PDF OCR和自动归档脚本

功能：
1. 对PDFs文件夹中的未归档PDF进行OCR处理
2. 分析论文标题
3. 与已有论文对比
4. 将新论文归档到第五天文件夹
"""

import os
import sys
import shutil
import PyPDF2
from pathlib import Path

# 配置
PDF_DIR = r'd:\Stazica\my_files\University_works\self study\VLA--self-research\PDFs'
DAY5_DIR = r'd:\Stazica\my_files\University_works\self study\VLA--self-research\第五天前沿技术深入研究'
ALREADY_ARCHIVED = [
    'OpenVLA_2024.6',
    'Pi_0_2025.2',
    'RT-2_2023.7',
    'RDT-1B_2024.10',
    'RT-X_2023.10',
    'RT-1_2022',
    'PaLM-E_2023.3',
    'RT-H_2024.3',
    'ATM_RSS2024',
    'ConRFT_RSS2025',
    'DecisionNCE_ICML2024',
    'FiS-VLA_2025',
    'GeminiRobotics_2025',
    'HoloBrain-0_2025',
    'iRe-VLA_ICRA2025',
    'CoReVLA_2025',
]

def get_pdf_title(pdf_path):
    """从PDF中提取标题"""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            
            # 方法1: 从元数据中获取
            if reader.metadata and reader.metadata.title:
                title = reader.metadata.title.strip()
                if title and title != 'Unknown':
                    return title
            
            # 方法2: 从第一页内容中获取标题
            if len(reader.pages) > 0:
                first_page_text = reader.pages[0].extract_text()
                lines = first_page_text.split('\n')
                
                # 尝试找到标题行（通常在前面，较长）
                for line in lines[:20]:
                    line = line.strip()
                    # 过滤掉页码、arXiv编号等
                    if line and len(line) > 20 and not line.startswith('arXiv') and not line.startswith('http'):
                        # 检查是否包含论文标题特征
                        if ':' in line or not line.isupper():
                            return line[:200]  # 限制长度
            
            return "未知标题"
    except Exception as e:
        print(f"  错误: {e}")
        return None

def perform_ocr(pdf_path, output_txt_path):
    """对PDF进行OCR处理"""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            
            with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(f"论文OCR文本\n\n")
                txt_file.write(f"源文件: {os.path.basename(pdf_path)}\n\n")
                
                for i, page in enumerate(reader.pages, 1):
                    txt_file.write(f"=== 第{i}页 ===\n")
                    text = page.extract_text()
                    txt_file.write(text)
                    txt_file.write("\n\n")
            
            print(f"  OCR完成: {len(reader.pages)}页")
            return True
    except Exception as e:
        print(f"  OCR错误: {e}")
        return False

def generate_summary(pdf_path, ocr_text_path, title):
    """生成基于OCR的论文总结"""
    try:
        # 读取OCR文本
        with open(ocr_text_path, 'r', encoding='utf-8') as f:
            ocr_text = f.read()
        
        # 提取摘要部分
        abstract_start = ocr_text.find('Abstract')
        abstract = ""
        if abstract_start != -1:
            abstract_end = ocr_text.find('\n\n', abstract_start + 100)
            if abstract_end != -1:
                abstract = ocr_text[abstract_start:abstract_end].strip()
        
        # 提取引言部分
        intro_start = ocr_text.find('I. INTRODUCTION')
        intro = ""
        if intro_start != -1:
            intro_end = ocr_text.find('\nII.', intro_start + 100)
            if intro_end != -1:
                intro = ocr_text[intro_start:intro_end].strip()
        
        # 生成总结
        summary = f"""# {title}

**PDF文件**: {os.path.basename(pdf_path)}
**归档时间**: 2026-02-21

---

## 📋 基本信息

**标题**: {title}

**论文类型**: 会议/期刊论文

---

## 🎯 摘要

{abstract[:1000] if abstract else "暂无摘要"}

---

## 📝 引言

{intro[:1000] if intro else "暂无引言"}

---

## 🔗 相关信息

**arXiv编号**: {os.path.basename(pdf_path).replace('.pdf', '')}
**OCR文本**: {os.path.basename(ocr_text_path)}

---

**文档创建时间**: 2026-02-21
**基于**: PDF OCR文本自动生成
"""
        
        return summary
    except Exception as e:
        print(f"  生成总结错误: {e}")
        return None

def is_new_paper(title, already_archived):
    """判断是否为新论文"""
    # 简单的标题匹配
    for archived in already_archived:
        if archived.lower().replace('_', ' ') in title.lower():
            return False
    return True

def create_folder_name(title, arxiv_id):
    """创建文件夹名称"""
    # 移除特殊字符
    safe_title = title.replace(':', ' ').replace('/', ' ').replace('?', '')
    # 取前50个字符
    safe_title = safe_title[:50].strip()
    # 添加arXiv编号
    folder_name = f"{safe_title}_{arxiv_id}"
    return folder_name

def process_pdfs():
    """处理PDFs文件夹中的未归档PDF"""
    # 设置输出编码
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # 获取所有PDF文件
    pdf_files = []
    for file in os.listdir(PDF_DIR):
        if file.endswith('.pdf') and not os.path.isdir(os.path.join(PDF_DIR, file)):
            # 跳过已归档的
            if not any(folder.lower() in file.lower() for folder in ALREADY_ARCHIVED):
                pdf_files.append(file)
    
    print(f"找到 {len(pdf_files)} 个未归档PDF文件")
    print("=" * 80)
    
    # 处理每个PDF
    for pdf_file in sorted(pdf_files):
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        print(f"\n处理: {pdf_file}")
        print("-" * 80)
        
        # 提取标题
        title = get_pdf_title(pdf_path)
        print(f"标题: {title}")
        
        # 检查是否为新论文
        if not is_new_paper(title, ALREADY_ARCHIVED):
            print(f"状态: 已归档，跳过")
            continue
        
        # 创建文件夹
        arxiv_id = pdf_file.replace('.pdf', '')
        folder_name = create_folder_name(title, arxiv_id)
        paper_dir = os.path.join(DAY5_DIR, folder_name)
        
        print(f"文件夹: {folder_name}")
        
        # 创建文件夹
        os.makedirs(paper_dir, exist_ok=True)
        
        # 复制PDF
        pdf_copy_path = os.path.join(paper_dir, pdf_file)
        if not os.path.exists(pdf_copy_path):
            shutil.copy2(pdf_path, pdf_copy_path)
            print(f"  PDF已复制")
        
        # OCR处理
        ocr_txt_name = f"{arxiv_id}.txt"
        ocr_txt_path = os.path.join(paper_dir, ocr_txt_name)
        
        if not os.path.exists(ocr_txt_path):
            if perform_ocr(pdf_path, ocr_txt_path):
                print(f"  OCR完成")
        else:
            print(f"  OCR已存在，跳过")
        
        # 生成总结
        summary_md_name = f"{arxiv_id}_论文总结.md"
        summary_md_path = os.path.join(paper_dir, summary_md_name)
        
        if not os.path.exists(summary_md_path):
            summary = generate_summary(pdf_path, ocr_txt_path, title)
            if summary:
                with open(summary_md_path, 'w', encoding='utf-8') as f:
                    f.write(summary)
                print(f"  总结已生成")
        else:
            print(f"  总结已存在，跳过")
        
        print(f"完成: {folder_name}")
        print("=" * 80)

if __name__ == '__main__':
    print("PDF OCR和自动归档脚本")
    print("=" * 80)
    process_pdfs()
    print("\n所有处理完成！")
