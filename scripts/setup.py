import os
import platform
import subprocess

from setup_python import PythonConfiguration as PythonRequirements
from setup_premake import PremakeConfiguration as PremakeRequirements

# Make sure everything we need for the setup is installed
PythonRequirements.Validate()
premakeInstalled = PremakeRequirements.Validate()

print("\nUpdating submodules...")
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

if (premakeInstalled):
    print("\nRunning premake...")
    currentPlatform = platform.system()

    if currentPlatform == 'Linux':
        subprocess.call(
            [os.path.abspath("./scripts/Linux-GenProjects.sh"), "nopause"])
    elif currentPlatform == 'Darwin':
        subprocess.call(
            ['chmod', 'u+x', os.path.abspath("./scripts/Mac-GenProjects.sh")])
    elif currentPlatform == 'Windows':
        subprocess.call(
            [os.path.abspath("./scripts/Win-GenProjects.bat"), "nopause"])
    else:
        print('Cannot Identify current platform')

    print("\nSetup completed!")
else:
    print("Prism requires Premake to generate project files.")
