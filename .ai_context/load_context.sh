#Mac/Linux 辅助脚本，需 chmod +x

#!/bin/bash
# 用法: ./load_context.sh TASKS/001_xxx.md

BASE_DIR="$(dirname "$0")"
TASK_FILE="$1"

if [ -z "$TASK_FILE" ]; then
  echo "Usage: $0 <task_markdown_file>"
  exit 1
fi

echo "--- Loading Context for Claude Code ---"
echo ">>> SYSTEM PROFILE"
cat "$BASE_DIR/SYSTEM_PROFILE.md"
echo -e "\n\n>>> PROJECT CONTEXT"
cat "$BASE_DIR/PROJECT_CONTEXT.md"
echo -e "\n\n>>> ARCHITECTURE"
cat "$BASE_DIR/ARCHITECTURE.md"
echo -e "\n\n>>> CURRENT TASK"
cat "$BASE_DIR/$TASK_FILE"

# Mac 用户取消下面注释可直接复制到剪贴板
# | pbcopy
# echo "Done! Context copied to clipboard."
