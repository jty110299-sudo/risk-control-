# Risk Control Agent v2.0 Design System

## 1. Product Direction

Risk Control Agent should feel like a product-grade analyst workbench: upload data, configure a target, train a risk model, generate `risk_score`, review risk bands, inspect attribution, receive rule-based recommendations, and write a report.

The UI is inspired by Apple-like minimal dashboard principles: clean surfaces, strong hierarchy, generous whitespace, and content-first interaction. It does not use Apple trademarks, brand assets, official fonts, images, or icons.

## 2. Visual Theme

1. Light background.
2. Large, clear page titles with concise subtitles.
3. Rounded cards with soft shadows.
4. Each page focuses on one primary user task.
5. Avoid project phase/status clutter in the main UI.
6. Avoid dense raw tables unless the user explicitly needs detail.
7. Avoid cyber, glowing, or large-screen command-center styling.

## 3. Color Tokens

| Token | Color | Usage |
| --- | --- | --- |
| `background` | `#F5F5F7` | App background. |
| `surface` | `#FFFFFF` | Primary card and panel surface. |
| `surface_soft` | `#FBFBFD` | Secondary card surface. |
| `text_primary` | `#1D1D1F` | Main titles and values. |
| `text_secondary` | `#6E6E73` | Body text and captions. |
| `accent_blue` | `#0071E3` | Primary action and links. |
| `border` | `#D2D2D7` | Dividers and subtle card borders. |
| `success` | `#34C759` | Completed or normal states. |
| `warning` | `#FF9F0A` | Needs attention. |
| `danger` | `#FF3B30` | High-risk or blocked state. |
| `purple` | `#AF52DE` | Attribution / insight accent. |

## 4. Typography

Use system fonts only:

```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC", sans-serif;
```

Large titles should be clear and sparse. Metric values should be bold and easy to scan. Tables should remain readable and not too small.

## 5. Navigation

Left navigation uses functional groups, not generic "navigation" labels:

Risk Control Agent

风险工作台

* 主控台
* 数据接入
* 风险评估

分析中心

* 数据可视化
* 归因分析
* 智能建议

交付中心

* 报告撰写
* 运行审计

系统

* 设置

## 6. Components

1. Hero header: one clear task-oriented title and a concise explanation.
2. Summary card: one label, one value, one supporting line.
3. Workflow step: compact status showing 未开始 / 可运行 / 已完成 / 需要检查.
4. Upload panel: simple instructions, file uploader, field mapping.
5. Chart panel: card-wrapped plot, never a random chart.
6. Insight panel: reason codes and segment contribution with explicit investigation boundary.
7. Recommendation card: severity badge, recommendation text, Human Confirmation flag.
8. Report preview: clean Markdown/HTML preview in a card.
9. Audit table: compact action log without raw sensitive data.

## 7. Interaction Rules

1. Data upload must be obvious.
2. Supervised model training requires a valid target label.
3. If no target and no score exist, only exploratory analysis is allowed.
4. Do not fabricate target, score, chart, metric, model result, or attribution.
5. Smart recommendations are rule-based and must not execute business actions.
6. High-risk recommendations require Human Confirmation.
7. Report generation should explain missing prerequisites instead of producing empty filler.

## 8. Do / Don't

Do:

* Use Chinese-first labels.
* Use simple cards and concise copy.
* Make the next step clear.
* Keep high-risk and Human Confirmation states visible.
* Keep uploaded data ignored by Git.

Don't:

* Do not show phase completion as primary UI content.
* Do not expose CHANGELOG or project logs as main product pages.
* Do not invent charts for visual appeal.
* Do not add auto reject, auto limit adjustment, auto channel closure, or policy modification actions.
* Do not claim production readiness.

## 9. Agent Prompt Guide

When modifying the UI, follow this file first. If a new interaction pattern is needed, update `DESIGN.md` before implementing it. Keep the interface minimal, task-oriented, and Chinese-first.
