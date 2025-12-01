# dw_Dev_template

这套方案的核心在于：通过文件管理思维，将 AI 的“短期记忆”固化为 Git 仓库中的“长期记忆”，从而实现高质量的后续迭代和维护。

📂 1. 目录结构设计 (Git Repository Structure)
建议在项目根目录下创建一个专门的文件夹（如 .ai_context 或 docs/ai），用于存放所有 AI 相关的上下文文档。

<pre>
my-project/
├── .ai_context/                # 【核心】AI 大脑文件夹
│   ├── SYSTEM_PROFILE.md       # 1. 团队/个人偏好 (Team/Personal Context)
│   ├── PROJECT_CONTEXT.md      # 2. 项目核心上下文 (Project Context)
│   ├── ARCHITECTURE.md         # 3. 架构与技术栈细节 (可合并入 Project Context)
│   └── TASKS/                  # 4. 中间任务文档 (Intermediate Docs)
│       ├── 001_auth_setup.md
│       ├── 002_optimize_db_query.md
│       └── template_task.md    # 任务模板
├── src/
├── ...
├──.gitignore                  # 确保 .ai_context 被提交到仓库 
├── SUMMARY.md                # [自动生成] 项目仪表盘
└── scripts/                  # 建议建个 scripts 文件夹整理脚本
    ├── generate_summary.py   # [新增] 生成概览的 Python 脚本
    └── load_context.sh       # [移动] 之前的一键加载脚本
</pre>


🚀 如何开始？
创建文件夹：在项目根目录执行 mkdir -p .ai_context/TASKS .ai_context/DECISIONS。

创建文件：将上述内容分别复制进去。

提交 Git：

Bash

git add .ai_context
git commit -m "chore: init ai context protocol based on context-first methodology"
开始第一个任务：

Bash

cp .ai_context/TASKS/template.md .ai_context/TASKS/001_init_project.md
# 编辑 001_init_project.md 填入你的需求
# 开始你的 Claude Code 之旅！
