# 【核心】AI 大脑文件夹:
#SYSTEM_PROFILE.md       # 1. 团队/个人偏好 (Team/Personal Context)
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
