#!/bin/bash
# 用法: ./scripts/load_context.sh TASKS/001_xxx.md

# 获取脚本所在的目录 (.ai_context/scripts/)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# 获取父目录 (.ai_context/)
BASE_DIR="$(dirname "$SCRIPT_DIR")"
TASK_FILE="$1"

if [ -z "$TASK_FILE" ]; then
  echo "Usage: $0 <task_markdown_file>"
  exit 1
fi

echo "--- Loading Context ---"
echo ">>> SYSTEM PROFILE"
cat "$BASE_DIR/SYSTEM_PROFILE.md"
echo -e "\n\n>>> PROJECT CONTEXT"
cat "$BASE_DIR/PROJECT_CONTEXT.md"
echo -e "\n\n>>> ARCHITECTURE"
cat "$BASE_DIR/ARCHITECTURE.md"

echo -e "\n\n>>> CURRENT TASK"
if [ -f "$BASE_DIR/$TASK_FILE" ]; then
    cat "$BASE_DIR/$TASK_FILE"
else
    echo "Error: Task file '$BASE_DIR/$TASK_FILE' not found."
    exit 1
fi
