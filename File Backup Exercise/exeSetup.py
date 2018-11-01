import sys
from cx_Freeze import setup, Executable

setup(name = "AutoBackup",
      version = "1.0",
      description = "simple automated backup program",
      executables = [Executable("backupToZip.py")])