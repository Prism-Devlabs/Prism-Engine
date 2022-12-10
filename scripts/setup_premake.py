import platform
import os
from pathlib import Path
import utils


class PremakeConfiguration:
    currentPlatform = platform.system()
    premakePlatform = "nil"

    if currentPlatform == 'Linux':
        premakePlatform = "linux.tar.gz"
        print('Current platform is Linux')
    elif currentPlatform == 'Darwin':
        premakePlatform = "macosx.tar.gz"
        print('Current platform is MacOs')
    elif currentPlatform == 'Windows':
        premakePlatform = "windows.zip"
        print('Current platform is Windows')
    else:
        print('Cannot Identify current platform')
        premakePlatform = "windows.zip"

    premakeVersion = "5.0.0-beta2"
    currentPlatform = "windows.zip"
    premakeZipUrls = f"https://github.com/premake/premake-core/releases/download/v{premakeVersion}/premake-{premakeVersion}-{premakePlatform}"
    premakeLicenseUrl = "https://raw.githubusercontent.com/premake/premake-core/master/LICENSE.txt"
    premakeDirectory = "./vendor/premake/bin"

    @classmethod
    def Validate(cls):
        if (not cls.CheckIfPremakeInstalled()):
            print("Premake is not installed.")
            return False

        print(
            f"Correct Premake located at {os.path.abspath(cls.premakeDirectory)}")
        return True

    @classmethod
    def CheckIfPremakeInstalled(cls):
        premakeExe = Path(f"{cls.premakeDirectory}/premake5")
        if (not premakeExe.exists()):
            return cls.InstallPremake()

        return True

    @classmethod
    def InstallPremake(cls):
        permissionGranted = False
        while not permissionGranted:
            reply = str(input("Premake not found. Would you like to download Premake {0:s}? [Y/N]: ".format(
                cls.premakeVersion))).lower().strip()[:1]
            if reply == 'n':
                return False
            permissionGranted = (reply == 'y')

        premakePath = f"{cls.premakeDirectory}/premake-{cls.premakeVersion}-{cls.premakePlatform}"
        print("Downloading {0:s} to {1:s}".format(
            cls.premakeZipUrls, premakePath))
        utils.DownloadFile(cls.premakeZipUrls, premakePath)
        print("Extracting", premakePath)
        utils.UnzipFile(premakePath, deleteZipFile=True)
        print(
            f"Premake {cls.premakeVersion} has been downloaded to '{cls.premakeDirectory}'")
        premakeLicensePath = f"{cls.premakeDirectory}/LICENSE.txt"
        print("Downloading {0:s} to {1:s}".format(
            cls.premakeLicenseUrl, premakeLicensePath))
        utils.DownloadFile(cls.premakeLicenseUrl, premakeLicensePath)
        print(
            f"Premake License file has been downloaded to '{cls.premakeDirectory}'")
        return True
