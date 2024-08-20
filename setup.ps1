# Function to check and install a command
function Install-IfNotExists {
    param (
        [string]$CommandName,
        [string]$InstallCommand
    )

    if (-not (Get-Command $CommandName -ErrorAction SilentlyContinue)) {
        Write-Host "'$CommandName' command not found. Installing..."
        Invoke-Expression $InstallCommand
    } else {
        Write-Host "'$CommandName' command is already installed."
    }
}

# Install uv if not exists
Install-IfNotExists -CommandName "uv" -InstallCommand "irm https://astral.sh/uv/install.ps1 | iex"

# Install ruff if not exists
Install-IfNotExists -CommandName "ruff" -InstallCommand "irm https://astral.sh/uv/install.ps1 | iex"

# Ensure ~/.cargo/bin is in PATH
$CargoBinPath = "$HOME\.cargo\bin"
if (-not $env:PATH.Contains($CargoBinPath)) {
    Write-Host "Adding ~/.cargo/bin to PATH"
    $env:PATH = "$CargoBinPath;$env:PATH"
    
    # Optionally, add to the profile for future sessions
    $PathUpdate = "`$env:PATH = '$CargoBinPath;$env:PATH'"
    Add-Content -Path $PROFILE -Value $PathUpdate
    Write-Host "PATH updated in $PROFILE. Please restart your shell or run: `n`source $PROFILE`n"
}
