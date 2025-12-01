# dw_Dev_template

# 专门的文件夹（如 .ai_context 或 docs/ai），用于存放所有 AI 相关的上下文文档。

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
└── .gitignore                  # 确保 .ai_context 被提交到仓库

