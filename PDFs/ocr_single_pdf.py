#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单篇PDF文件OCR处理脚本
用于验证待验证论文的内容
"""

import fitz
import sys

def ocr_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += f"\n--- Page {page_num + 1} ---\n"
            text += page.get_text()
            text += "\n"
        
        pdf_document.close()
        
        return text
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None

def extract_title(text):
    """Extract title from text"""
    if not text:
        return "Unknown Title"
    
    lines = text.split('\n')
    title_lines = []
    
    for line in lines[:50]:
        line = line.strip()
        if line and not line.startswith('Page') and not line.startswith('---'):
            title_lines.append(line)
            if len(title_lines) >= 3:
                break
    
    if title_lines:
        return ' '.join(title_lines)
    else:
        return "Unknown Title"

def main():
    if len(sys.argv) != 2:
        print("Usage: python ocr_single_pdf.py <pdf_file>")
        return
    
    pdf_path = sys.argv[1]
    print(f"Processing PDF: {pdf_path}")
    
    text = ocr_pdf(pdf_path)
    
    if text:
        title = extract_title(text)
        print(f"\n=== Extracted Title ===")
        print(title)
        print(f"\n=== First 1000 characters of OCR result ===")
        print(text[:1000] + "...")
        
        # Save OCR result
        output_path = pdf_path.replace('.pdf', '_ocr.txt')
        with open(output_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(text)
        print(f"\nOCR result saved to: {output_path}")
    else:
        print("Failed to process PDF")

if __name__ == "__main__":
    main()
