Set-Location -Path (Split-Path -Parent $MyInvocation.MyCommand.Definition)

$weaponIds = Get-Content -Path weapon-ids
$weaponNames = Get-Content -Path weapon-names
$weaponUsed = Get-Content -Path weapon-used

$index = $weaponIds.IndexOf($weaponUsed)
$weaponName = $weaponNames[$index]
Write-Output $weaponName