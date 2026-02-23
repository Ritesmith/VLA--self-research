#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析PDF文件内容，确定论文主题并进行分类
"""

import os
import re

# 尝试导入PDF处理库
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

def extract_text_from_pdf(pdf_path):
    """
    从PDF文件中提取文本
    
    Args:
        pdf_path (str): PDF文件路径
    
    Returns:
        str: 提取的文本内容
    """
    text = ""
    
    if pdf_library == 'PyPDF2':
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                
                # 提取前10页的内容，通常包含标题、摘要和引言
                for i in range(min(10, num_pages)):
                    page = reader.pages[i]
                    text += page.extract_text() + '\n'
        except Exception as e:
            print(f"Error extracting text with PyPDF2: {e}")
            return ""
    
    elif pdf_library == 'pdfplumber':
        try:
            with pdfplumber.open(pdf_path) as pdf:
                num_pages = len(pdf.pages)
                
                # 提取前10页的内容
                for i in range(min(10, num_pages)):
                    page = pdf.pages[i]
                    text += page.extract_text() + '\n'
        except Exception as e:
            print(f"Error extracting text with pdfplumber: {e}")
            return ""
    
    return text

def analyze_paper_topic(text):
    """
    分析论文主题
    
    Args:
        text (str): 论文文本内容
    
    Returns:
        str: 论文主题分类
    """
    # 转换为小写以便匹配
    text_lower = text.lower()
    
    # 定义关键词和对应的分类
    categories = {
        "流匹配技术": ["flow matching", "flow-matching", "continuous time", "ode"],
        "残差向量量化": ["residual vector quantization", "rvq", "vector quantization"],
        "具身先验注入": ["embodied prior", "prior injection", "kinematics", "3d perception"],
        "双系统架构": ["dual system", "fast-slow", "two-system", "system 1 system 2"],
        "强化学习微调": ["reinforcement learning", "fine-tuning", "rl fine-tuning", "stable fine-tuning"],
        "无标签数据利用": ["unlabeled data", "self-supervised", "contrastive learning", "decisionnce"],
        "跨具身泛化": ["cross-embodiment", "zero-shot generalization", "embodiment transfer"],
        "模型蒸馏": ["model distillation", "knowledge distillation", "distillation"],
        "多模态融合": ["multimodal fusion", "vision-language-action", "vla", "multimodal integration"],
        "世界模型集成": ["world model", "physics model", "environment prediction", "causal reasoning"]
    }
    
    # 计算每个分类的关键词匹配数
    category_scores = {}
    for category, keywords in categories.items():
        score = 0
        for keyword in keywords:
            if keyword in text_lower:
                score += 1
        category_scores[category] = score
    
    # 找到得分最高的分类
    if category_scores:
        best_category = max(category_scores, key=category_scores.get)
        best_score = category_scores[best_category]
        
        # 如果最高得分大于0，则返回该分类
        if best_score > 0:
            return best_category
    
    # 默认分类
    return "其他VLA技术"

def get_paper_info(text):
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
        "topic": ""
    }
    
    # 尝试提取标题（通常是文本的前几行）
    lines = text.split('\n')
    title_lines = []
    for line in lines[:20]:  # 前20行通常包含标题
        line = line.strip()
        if line and len(line) > 10:  # 标题通常较长
            title_lines.append(line)
            if len(title_lines) >= 3:  # 标题通常不超过3行
                break
    info["title"] = ' '.join(title_lines)
    
    # 尝试提取摘要
    abstract_match = re.search(r'abstract[\s:]*\n(.*?)(?:\n\n|\n1\.|\nintroduction)', text, re.DOTALL | re.IGNORECASE)
    if abstract_match:
        info["abstract"] = abstract_match.group(1).strip()
    
    # 分析主题
    info["topic"] = analyze_paper_topic(text)
    
    return info

def classify_pdf(pdf_path):
    """
    分类PDF文件
    
    Args:
        pdf_path (str): PDF文件路径
    """
    print(f"分析文件: {pdf_path}")
    
    # 提取文本
    text = extract_text_from_pdf(pdf_path)
    
    if not text:
        print("无法提取PDF文本内容")
        return
    
    # 分析论文信息
    paper_info = get_paper_info(text)
    
    # 输出论文信息
    print("\n论文信息:")
    print(f"标题: {paper_info['title']}")
    print(f"摘要: {paper_info['abstract'][:300]}...")  # 只显示摘要前300个字符
    print(f"分类: {paper_info['topic']}")
    
    # 检查目标分类目录是否存在
    category_dir = os.path.join("技术栈", paper_info["topic"])
    if not os.path.exists(category_dir):
        print(f"\n警告: 分类目录 {category_dir} 不存在")
        return
    
    # 复制文件到分类目录
    pdf_filename = os.path.basename(pdf_path)
    dest_path = os.path.join(category_dir, pdf_filename)
    
    try:
        import shutil
        shutil.copy2(pdf_path, dest_path)
        print(f"\n文件已复制到: {dest_path}")
    except Exception as e:
        print(f"\n无法复制文件: {e}")

if __name__ == "__main__":
    pdf_path = r"PDFs\2601.22153v1.pdf"
    classify_pdf(pdf_path)
