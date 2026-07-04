# GitHub Upload Guide

## 上传前检查

上传前请先运行：

```bash
python scripts/project_health_check.py
python -m pytest
```

## 不要上传大型数据文件

不要上传 `data/raw/` 下的大型官方原始数据，不要上传真实个人金融数据，不要上传未经人工确认的 derived outputs。

## 检查 `.gitignore`

确认 `.gitignore` 忽略：

* `data/raw/*`
* `data/processed/*`
* `*.zip`
* `*.parquet`
* `*.db`
* `*.pkl`

## 检查文档

上传前检查：

* `README.md`
* `SOURCES.md`
* `PROJECT_LOG.md`
* `CHANGELOG.md`
* `PROJECT_SUMMARY.md`
* `docs/release/pre_release_checklist.md`
* `docs/release/data_safety_checklist.md`

## 检查 requirements

确认 `requirements.txt` 和 `requirements-dev.txt` 可安装项目运行与测试依赖。

## 检查 outputs

检查 `outputs/alerts/` 和 `outputs/reports/` 是否包含伪造结果。没有真实输入时，不应提交伪造 alert 或 report。

## 建议的 Git 操作命令

以下命令仅供用户手动执行，Codex 不应自动执行 Git 操作。

```bash
git init
git status
git add .
git commit -m "Initial release of Risk Control Agent"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```
