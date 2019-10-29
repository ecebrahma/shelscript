$here = Split-Path -Parent $MyInvocation.MyCommand.Path

function Initialize-Assemblies {
    $libDir = Join-Path $here "lib"
    $assemblies = @{
        "core" = Join-Path $libDir "netstandard1.3\YamlDotNet.dll";
        "net45" = Join-Path $libDir "net45\YamlDotNet.dll";
        "net35" = Join-Path $libDir "net35\YamlDotNet.dll";
    }

    try {
        [YamlDotNet.Serialization.Serializer] | Out-Null
    } catch [System.Management.Automation.RuntimeException] {
        if ($PSVersionTable.PSEdition -eq "Core") {
            return [Reflection.Assembly]::LoadFrom($assemblies["core"])
        } elseif ($PSVersionTable.PSVersion.Major -ge 4) {
            return [Reflection.Assembly]::LoadFrom($assemblies["net45"])
        } else {
            return [Reflection.Assembly]::LoadFrom($assemblies["net35"])
        }
    }
}

Initialize-Assemblies | Out-Null