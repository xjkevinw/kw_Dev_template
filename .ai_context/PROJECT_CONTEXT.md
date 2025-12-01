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
