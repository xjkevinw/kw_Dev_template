# Project Context  (项目核心说明书，请根据实际项目修改)

## 1. 项目简介
*(在此处填写项目的一句话描述，例如：这是一个基于 Next.js 的电商后台管理系统)*

## 2. 核心业务实体 (Domain Entities)
*(在此处列出核心数据模型及其关系)*
- **User**: 系统用户，包含角色 (Admin/Customer)。
- **Order**: 订单，关联 User 和 Products。
- **Product**: 商品信息。

## 3. 关键业务规则 (Business Rules)
- 未登录用户无法访问 `/dashboard` 开头的路由。
- 软删除策略：所有数据删除操作均仅更新 `deletedAt` 字段，不物理删除。
