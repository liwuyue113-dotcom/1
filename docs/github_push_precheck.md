# GitHub 推送前最小检查

## 文档用途

本文记录 2026-06-24 第一次本地提交之后，推送到 GitHub 之前需要确认的最小事项。

本阶段目标不是立刻推送，而是确认当前仓库是否具备推送条件，以及还缺什么信息。

## 当前 Git 状态

- 当前分支：`master`
- 第一次本地提交：`f9ea39e chore: initialize portfolio project workspace`
- 当前远程仓库：未配置
- 当前未跟踪文件：`tools/`

`tools/` 当前仍然不进入主项目提交范围，因为它主要是本地简历 PDF 生成工具，和《囚城营救》AI 游戏作品集主线关系较弱。后续如果要整理求职材料，可以单独建一个阶段处理。

## 推送前已确认

- 第一次本地提交已经完成。
- `.gitignore` 已覆盖 `.env`、虚拟环境、缓存、输出目录和 Unity 生成目录。
- 代码和文档主线已经进入 Git 历史。
- `tools/` 没有进入第一次提交。

## 还不能直接推送的原因

当前仓库没有配置 GitHub remote。

推送前至少需要确认：

1. GitHub 仓库地址。
2. 仓库是公开还是私有。
3. 是否继续使用当前 `master` 分支作为默认分支，或改成 `main`。

## 下一步最小动作

用户创建或提供 GitHub 仓库地址后，再执行：

```powershell
git remote add origin <GitHub 仓库地址>
git push -u origin master
```

如果用户希望默认分支使用 `main`，则先执行：

```powershell
git branch -M main
git push -u origin main
```

## 当前阶段边界

本阶段不创建 GitHub 仓库。

本阶段不推送代码。

本阶段不处理 `tools/`。

本阶段只确认本地仓库已经具备推送前的最低准备状态。
