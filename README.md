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
└── .gitignore                  # 确保 .ai_context 被提交到仓库 
</pre>

📝 2. 核心模板 (Templates)
模板 A：团队/个人偏好 (SYSTEM_PROFILE.md)
这个文件定义了 AI 的“人设”和基本交互规则。


# AI Interaction Guidelines

## 1. 语言与沟通
- **思考与回复**：请使用**中文**进行解释和沟通。
- **代码与注释**：所有代码变量命名、Git Commit Message、代码注释必须使用**英文**。
- **风格**：保持专业、简洁。不要过度客套。

## 2. 编码规范 (Coding Standards)
- **命名**：使用驼峰命名法 (camelCase) 用于变量，帕斯卡命名法 (PascalCase) 用于类。
- **错误处理**：严禁吞掉错误 (swallowing errors)，必须有明确的 logging。
- **测试**：新功能必须包含对应的 Unit Test。

## 3. 工作流限制
- **小步提交**：生成的代码变动不应超过 200 行，完成后请提示我进行 Review。
- **禁止假定**：如果遇到模糊的需求，请先提问，不要自行假设。
模板 B：项目核心上下文 (PROJECT_CONTEXT.md)
这是项目的“说明书”，必须随着项目迭代及时更新。

# Project Context

## 1. 项目简介
这是一个基于 Next.js + Supabase 的电商管理后台。
核心目标：提供极简的库存管理和订单处理功能。

## 2. 关键目录结构
- `/src/app`: App Router 路由定义
- `/src/lib`: 数据库连接与通用工具函数
- `/src/components/ui`: ShadcnUI 基础组件

## 3. 技术栈决策
- ORM: Prisma
- State Management: Zustand
- Styling: TailwindCSS

## 4. 业务规则 (Business Rules)
- 用户必须登录才能访问 `/dashboard`。
- 订单状态流转：Pending -> Paid -> Shipped -> Completed。
- **[重要]**：删除数据必须使用软删除 (Soft Delete)，字段为 `deletedAt`。
模板 C：任务规划文档 (TASKS/00X_task_name.md)
这是视频中提到的“最重要的中间产物”。每次开发新功能或优化时，先写这个文件，再写代码。


# Task: [002] 优化首页加载速度

## 1. 背景与目标
当前首页加载时间超过 3秒，主要原因是同时加载了所有商品图片。
**目标**：将 LCP (Largest Contentful Paint) 降低到 1.2秒以内。

## 2. 分析与计划 (Analysis & Plan)
- [ ] **Step 1**: 分析当前 API `/api/products` 的响应时间。
- [ ] **Step 2**: 引入 Redis 缓存热点数据。
- [ ] **Step 3**: 前端图片实现 Lazy Loading 和 CDN 优化。

## 3. 具体实施细节 (由 AI 协助补充)
*(在此处使用 Claude Code 的 Shift+Tab 模式，让 AI 填入具体的实施思路，确认无误后再开始编码)*
- Redis Key 设计: `products:list:page_{n}`
- 缓存失效策略: TTL 60秒 + 更新商品时主动清除。

## 4. 验证标准 (Validation)
- 运行 Lighthouse 跑分，Performance > 90。
- 确保缓存一致性，修改商品价格后，首页应即时（或1分钟内）更新。
🔄 3. 工作流协议 (The Protocol)
阶段一：启动与规划 (Start & Plan)
创建任务文件：复制 template_task.md，新建 TASKS/003_feature.md。

加载上下文：在 Claude Code 终端中输入：
  <code>
    Bash
    
    /read .ai_context/SYSTEM_PROFILE.md <br>
    /read .ai_context/PROJECT_CONTEXT.md <br>
    /read .ai_context/TASKS/003_feature.md <br>
  </code>

谋定而后动 (Planning)：

告诉 Claude：“请阅读上述任务文档，帮我完善‘具体实施细节’部分，不要写代码，只分析方案。”

Review：你检查 AI 补充的细节。如果方案有误，直接修改 Markdown 文件，再次喂给 AI。

阶段二：执行与迭代 (Execute & Iterate)
按步骤执行：

指令：“按照任务文档 Step 1 的计划，开始编写代码。”

小步提交：

AI 完成一小部分后，运行测试。

人工 Review。

Git Commit：“feat: implement redis caching (Step 1 of Task 003)”。

上下文清洗 (Context Management)：

如果对话过长（例如超过 15 轮），执行 /compact 或 /clear。

关键点：由于你有 TASKS/003_feature.md 这个“外挂内存”，即使 Clear 之后，你只需要重新 /read 这个任务文件，AI 就能立刻知道进度到了哪里，无需重头解释。

阶段三：追加更改与优化 (Optimization & Changes)
这是用户最关心的部分：如何处理后续变动？

场景：功能做完了，但发现 Redis 缓存策略有问题，需要修改。

不要在原对话中纠缠：不要在混乱的旧上下文中修修补补。

更新任务文档：

打开 TASKS/003_feature.md。

在底部追加一个章节：

## 5. 修正与优化 (2025-08-24)
**问题**：TTL 60秒太长，导致库存不同步。
**修正方案**：改为“写入时更新缓存(Write-through)”策略。

重启会话：
  <code>
    /clear 清空上下文。
    /read .ai_context/TASKS/003_feature.md。
  </code>
  
指令：“请阅读文档第 5 部分‘修正与优化’，帮我重构缓存逻辑。”

阶段四：收尾与归档 (Finalize)
更新全局上下文：如果这次任务引入了新的技术（如 Redis），必须更新 PROJECT_CONTEXT.md 中的“技术栈决策”部分。

归档：将任务标记为已完成。这些文档保留在 Git 历史中，成为了项目最好的开发日志。

💡 为什么要这样做？
对抗 AI 的遗忘：AI 记不住 100 轮之前的对话，但它永远能读懂最新的 Markdown 文档。

Git 历史即文档：你的思考过程、决策变更都记录在 Markdown 里并被 Commit 了。三个月后你（或新同事）接手，看一眼 TASKS 文件夹就知道当初为什么这么写。

无痛切换 Session：随时可以 /clear 甚至关机睡觉。第二天早上，/read 一下文档，满血复活。
