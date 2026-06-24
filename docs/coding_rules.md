# 项目开发规范

## 文档用途

本文档用于保持 Unity、Python、文档与 Git 记录一致。规则以“容易理解、容易维护、适合作品集展示”为优先目标。

## C# 代码规范

- 类名、方法名使用 `PascalCase`，例如 `PlayerController`
- 私有字段使用 `camelCase`，例如 `moveSpeed`
- 布尔变量使用清晰的是非含义，例如 `isHidden`、`hasKey`
- 一个脚本优先只负责一类功能
- 避免把移动、攻击、交互、存档全部写进同一个 Player 脚本
- Inspector 中需要配置的私有字段使用 `[SerializeField]`
- 复杂判断拆成名称清晰的小方法
- 只有必要时添加注释，注释说明“为什么”，而不是重复代码

推荐职责拆分：

```text
PlayerMovement      负责移动
PlayerCombat        负责攻击与受伤
PlayerInteraction   负责与门、物品、NPC 交互
PlayerState         负责钥匙、任务与其他玩家状态
```

## Python 代码规范

- 文件和变量使用小写加下划线，例如 `npc_service.py`
- 函数名称表达具体动作，例如 `build_npc_prompt`
- API 路由、模型调用和数据存储尽量分开
- API Key 必须放在环境变量中，不能写进代码或提交到 Git
- AI 返回的数据必须经过验证后才能交给 Unity
- 初学阶段优先写清晰直接的代码，不为了“高级”而使用复杂语法

## 文件命名规范

| 类型 | 规范 | 示例 |
| --- | --- | --- |
| C# 脚本 | PascalCase | `NpcDialogueController.cs` |
| Python 文件 | snake_case | `npc_service.py` |
| Unity Scene | PascalCase | `CastleLevel01.unity` |
| Prefab | PascalCase | `GuardPrefab.prefab` |
| 文档 | snake_case | `game_design.md` |
| JSON 数据 | snake_case | `npc_data.json` |

避免使用：

- `New Folder`
- `test2_final`
- `未命名`
- 含义不清的缩写

## Prefab 规范

- 可重复使用的角色、敌人、交互物体必须制作成 Prefab
- Prefab 名称要能表达用途
- Prefab 内部层级保持简洁
- 修改共享 Prefab 前确认是否会影响所有实例
- 同类 Prefab 使用一致的组件结构
- AI NPC Prefab 不保存 API Key 或服务端秘密

建议目录：

```text
Assets/Prefabs/Player/
Assets/Prefabs/NPC/
Assets/Prefabs/Enemies/
Assets/Prefabs/Environment/
Assets/Prefabs/UI/
```

## Scene 规范

- Scene 按用途命名，不使用默认名称长期开发
- 每个 Scene 根节点保持清晰分组
- 测试功能使用独立测试 Scene，避免污染正式关卡
- AI NPC 接入初期建议使用单独的 `AINpcTest` Scene
- 正式场景修改前先确认可运行基线

建议根节点：

```text
Systems
Environment
Characters
Interactables
UI
Lighting
```

## Git 提交规范

提交信息使用清晰的动作描述：

```text
feat: add npc trust response
fix: prevent hidden route opening below trust threshold
docs: update ai npc interface design
refactor: split player movement from combat
```

提交原则：

- 一个提交完成一个明确目标
- 提交前运行项目或相关测试
- 不提交 API Key 和本地配置秘密
- 不提交 Unity 自动生成的大型临时目录
- 功能完成时同步更新 `docs/progress.md`
- 产生重要方案选择时同步更新 `docs/tech_decision.md`

## 文档维护规范

每次完成一个功能时：

1. 更新 `progress.md` 中的状态
2. 更新与功能直接相关的设计文档
3. 在 `tech_decision.md` 记录重要方案选择
4. 如果项目整体方向变化，更新 `project_context.md`
5. 文档内容以当前代码和可验证结果为准
