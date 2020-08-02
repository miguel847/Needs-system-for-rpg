import sys
from cx_Freeze import setup, Executable
import pyperclip


base = None

executables = [
        Executable("what is the need.py", base= None)
]

buildOptions = dict(
        packages = [],
        includes = ["pyperclip"],
        include_files = [],
        excludes = []
)




setup(
    name = "What is the need",
    version = "2.0",
    description = "scrip used to calculete the needs for rpg game",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
