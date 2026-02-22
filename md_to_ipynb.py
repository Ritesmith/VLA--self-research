#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将Markdown文件转换为Jupyter Notebook文件
"""

import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

def md_to_ipynb(md_path, ipynb_path):
    """
    将Markdown文件转换为Jupyter Notebook文件
    
    Args:
        md_path (str): Markdown文件路径
        ipynb_path (str): 输出的Jupyter Notebook文件路径
    """
    # 读取Markdown文件内容
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # 创建新的Notebook
    nb = new_notebook()
    
    # 添加Markdown内容作为一个单元格
    md_cell = new_markdown_cell(source=md_content)
    nb.cells.append(md_cell)
    
    # 保存为.ipynb文件
    with open(ipynb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"转换完成: {md_path} -> {ipynb_path}")

def batch_convert():
    """
    批量转换所有技术细节的MD文件为IPYNB文件
    """
    # 技术细节目录列表
    tech_dirs = [
        "流匹配技术",
        "残差向量量化",
        "具身先验注入",
        "双系统架构",
        "强化学习微调",
        "无标签数据利用",
        "跨具身泛化",
        "模型蒸馏",
        "多模态融合",
        "世界模型集成"
    ]
    
    # 基础路径
    base_path = "技术栈"
    
    # 逐个转换
    for tech_dir in tech_dirs:
        # MD文件路径
        md_path = os.path.join(base_path, tech_dir, f"{tech_dir}详细介绍.md")
        
        # 检查MD文件是否存在
        if not os.path.exists(md_path):
            print(f"警告: {md_path} 不存在")
            continue
        
        # IPYNB文件路径
        ipynb_path = os.path.join(base_path, tech_dir, f"{tech_dir}详细介绍.ipynb")
        
        # 转换
        md_to_ipynb(md_path, ipynb_path)

if __name__ == "__main__":
    batch_convert()
