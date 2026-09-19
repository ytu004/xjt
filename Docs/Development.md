# C++ 开发约定

项目由 AI 持续开发，以 C++ 为核心逻辑的实现入口。蓝图及其他二进制资源用于配置、场景和视听表现，避免把关键规则藏在事件图中。AI 负责代码、构建、资源脚本和可执行的验证；设计效果仍需要实际试玩，编译成功不代表体验正确。

## 代码与资源分工

- C++：角色与输入、检查点与重试、干扰调度、媒介对象状态、行为记录、meta 条件、存档、UI 状态及可测试的规则。
- 编辑器与资源：关卡布局、材质、贴图、音频、动画、Widget 布局和原生类的参数实例。
- 数据：简单可调规则优先使用配置或可读表格源；需要资产引用时使用 DataAsset/DataTable，保留 UE 正常资源工作流。
- Python 编辑器脚本：创建、检查和批量维护资源，不承载运行时玩法。禁止手工拼接或直接修改 .uasset/.umap 的二进制内容。
- UPROPERTY 与 UFUNCTION 暴露必要的调参和展示接口；同一规则不在 C++ 与蓝图中维护两份实现。
- 模块只加入实际使用的依赖；EnhancedInput、Paper2D、UMG 等在对应代码加入时声明。

## 构建与打开

使用 UE 5.8.2 和兼容的 MSVC C++ 工具链及 Windows SDK。在项目根目录运行：

```powershell
./Scripts/Build.ps1
# 非 Launcher 安装可显式传入：
./Scripts/Build.ps1 -EngineRoot 'D:/EPIC/UE_5.8'
# 需要验证游戏目标时：
./Scripts/Build.ps1 -Target XJT
```

构建成功后双击 XJT.uproject。脚本默认构建 Development Editor，不依赖提交到 Git 的 .sln。游戏目标编译不等于完成 Cook/打包，正式交付需另做资源烘焙和打包验证。

新增或修改反射头文件、模块、构造函数时，关闭本项目编辑器，执行完整构建后再打开；不要把 Live Coding 作为此类变更的唯一验收。不要自动关闭其他项目或用户未保存的编辑器。

## 开发与验证顺序

每次以一个可审阅功能为单位：实现原生逻辑，编译并处理 UHT 错误，验证资产引用和原生类加载，最后在编辑器运行与本次变化相关的场景。

为状态转换、事件顺序、暂停恢复、死亡复位和存档迁移编写有意义的自动化检查。手感、阅读负担和 meta 表达仍需实际试玩；不为简单声明写与实现互相抄写的测试。

构建日志、生成代码、Binaries、Intermediate、Saved、DerivedDataCache 和 IDE 项目文件不提交。Source、Config、Content、构建脚本和必要项目文档必须提交；资源继续使用 Git LFS。

## 当前基础

原生运行时模块为 XJT，提供 XJT 与 XJTEditor 构建目标。默认 GameMode 为 AXJTGameModeBase。它目前只继承引擎基础行为，不代表侧视角色、输入、跳跃、干扰或 meta 系统已经完成。
