dw_Dev_template

A lightweight, Git-based context engineering framework that gives AI coding agents persistent project memory across sessions.

中文版本 / Chinese version
Why This Exists
Modern AI coding agents — Claude Code, Cursor, GitHub Copilot, Aider, and others — are powerful, but they suffer from a fundamental limitation: their context is ephemeral. Every new session starts blank. The architectural decisions you explained yesterday, the coding conventions your team agreed on last month, the reason you chose Postgres over MongoDB — all of it has to be re-explained, re-discovered, or simply lost.
The result: inconsistent code, repeated mistakes, drifting architecture, and hours wasted re-establishing context every time you (or a teammate) start a new AI-assisted session.
dw_Dev_template solves this with a simple idea: treat AI context the same way we treat code — as a first-class artifact that lives in the Git repository, gets reviewed, gets versioned, and gets shared across the team.
By converting the AI's short-term session memory into long-term, version-controlled markdown documents, this framework enables:

✅ Consistent AI behavior across sessions, machines, and teammates
✅ Onboarding-friendly projects — both humans and AI agents come up to speed in minutes, not hours
✅ Auditable AI-assisted development — every architectural decision and task is documented
✅ Higher-quality iteration — the AI builds on prior decisions instead of contradicting them

Repository Structure
my-project/
├── .ai_context/                # The AI "brain" folder
│   ├── SYSTEM_PROFILE.md       # Team / personal preferences (coding style, tooling)
│   ├── PROJECT_CONTEXT.md      # Project goals, scope, constraints
│   ├── ARCHITECTURE.md         # Tech stack and architectural decisions
│   └── TASKS/                  # Per-task working documents
│       ├── 001_auth_setup.md
│       ├── 002_optimize_db_query.md
│       └── template_task.md    # Reusable task template
├── src/
│   └── ...                     # Your actual project code
├── scripts/
│   ├── generate_summary.py     # Auto-generates SUMMARY.md project dashboard
│   └── load_context.sh         # One-command context loader for AI agents
├── SUMMARY.md                  # [Auto-generated] Project dashboard
└── .gitignore                  # Ensures .ai_context IS committed to the repo
What each file does
FilePurposeSYSTEM_PROFILE.mdYour personal or team preferences: preferred languages, coding style, tooling choices, communication style. Rarely changes.PROJECT_CONTEXT.mdWhat this project is: goals, scope, target users, key constraints. Changes when the project pivots.ARCHITECTURE.mdHow this project is built: tech stack, key design decisions, trade-offs made. Updated as architecture evolves.TASKS/NNN_*.mdOne file per task or feature. Captures requirements, decisions, and outcomes for that specific work.SUMMARY.mdA consolidated dashboard auto-generated from the above. The "single-paste" briefing you give to any new AI session.
Quick Start
1. Initialize the structure
bashmkdir -p .ai_context/TASKS .ai_context/DECISIONS
Copy the template files from this repo into your .ai_context/ folder.
2. Commit to Git
bashgit add .ai_context
git commit -m "chore: init ai context protocol based on context-first methodology"
3. Start your first task
bashcp .ai_context/TASKS/template_task.md .ai_context/TASKS/001_init_project.md
# Edit 001_init_project.md to describe what you want to build
4. Begin your AI-assisted session
Load the context with the helper script:
bash./scripts/load_context.sh
Or paste the contents of SUMMARY.md into your AI agent's first message. The agent now has full project context — start coding.
Example: A Populated PROJECT_CONTEXT.md
markdown# Project Context

## What we're building
A FastAPI service that ingests clinical notes and returns structured
ICD-10 codes using a fine-tuned LLM.

## Why
Manual coding takes ~15 minutes per note. We need <30 seconds with >92% accuracy.

## Constraints
- HIPAA compliance required — no patient data leaves our VPC
- Latency budget: p95 < 2 seconds
- Must run on existing GCP infrastructure

## Out of scope
- ICD-11 (project deferred until 2027)
- Real-time streaming (batch is acceptable)
When an AI agent reads this before writing any code, the quality and relevance of its output improves dramatically — no more "let me suggest a generic FastAPI scaffold" responses.
Philosophy
This project is built on three principles:

Context is code. It deserves the same rigor — versioning, review, reuse.
Documentation written for AI is better documentation for humans too. Forcing clarity for an LLM forces clarity, period.
The best AI workflow is one a teammate can pick up tomorrow. No magic prompts, no hidden state — everything lives in the repo.

Roadmap

 CLI tool to scaffold the .ai_context/ structure in any repo
 Auto-extraction of decisions from PR descriptions into DECISIONS/
 Integration examples for Claude Code, Cursor, and Aider
 VS Code extension for one-click context loading

Contributing
Contributions, suggestions, and battle-tested workflow improvements are welcome. Open an issue or PR.
License
MIT

Suggested GitHub topics for this repo: ai-agents, claude-code, cursor, context-engineering, developer-tools, llm, prompt-engineering, ai-workflow, documentation-as-code
