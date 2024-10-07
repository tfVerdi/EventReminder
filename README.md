# Verdi's daily reminder

A personal organization tool, designed to be customized with your own events, built into an executable and set up as a startup program on your PC, so you can be easily reminded of upcoming or recently passed events (within a 7 day range).

This program has no external dependencies, only Python's packed libraries are used.

# How to use

- Check out the source code (main.py).
- Customize your events following the format present at the IMPORTANT DATES section of the code, if there are more than one event in one particular day, use a newline character to separate them on the string ("\n").
- Build into an .exe. Using the PyInstaller library with the --onefile option is recommended for simplicity, but likely nothing will break if you build it in some other way.
- Set executable to run on startup on your OS.