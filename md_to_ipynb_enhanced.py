#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将Markdown文件转换为Jupyter Notebook文件，并为代码示例添加必要的导入语句
"""

import os
import re
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

def add_imports_to_code(code):
    """
    为代码示例添加必要的导入语句
    
    Args:
        code (str): 原始代码
    
    Returns:
        str: 添加了导入语句的代码
    """
    # 检查代码中使用的库
    uses_torch = 'torch' in code or 'nn' in code or 'F.' in code
    uses_numpy = 'numpy' in code or 'np.' in code
    uses_matplotlib = 'matplotlib' in code or 'plt.' in code
    
    # 构建导入语句
    imports = []
    if uses_torch:
        imports.append('import torch')
        imports.append('import torch.nn as nn')
        imports.append('import torch.nn.functional as F')
    if uses_numpy:
        imports.append('import numpy as np')
    if uses_matplotlib:
        imports.append('import matplotlib.pyplot as plt')
    
    # 如果有导入语句，添加到代码开头
    if imports:
        import_str = '\n'.join(imports) + '\n\n'
        code = import_str + code
    
    return code

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
    
    # 分离Markdown和代码块
    # 正则表达式匹配代码块： ```python ... ```
    code_blocks = re.findall(r'```python\s*\n(.*?)\s*\n```', md_content, re.DOTALL)
    markdown_parts = re.split(r'```python\s*\n.*?\s*\n```', md_content, re.DOTALL)
    
    # 交替添加Markdown和代码单元格
    for i, markdown_part in enumerate(markdown_parts):
        # 添加Markdown单元格
        if markdown_part.strip():
            md_cell = new_markdown_cell(source=markdown_part)
            nb.cells.append(md_cell)
        
        # 添加代码单元格（如果有）
        if i < len(code_blocks):
            code = code_blocks[i]
            # 添加导入语句
            code_with_imports = add_imports_to_code(code)
            # 创建代码单元格
            code_cell = new_code_cell(source=code_with_imports)
            nb.cells.append(code_cell)
    
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
