#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF文件OCR处理脚本
功能：
1. 遍历PDFs文件夹中的所有PDF文件
2. 对每个PDF文件进行OCR处理
3. 从OCR结果中提取标题
4. 与已归档的论文标题进行比较
5. 如果是新论文，将OCR结果和基于OCR的总结放到第五天的文件夹
"""

import os
import fitz
import re
import shutil

# 配置路径
PDFS_DIR = "d:\\Stazica\\my_files\\University_works\\self study\\VLA--self-research\\PDFs"
FIFTH_DAY_DIR = "d:\\Stazica\\my_files\\University_works\\self study\\VLA--self-research\\第五天前沿技术深入研究"

# 已归档的论文标题列表（从PDF文件汇总报告中提取）
ARCHIVED_TITLES = [
    "LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models",
    "Genie: Generative Interactive Environments",
    "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models",
    "RoboCLIP: One Demonstration is Enough to Learn Robot Policies",
    "Sim2Real2Sim: Bridging the Gap with Learnable World Models",
    "CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine"
]

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
        
        with open(output_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(text)
        
        return text
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return None

def extract_title(ocr_text):
    """从OCR文本中提取论文标题"""
    if not ocr_text:
        return "Unknown Title"
    
    # 尝试从OCR文本的前几行提取标题
    lines = ocr_text.split('\n')
    title_lines = []
    
    # 跳过空行和页码行
    for line in lines[:50]:  # 只检查前50行
        line = line.strip()
        if line and not re.match(r'^\d+$', line) and not line.startswith('Page'):
            title_lines.append(line)
            if len(title_lines) >= 3:  # 标题最多3行
                break
    
    if title_lines:
        return ' '.join(title_lines)
    else:
        return "Unknown Title"

def is_new_paper(title):
    """检查是否是新论文"""
    if not title or title == "Unknown Title":
        return True  # 未知标题的论文也视为新论文
    
    # 与已归档标题比较
    for archived_title in ARCHIVED_TITLES:
        if title.lower() in archived_title.lower() or archived_title.lower() in title.lower():
            return False
    
    return True

def generate_summary(ocr_text):
    """基于OCR文本生成简要总结"""
    if not ocr_text:
        return "无法生成总结：OCR处理失败"
    
    # 提取摘要部分
    abstract_pattern = re.compile(r'abstract\s*[:\.]?\s*(.*?)(?:\\n\\n|\\n---|introduction|\\n\\s*1\\.)', re.DOTALL | re.IGNORECASE)
    abstract_match = abstract_pattern.search(ocr_text)
    
    abstract = ""
    if abstract_match:
        abstract = abstract_match.group(1).strip()
    
    # 提取关键词
    keywords_pattern = re.compile(r'keywords?\s*[:\.]?\s*(.*?)(?:\\n\\n|\\n---|abstract|introduction)', re.DOTALL | re.IGNORECASE)
    keywords_match = keywords_pattern.search(ocr_text)
    
    keywords = ""
    if keywords_match:
        keywords = keywords_match.group(1).strip()
    
    # 生成总结
    summary = f"# 论文总结\n\n"
    summary += f"## 摘要\n{abstract if abstract else '未找到摘要部分'}\n\n"
    summary += f"## 关键词\n{keywords if keywords else '未找到关键词部分'}\n\n"
    summary += "## 内容概览\n本文档包含论文的完整OCR结果，详细内容请参考OCR文本文件。\n"
    
    return summary

def process_pdf(pdf_path):
    """处理单个PDF文件"""
    pdf_name = os.path.basename(pdf_path)
    pdf_base = os.path.splitext(pdf_name)[0]
    
    print(f"\n=== 处理文件: {pdf_name} ===")
    
    # 1. 生成OCR结果
    ocr_text = ocr_pdf(pdf_path, os.path.join(os.path.dirname(pdf_path), f"{pdf_base}.txt"))
    
    if not ocr_text:
        print(f"❌ OCR处理失败: {pdf_name}")
        return False
    
    # 2. 提取标题
    title = extract_title(ocr_text)
    print(f"📄 提取标题: {title}")
    
    # 3. 检查是否是新论文
    if is_new_paper(title):
        print(f"✨ 发现新论文: {title}")
        
        # 4. 创建第五天文件夹
        # 用标题的前50个字符作为文件夹名
        folder_name = re.sub(r'[^a-zA-Z0-9\s_-]', '', title)[:50].strip()
        folder_name = folder_name.replace(' ', '_') + f"_{pdf_base}"
        target_folder = os.path.join(FIFTH_DAY_DIR, folder_name)
        
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        # 5. 复制PDF文件
        target_pdf = os.path.join(target_folder, pdf_name)
        shutil.copy2(pdf_path, target_pdf)
        print(f"📋 复制PDF文件到: {target_pdf}")
        
        # 6. 复制OCR结果
        target_ocr = os.path.join(target_folder, f"{pdf_base}.txt")
        shutil.copy2(os.path.join(os.path.dirname(pdf_path), f"{pdf_base}.txt"), target_ocr)
        print(f"📋 复制OCR结果到: {target_ocr}")
        
        # 7. 生成并保存总结
        summary = generate_summary(ocr_text)
        target_summary = os.path.join(target_folder, f"{pdf_base}_论文总结.md")
        with open(target_summary, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"📋 生成论文总结到: {target_summary}")
        
        return True
    else:
        print(f"📌 已归档论文: {title}")
        return False

def main():
    """主函数"""
    print("🚀 开始处理PDF文件...")
    print(f"📁 处理目录: {PDFS_DIR}")
    print(f"🎯 目标目录: {FIFTH_DAY_DIR}")
    
    # 遍历PDFs文件夹
    processed_count = 0
    new_papers_count = 0
    
    for root, dirs, files in os.walk(PDFS_DIR):
        # 跳过子文件夹，只处理根目录的PDF文件
        if root != PDFS_DIR:
            continue
        
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                if process_pdf(pdf_path):
                    new_papers_count += 1
                processed_count += 1
    
    print(f"\n=== 处理完成 ===")
    print(f"📊 处理文件数: {processed_count}")
    print(f"✨ 新论文数: {new_papers_count}")
    print(f"🎯 新论文已保存到第五天文件夹")

if __name__ == "__main__":
    main()
