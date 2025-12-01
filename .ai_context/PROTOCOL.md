# Claude Code 协作协议 (The "Context-First" Protocol)

> **核心原则 (Core Principles)**
> 1. **Git 即记忆 (Git is Memory)**: AI 的上下文窗口是短暂的，Markdown 文档是永恒的。所有重要的上下文必须沉淀为文件。
> 2. **谋定而后动 (Plan before Code)**: 禁止在没有更新任务文档 (`TASKS/*.md`) 的情况下直接编写代码。
> 3. **文档驱动变更 (Docs Drive Changes)**: 需求变更时，先改 Markdown，重启会话，再改代码。

---

## 1. 目录结构标准 (Directory Structure)

所有 AI 相关上下文必须存放于 `.ai_context/` 目录，且**必须提交到 Git**。

- `SYSTEM_PROFILE.md`: 定义 AI 行为、语言偏好、Linter 规则。
- `PROJECT_CONTEXT.md`: 项目业务背景、关键逻辑实体。
- `ARCHITECTURE.md`: 技术栈硬性约束、架构决策记录。
- `TASKS/`: **[动态]** 任务执行文档（中间产物），每次开发新功能时创建。
- `DECISIONS/`: **[归档]** 重大技术决策记录 (ADR)。

---

## 2. 上下文加载顺序 (Context Loading Order)

每次开启新会话（New Session）或执行 `/clear` 后，必须按以下顺序加载：

**推荐方式 (脚本一键加载):**
运行: `./.ai_context/scripts/load_context.sh TASKS/xxx_current_task.md`

**手动加载顺序:**
1. `/read .ai_context/SYSTEM_PROFILE.md`
2. `/read .ai_context/PROJECT_CONTEXT.md`
3. `/read .ai_context/ARCHITECTURE.md`
4. `/read .ai_context/TASKS/xxx_current_task.md`

---

## 3. 标准工作流 (The Protocol Loop)

### 🔄 阶段 I: 启动 (Init)
1. **新建任务**: 复制 `TASKS/template.md` 创建新文件 `TASKS/00X_task_name.md`。
2. **填充草稿**: 填写任务的 `背景` 和 `目标`。
3. **加载上下文**: 运行加载脚本。

### 📅 阶段 II: 规划 (Plan)
1. **指令**: *"请阅读当前任务文档，完善 '分析与计划' 和 '具体实施细节' 章节。不要写代码。" (Use Shift+Tab)*
2. **人工审查**: 检查 Markdown。如果不满意，**直接修改 Markdown 文件**并保存。

### 💻 阶段 III: 执行 (Execute)
1. **指令**: *"计划已确认，请开始执行 Step 1..."*
2. **循环**: 编码 -> 测试 -> Review -> 提交。
3. **维护**: 每 10-15 轮对话执行 `/compact`。如果混乱则 `/clear` 并重新加载。

### 🛠️ 阶段 IV: 修正与迭代 (Refine) - **核心步骤**
> **⚠️ 关键规则**: 需求变更或修 Bug 时：

1. **停止对话 (Stop)**: 不要试图在旧会话中修补。
2. **更新文档 (Doc)**: 在任务文件的 `## 4. 修正与迭代记录` 章节描述新需求。
3. **重启 (Reset)**: `/clear` -> 运行加载脚本。
4. **指令 (Prompt)**: *"请阅读文档底部的修正记录，对代码进行调整。"*

### ✅ 阶段 V: 结项 (Finalize)
1. **总结**: 填写 `## 5. 任务结项总结`。
2. **归档**: 运行 `python3 .ai_context/scripts/generate_summary.py` 更新概览，然后提交 Git。
