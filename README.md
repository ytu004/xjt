# XJT

基于“媒介即讯息”概念的 2D 平台跳跃项目。使用 Unreal Engine **5.8.2**，当前为蓝图项目基础，启用 Paper2D 和 Enhanced Input。

## 当前状态

已配置项目入口、初始灰盒关卡、资源目录、Git 忽略规则和 Git LFS。初始关卡仅有平台、出生点和灯光。角色移动、侧视相机、跳跃、死亡重生、闪白、广告入侵、平台漂移、弹幕推力及通关逻辑尚未实现；当前不是可玩 Demo。

## 本地打开

安装 UE 5.8.2，双击 `XJT.uproject`。编辑器启动时打开 `Content/XJT/Maps/L_Prototype.umap`。首次打开会生成本地缓存。团队统一引擎版本，避免资源被意外升级。

## 克隆和协作

先安装 Git 和 Git LFS，然后执行：

```powershell
git lfs install
git clone <仓库地址>
cd <仓库目录>
git lfs pull
```

`.uasset`、`.umap` 和常见美术/音视频资源使用 LFS。不要把 LFS 指针文件误当作实际资源；克隆后确保 `git lfs pull` 成功。蓝图与地图不适合文本合并，修改同一个资源前先与队友协调。

## 提交哪些文件

| 提交 | 不提交 |
| --- | --- |
| `.uproject`、`Config/`、`Content/` | `Saved/`、`Intermediate/`、`DerivedDataCache/` |
| 后续新增的 `Source/` 和项目插件 | 项目根目录 `Binaries/`、生成的 IDE 文件 |
| 必要的 `Build/` 配置及图标 | 本地日志、个人编辑器设置、凭据 |
| 文档、脚本、`.gitignore`、`.gitattributes` | UE 引擎安装目录、打包交付物 |

`Content/` 中的蓝图、地图、贴图等是必要文件，不能为了缩小仓库而省略。二进制专用插件可能必须包含其 `Binaries/`，因此没有全局忽略插件二进制目录。打包产物放在仓库外。

Git LFS 使用独立存储和带宽配额，添加大型素材前检查 GitHub 账户配额。引擎自带基础网格由本机 UE 提供，不复制进仓库。

## 资源约定

项目资源集中在 `Content/XJT/`，按 `Maps`、`Blueprints`、`Input`、`UI`、`Art`、`Audio` 分类。建议命名：`L_` 地图、`BP_` 蓝图、`WBP_` UI、`IA_` 输入动作、`IMC_` 输入映射、`T_` 贴图、`M_` 材质。

策划内容及首个开发阶段见 `Docs/ProjectPlan.md`。
