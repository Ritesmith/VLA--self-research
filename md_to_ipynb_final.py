#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将Markdown文件转换为Jupyter Notebook文件，并为代码示例添加必要的导入语句
"""

import os
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
    uses_torch = 'torch' in code or 'nn' in code or 'F.' in code or 'torch.' in code
    uses_numpy = 'numpy' in code or 'np.' in code
    uses_matplotlib = 'matplotlib' in code or 'plt.' in code
    uses_time = 'time' in code or 'time.' in code
    uses_json = 'json' in code or 'json.' in code
    uses_random = 'random' in code or 'random.' in code
    
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
    if uses_time:
        imports.append('import time')
    if uses_json:
        imports.append('import json')
    if uses_random:
        imports.append('import random')
    
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
        content = f.read()
    
    # 创建新的Notebook
    nb = new_notebook()
    
    # 分割内容为行
    lines = content.split('\n')
    
    # 处理内容，构建单元格
    current_cell = []
    in_code_block = False
    code_language = ''
    
    for line in lines:
        # 检查代码块开始
        if line.strip().startswith('```'):
            if not in_code_block:
                # 代码块开始
                in_code_block = True
                code_language = line.strip()[3:].strip()
                
                # 如果当前有Markdown内容，创建Markdown单元格
                if current_cell:
                    md_content = '\n'.join(current_cell)
                    if md_content.strip():
                        md_cell = new_markdown_cell(source=md_content)
                        nb.cells.append(md_cell)
                    current_cell = []
            else:
                # 代码块结束
                in_code_block = False
                
                # 创建代码单元格
                if code_language == 'python':
                    code_content = '\n'.join(current_cell)
                    code_with_imports = add_imports_to_code(code_content)
                    code_cell = new_code_cell(source=code_with_imports)
                    nb.cells.append(code_cell)
                current_cell = []
        else:
            # 添加行到当前单元格
            current_cell.append(line)
    
    # 处理最后一个Markdown单元格
    if current_cell:
        md_content = '\n'.join(current_cell)
        if md_content.strip():
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
