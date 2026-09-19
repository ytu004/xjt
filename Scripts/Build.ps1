[CmdletBinding()]
param(
    [string]$EngineRoot,
    [ValidateSet('XJTEditor', 'XJT')]
    [string]$Target = 'XJTEditor',
    [ValidateSet('Development', 'DebugGame', 'Shipping')]
    [string]$Configuration = 'Development'
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$projectFile = Join-Path $projectRoot 'XJT.uproject'
$project = Get-Content -LiteralPath $projectFile -Raw | ConvertFrom-Json

if ($Target -eq 'XJTEditor' -and $Configuration -eq 'Shipping') {
    throw 'Shipping is available only for the XJT game target.'
}
if (-not $EngineRoot) {
    $installManifest = Join-Path $env:ProgramData 'Epic/UnrealEngineLauncher/LauncherInstalled.dat'
    if (Test-Path -LiteralPath $installManifest) {
        $installs = Get-Content -LiteralPath $installManifest -Raw | ConvertFrom-Json
        $engineInstall = $installs.InstallationList |
            Where-Object { $_.AppName -eq "UE_$($project.EngineAssociation)" } |
            Select-Object -First 1
        if ($engineInstall) { $EngineRoot = $engineInstall.InstallLocation }
    }
}
if (-not $EngineRoot) {
    throw 'Engine installation not found. Pass -EngineRoot with your UE 5.8.2 directory.'
}
$engineVersion = Get-Content -LiteralPath (Join-Path $EngineRoot 'Engine/Build/Build.version') -Raw |
    ConvertFrom-Json
if ($engineVersion.MajorVersion -ne 5 -or $engineVersion.MinorVersion -ne 8 -or $engineVersion.PatchVersion -ne 2) {
    throw 'This project uses UE 5.8.2. Pass the matching -EngineRoot.'
}
$buildTool = Join-Path $EngineRoot 'Engine/Build/BatchFiles/Build.bat'
if (-not (Test-Path -LiteralPath $buildTool)) { throw "Build tool not found: $buildTool" }

& $buildTool $Target Win64 $Configuration $projectFile -WaitMutex -NoHotReloadFromIDE
if ($LASTEXITCODE -ne 0) { throw "Unreal build failed with exit code $LASTEXITCODE." }
