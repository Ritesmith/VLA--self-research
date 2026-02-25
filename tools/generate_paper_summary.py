#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取PDF文本内容并生成论文总结
"""

import os
import re

try:
    import PyPDF2
    pdf_library = 'PyPDF2'
except ImportError:
    try:
        import pdfplumber
        pdf_library = 'pdfplumber'
    except ImportError:
        print("Error: No PDF processing library found. Please install PyPDF2 or pdfplumber.")
        exit(1)

def extract_full_text_from_pdf(pdf_path):
    """
    从PDF文件中提取完整文本
    
    Args:
        pdf_path (str): PDF文件路径
    
    Returns:
        str: 提取的完整文本内容
    """
    text = ""
    
    if pdf_library == 'PyPDF2':
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                
                print(f"提取PDF文本，共 {num_pages} 页...")
                
                for i in range(num_pages):
                    page = reader.pages[i]
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n=== 第 {i+1} 页 ===\n"
                        text += page_text + '\n'
                        
                    # 显示进度
                    if (i + 1) % 5 == 0:
                        print(f"已提取 {i+1}/{num_pages} 页")
        except Exception as e:
            print(f"Error extracting text with PyPDF2: {e}")
            return ""
    
    elif pdf_library == 'pdfplumber':
        try:
            with pdfplumber.open(pdf_path) as pdf:
                num_pages = len(pdf.pages)
                
                print(f"提取PDF文本，共 {num_pages} 页...")
                
                for i in range(num_pages):
                    page = pdf.pages[i]
                    page_text = page.extract_text()
                    if page_text:
                        text += f"\n=== 第 {i+1} 页 ===\n"
                        text += page_text + '\n'
                        
                    # 显示进度
                    if (i + 1) % 5 == 0:
                        print(f"已提取 {i+1}/{num_pages} 页")
        except Exception as e:
            print(f"Error extracting text with pdfplumber: {e}")
            return ""
    
    print(f"文本提取完成，共 {len(text)} 字符")
    return text

def extract_paper_info(text):
    """
    从文本中提取论文信息
    
    Args:
        text (str): 论文文本内容
    
    Returns:
        dict: 论文信息
    """
    info = {
        "title": "",
        "authors": "",
        "abstract": "",
        "introduction": "",
        "methodology": "",
        "experiments": "",
        "conclusion": ""
    }
    
    # 提取标题（通常是文本的前几行）
    lines = text.split('\n')
    title_lines = []
    author_lines = []
    
    # 收集可能的标题和作者行
    for i, line in enumerate(lines[:50]):  # 前50行通常包含标题和作者
        line = line.strip()
        if line:
            # 标题通常较长且可能包含关键词
            if len(line) > 20 and not line.startswith('==='):
                title_lines.append(line)
            # 作者行通常包含多个名字和邮箱
            elif '@' in line or ('author' in line.lower() and 's' in line.lower()):
                author_lines.append(line)
            # 如果已经收集了标题，且遇到可能的作者行
            elif title_lines and ('and' in line or ',' in line) and not line.startswith('==='):
                author_lines.append(line)
    
    # 合并标题行
    if title_lines:
        info["title"] = ' '.join(title_lines[:3])  # 最多取前3行作为标题
    
    # 合并作者行
    if author_lines:
        info["authors"] = ' '.join(author_lines[:2])  # 最多取前2行作为作者
    
    # 提取摘要
    abstract_match = re.search(r'abstract[\s:]*\n(.*?)(?:\n\n\n|\n1\.|\nintroduction|\nsection 1)', text, re.DOTALL | re.IGNORECASE)
    if abstract_match:
        info["abstract"] = abstract_match.group(1).strip()
    
    # 提取引言
    intro_match = re.search(r'(?:introduction|1\.)[\s:]*\n(.*?)(?:\n\n\n|\n2\.|\nmethod|\nsection 2)', text, re.DOTALL | re.IGNORECASE)
    if intro_match:
        info["introduction"] = intro_match.group(1).strip()
    
    # 提取方法
    method_match = re.search(r'(?:method|methodology|2\.)[\s:]*\n(.*?)(?:\n\n\n|\n3\.|\nexperiment|\nsection 3)', text, re.DOTALL | re.IGNORECASE)
    if method_match:
        info["methodology"] = method_match.group(1).strip()
    
    # 提取实验
    exp_match = re.search(r'(?:experiment|experimental|3\.)[\s:]*\n(.*?)(?:\n\n\n|\n4\.|\nconclusion|\nsection 4)', text, re.DOTALL | re.IGNORECASE)
    if exp_match:
        info["experiments"] = exp_match.group(1).strip()
    
    # 提取结论
    conclusion_match = re.search(r'(?:conclusion|4\.)[\s:]*\n(.*?)(?:\n\n\n|\nreference|\nacknowledgment)', text, re.DOTALL | re.IGNORECASE)
    if conclusion_match:
        info["conclusion"] = conclusion_match.group(1).strip()
    
    return info

def generate_summary(paper_info):
    """
    基于论文信息生成总结
    
    Args:
        paper_info (dict): 论文信息
    
    Returns:
        str: 论文总结
    """
    summary = f"# {paper_info['title']}\n\n"
    
    if paper_info['authors']:
        summary += f"## 作者\n{paper_info['authors']}\n\n"
    
    summary += "## 摘要\n"
    if paper_info['abstract']:
        summary += f"{paper_info['abstract'][:500]}...\n\n"  # 限制摘要长度
    else:
        summary += "摘要未提取到\n\n"
    
    summary += "## 引言\n"
    if paper_info['introduction']:
        summary += f"{paper_info['introduction'][:300]}...\n\n"  # 限制引言长度
    else:
        summary += "引言未提取到\n\n"
    
    summary += "## 方法\n"
    if paper_info['methodology']:
        summary += f"{paper_info['methodology'][:500]}...\n\n"  # 限制方法长度
    else:
        summary += "方法未提取到\n\n"
    
    summary += "## 实验\n"
    if paper_info['experiments']:
        summary += f"{paper_info['experiments'][:300]}...\n\n"  # 限制实验长度
    else:
        summary += "实验未提取到\n\n"
    
    summary += "## 结论\n"
    if paper_info['conclusion']:
        summary += f"{paper_info['conclusion'][:300]}...\n\n"  # 限制结论长度
    else:
        summary += "结论未提取到\n\n"
    
    summary += "## 分类\n流匹配技术\n\n"
    
    summary += "## 学习建议\n"
    summary += "1. 重点理解DynamicVLA如何处理动态对象操作\n"
    summary += "2. 分析其与传统VLA模型的区别\n"
    summary += "3. 尝试复现核心算法\n"
    summary += "4. 与其他流匹配技术论文进行对比分析\n"
    
    return summary

def process_paper(pdf_path, output_dir):
    """
    处理论文，生成OCR结果和总结
    
    Args:
        pdf_path (str): PDF文件路径
        output_dir (str): 输出目录
    """
    print(f"处理论文: {pdf_path}")
    
    # 提取完整文本
    full_text = extract_full_text_from_pdf(pdf_path)
    
    if not full_text:
        print("无法提取PDF文本内容")
        return
    
    # 保存OCR结果
    ocr_output_path = os.path.join(output_dir, "OCR结果.txt")
    with open(ocr_output_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"OCR结果已保存到: {ocr_output_path}")
    
    # 提取论文信息
    paper_info = extract_paper_info(full_text)
    
    # 生成总结
    summary = generate_summary(paper_info)
    
    # 保存总结
    summary_output_path = os.path.join(output_dir, "论文总结.md")
    with open(summary_output_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"论文总结已保存到: {summary_output_path}")

if __name__ == "__main__":
    pdf_path = r"技术栈\流匹配技术\2601.22153v1.pdf"
    output_dir = r"第六天学习"
    process_paper(pdf_path, output_dir)
