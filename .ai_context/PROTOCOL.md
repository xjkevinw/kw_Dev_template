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

1. `/read .ai_context/SYSTEM_PROFILE.md` (加载人设)
2. `/read .ai_context/PROJECT_CONTEXT.md` (加载业务)
3. `/read .ai_context/ARCHITECTURE.md` (加载技术约束)
4. `/read .ai_context/TASKS/xxx_current_task.md` (加载当前任务)

---

## 3. 标准工作流 (Standard Workflow)

### 阶段 I: 启动 (Init)
1. **新建任务**: 基于 `TASKS/template.md` 创建新文件 `TASKS/00X_brief_desc.md`。
2. **填充草稿**: 填写任务的 `背景` 和 `目标`。
3. **加载上下文**: 按上述顺序加载文件。

### 阶段 II: 规划 (Plan)
1. **指令**: *"请阅读当前任务文档，完善 '分析与计划' 和 '具体实施细节' 章节。不要写代码。" (配合 Shift+Tab 使用)*
2. **人工审查**: 检查 Markdown 中的计划。
   - *如果不满意*: **直接修改 Markdown 文件**，保存。
   - *如果满意*: 进入下一阶段。

### 阶段 III: 执行 (Execute)
1. **指令**: *"计划已确认，请开始执行 Step 1..."*
2. **循环**: 编码 -> 测试 -> Review -> 提交。
3. **上下文维护**:
   - 每 10-15 轮对话，执行 `/compact`。
   - 如果上下文混乱，执行 `/clear` 并重新加载文档。

### 阶段 IV: 修正与迭代 (Refine)
> **⚠️ 关键规则**: 当需要修改已完成的功能，或需求发生变更时：

1. **停止对话**: 不要试图在旧会话中修补。
2. **更新文档**: 在任务文件的 `## 4. 修正与迭代记录` 章节描述新需求。
3. **重启**: `/clear` -> 重新加载上述 4 个文件。
4. **指令**: *"请阅读文档底部的修正记录，对代码进行调整。" (Refine the code based on the new notes)*

### 阶段 V: 结项 (Finalize)
1. **总结**: 在任务文件中填写 `## 5. 任务结项总结`。
2. **全局更新**:
   - 如果引入了新库/新技术 -> 更新 `ARCHITECTURE.md`。
   - 如果改变了核心业务逻辑 -> 更新 `PROJECT_CONTEXT.md`。
3. **提交**: `git add .ai_context && git commit -m "docs: archive task 00X"`

---

## 4. 给 AI 的指令 (Instructions for AI Agent)

当读取到本文件时，请遵循以下元规则：
1. **Protocol Compliance**: 严格遵守 "Read Docs -> Plan -> Code" 的循环。
2. **拒绝无文档请求**: 如果用户让你做一个复杂的特性，但没有提供对应的 `TASKS/` 文档，请礼貌地提示用户先创建任务文档。
3. **保持原子性**: 每次代码生成的改动量尽量控制在 200 行以内。
