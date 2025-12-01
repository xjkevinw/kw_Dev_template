#!/usr/bin/env python3
import os
import glob
import re
from datetime import datetime

# 配置路径: 向上找两级 (.ai_context/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS_DIR = os.path.join(BASE_DIR, "TASKS")
OUTPUT_FILE = os.path.join(BASE_DIR, "SUMMARY.md")
TEMPLATE_FILE = "template.md"

def parse_task_file(filepath):
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    title_match = re.search(r'^# Task:\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filename
    
    status_match = re.search(r'^>\s*(?:状态|Status):\s*(.+)$', content, re.MULTILINE)
    status = status_match.group(1).strip() if status_match else "Unknown"

    mtime = os.path.getmtime(filepath)
    mod_date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

    return {"filename": filename, "title": title, "status": status, "date": mod_date}

def generate_markdown(tasks):
    lines = []
    lines.append("# 📊 Project Task Summary")
    lines.append(f"> Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append("| ID/File | Task Description | Status | Last Modified |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for t in tasks:
        link = f"[{t['filename']}](./TASKS/{t['filename']})"
        lines.append(f"| {link} | {t['title']} | {t['status']} | {t['date']} |")
    return "\n".join(lines)

def main():
    if not os.path.exists(TASKS_DIR):
        print("No TASKS directory found.")
        return
    files = glob.glob(os.path.join(TASKS_DIR, "*.md"))
    tasks = []
    for f in files:
        if os.path.basename(f) == TEMPLATE_FILE: continue
        res = parse_task_file(f)
        if res: tasks.append(res)
    
    tasks.sort(key=lambda x: x['filename'], reverse=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(generate_markdown(tasks[:15]))
    print(f"✅ Summary generated at: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
