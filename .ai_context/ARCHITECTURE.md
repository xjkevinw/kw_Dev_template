# 3. 架构与技术栈细节 (可合并入 Project Context)

# Architecture & Tech Stack Guidelines

## 1. 技术栈清单 (Tech Stack & Versions)
*请严格遵守以下版本和库的选择，不要引入未授权的库。*

- **Frontend Framework**: Next.js 14 (App Router)
- **Language**: TypeScript 5.x (Strict Mode enabled)
- **Styling**: Tailwind CSS 3.4 (使用 `clsx` 和 `tailwind-merge` 处理类名合并)
- **State Management**: Zustand (用于全局状态), React Query (用于服务端数据)
- **Database/ORM**: PostgreSQL via Prisma 5.x
- **Auth**: NextAuth.js v5 (Beta)

## 2. 核心架构模式 (Core Patterns)

### 2.1 数据流向 (Data Flow)
* **Server Component**: 负责直接获取数据 (Direct DB access) 并通过 Props 传递给 Client Component。
* **Client Component**: 负责交互。所有数据变更 (Mutation) 必须通过 Server Actions 触发，严禁在客户端直接调用 API Route (除非是流式响应)。

### 2.2 目录组织逻辑 (Directory Philosophy)
* `src/app`: 仅存放路由页面 (`page.tsx`) 和布局 (`layout.tsx`)。不要在这里写复杂的业务逻辑组件。
* `src/components/features`: 按业务功能划分组件 (例如 `auth`, `cart`, `dashboard`)。
* `src/components/ui`: 纯展示型原子组件 (Buttons, Inputs)，通常来自 ShadcnUI，不包含业务逻辑。
* `src/server/actions`: 所有的 Server Actions 必须放在这里，且必须包含 Zod 输入验证。

## 3. 编码规范约束 (Coding Constraints)

* **Error Handling**: Server Actions 必须返回 `{ success: boolean, message: string, data?: any }` 的标准格式，前端据此显示 Toast。
* **Types**: 禁止使用 `any`。所有的数据库模型类型必须从 `@prisma/client` 导入。
* **Performance**: 所有重型组件 (Charts, Maps) 必须使用 `next/dynamic` 进行懒加载。

## 4. 关键决策记录 (Architecture Decision Records - ADR)
* *2025-08-01*: 决定放弃 Redux，改用 Zustand，因为项目复杂度无需 Redux。
* *2025-08-15*: 图片上传均代理到 AWS S3，不存储在本地服务器。
