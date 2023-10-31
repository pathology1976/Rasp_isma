import cx_Freeze

executables = [cx_Freeze.Executable("Rasp1.py")]

cx_Freeze.setup(
    name="Проверка расписания",
    options={"build_exe": {"packages":["pandas", "datetime", "openpyxl"]}},
    executables = executables
)