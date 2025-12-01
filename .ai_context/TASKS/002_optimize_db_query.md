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
