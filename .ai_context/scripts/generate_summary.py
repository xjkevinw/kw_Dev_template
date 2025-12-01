#!/usr/bin/env python3
import os
import glob
import re
from datetime import datetime

# 配置路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # .ai_context/
TASKS_DIR = os.path.join(BASE_DIR, "TASKS")
OUTPUT_FILE = os.path.join(BASE_DIR, "SUMMARY.md")
TEMPLATE_FILE = "template.md"

def parse_task_file(filepath):
    """解析任务文件，提取标题、状态和日期"""
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取标题 (匹配 # Task: [ID] Title)
    title_match = re.search(r'^# Task:\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filename

    # 提取状态 (匹配 > 状态: [Status])
    status_match = re.search(r'^>\s*(?:状态|Status):\s*(.+)$', content, re.MULTILINE)
    status = status_match.group(1).strip() if status_match else "Unknown"

    # 获取文件最后修改时间
    mtime = os.path.getmtime(filepath)
    mod_date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

    return {
        "filename": filename,
        "title": title,
        "status": status,
        "date": mod_date,
        "raw_mtime": mtime
    }

def generate_markdown(tasks):
    """生成 Markdown 表格"""
    lines = []
    lines.append("# 📊 Project Task Summary")
    lines.append(f"> Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    lines.append("| ID/File | Task Description | Status | Last Modified |")
    lines.append("| :--- | :--- | :--- | :--- |")
    
    for t in tasks:
        # 清理文件名中的 .md 后缀，做成链接
        link = f"[{t['filename']}](./TASKS/{t['filename']})"
        lines.append(f"| {link} | {t['title']} | {t['status']} | {t['date']} |")
    
    return "\n".join(lines)

def main():
    # 1. 获取所有 .md 文件
    files = glob.glob(os.path.join(TASKS_DIR, "*.md"))
    
    tasks = []
    for f in files:
        if os.path.basename(f) == TEMPLATE_FILE:
            continue
        tasks.append(parse_task_file(f))
    
    # 2. 排序：按文件名倒序 (003 -> 002)，或者按修改时间 raw_mtime
    # 这里默认按文件名倒序，这样最新的任务 ID 排在前面
    tasks.sort(key=lambda x: x['filename'], reverse=True)
    
    # 3. 取最近 10 个
    recent_tasks = tasks[:10]
    
    # 4. 写入 SUMMARY.md
    content = generate_markdown(recent_tasks)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Summary generated at: {OUTPUT_FILE}")
    print(f"   Total tasks: {len(tasks)}, Showing top: {len(recent_tasks)}")

if __name__ == "__main__":
    main()
