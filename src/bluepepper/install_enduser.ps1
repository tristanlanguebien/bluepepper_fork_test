$ErrorActionPreference = "Stop"

# Install virtual environment & dependencies
$install_script = Join-Path -Path $PSScriptRoot -ChildPath "install/install.py"
& python $install_script --update_packages

if ($LASTEXITCODE -ne 0) {
    throw "Python installation script failed with exit code $LASTEXITCODE"
}