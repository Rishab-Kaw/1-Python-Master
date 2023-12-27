**Python Quick Reference Guide:**

1. **Checking Python Version**
   ```
   python3 --version
   ```

2. **PIP Documentation**
   - Access the pip documentation at: [Pip Documentation](https://pip.pypa.io/en/latest/)

3. **Checking PIP Version**
   ```
   python3 -m pip --version
   ```

4. **Listing Installed Packages:**
     ```
     python3 -m pip list
     ```

5. **Updating pip, setuptools, and wheel**
     ```
     python3 -m pip install --upgrade pip setuptools wheel
     ```

6. **Creating Virtual Environments**
     ```
     python3 -m venv <Directory-Name>
     ```

7. **Activating Virtual Environment**
   - On Windows:
     ```
     <Directory-Name>\Scripts\activate
     ```
   - On Unix/macOS:
     ```
     source <Directory-Name>/bin/activate
     ```

8. **Installing Packages**
   - To install a package (e.g., SomeProject):
     ```
     python3 -m pip install SomeProject
     ```
   - To install a specific version of a package:
     ```
     python3 -m pip install SomeProject==1.4
     ```
   - To install packages for the current user only:
     ```
     python3 -m pip install --user SomeProject
     ```

9. **Upgrading Packages**
     ```
     python3 -m pip install --upgrade SomeProject
     ```

10. **Uninstalling Packages**
      ```
      python -m pip uninstall sampleproject
      ```

11. **Installing from Local Archives**
    - Install from a local .whl file:
      ```
      python3 -m pip install sampleproject-1.0-py3-none-any.whl
      ```
    - Install from a local archive (e.g., tar.gz):
      ```
      python3 -m pip install ./downloads/SomeProject-1.0.4.tar.gz
      ```

12. **Installing from Version Control Systems (VCS)**  For example, installing from a GitHub repository:
      ```
      python -m pip install git+https://github.com/pypa/sampleproject.git@main
      ```

13. **Install packages from a Requirements File**
      ```
      python3 -m pip install -r requirements.txt
      ```

14. **Format of 'requirements.txt' File**
    - To install the latest version of a package:
      ```
      pytest  # Latest version from PyPI
      ```
    - To install a specific version of a package:
      ```
      beautifulsoup4==0.6.1
      ```
    - To install from a downloaded wheel file:
      ```
      ./downloads/numpy-1.9.2-cp34-none-win32.whl
      ```

15. **Finding User Base Binary Directory**
    - On Linux:
      ```
      python3 -m site --user-base
      python3 -m site --user-base bin
      ```
    - On Windows:
      ```
      py -m site --user-site
      py -m site --user-site site-packages
      py -m site --user-site Scripts

      - Example output:     C:\Users\Username\AppData\Roaming\Python36\site-packages
      - Update your PATH to include: C:\Users\Username\AppData\Roaming\Python36\Scripts
      ```
<br>

---

**Python Command Line Interface (CLI) options guide:**

**Basic Python Command Structure**
   ```
   python [options] [-c command | -m module-name | script | - ] [args]
   ```

1. **Running a Python Script**
   - Basic Usage: `python script.py`
   - This is the most common way to run a Python script. Replace `script.py` with the name of your Python file.

2. **Executing Commands Directly**
   - Command: `python -c "command"`
   - Use this to execute Python code directly in the command line. For example, `python -c "print('Hello, World!')"` will print "Hello, World!".

3. **Interactive Mode**
   - Command: `python -i`
   - This starts Python in interactive mode. It's a way to write and test Python code in a command-by-command manner, similar to a live Python shell.

4. **Running Modules as Scripts**
   - Command: `python -m module_name`
   - This allows you to run a Python module as a script. For example, `python -m http.server` starts a simple HTTP server.

5. **Verbose Mode**
   - Command: `python -v`
   - This prints verbose output, showing detailed information about the modules being imported.

6. **Version Information**
   - Command: `python --version` or `python -V`
   - Shows the version of Python that is currently installed.

11. **Help**
    - Command: `python -h` or `python --help`
    - Displays help information about Python command line options.
    
7. **Optimization**
   - Command: `python -O`
   - Runs Python scripts with optimizations. It removes assert statements and reduces the size of the bytecode.

8. **Isolated Mode**
   - Command: `python -I`
   - Runs Python in an isolated environment where it ignores environment variables and user site-packages.

9. **Unbuffered Output**
   - Command: `python -u`
   - This is useful for real-time logging. It forces the stdout and stderr streams to be unbuffered.

10. **Warnings Control**
    - Command: `python -W action`
    - Controls how Python displays warnings. You can ignore all warnings (`-W ignore`), turn warnings into errors (`-W error`), etc.

12. **No Site-Package Import**
    - Command: `python -S`
    - This option prevents Python from automatically importing the `site` module. This module is normally imported during startup and adds a few directories to the `sys.path` variable. Using `-S` can help in creating a more controlled environment.

13. **Debug Mode**
    - Command: `python -d`
    - This enables the debug output of the Python interpreter. While not commonly used for everyday scripting, it can be useful if you're delving into more complex Python development and need to understand what's happening under the hood.

14. **Bytecode Generation Control**
    - Command: `python -B`
    - Python automatically generates bytecode (`.pyc` files) when modules are imported. This option prevents Python from writing these bytecode files, which can be helpful in certain scenarios like read-only filesystems.

15. **Execute as Python**
    - Command: `python -x`
    - Skips the first line of the source. This is a niche option, typically used to allow Python scripts to be written for Unix shells, which require a specific first line (`#!`).

16. **Environment Variable Control**
    - Command: `python -E`
    - Ignores all Python-related environment variables like `PYTHONPATH` and `PYTHONHOME`. This is useful when you want to ensure your script runs in a default Python environment without any external influences.

18. **Quiet Mode**
    - Command: `python -q`
    - Reduces the verbosity of Python, particularly in interactive mode. It suppresses the copyright message and the prompt.

19. **Customize Python Run**
    - Command: `python -X`
    - This option allows for implementation-specific options. For example, 
        - `-X faulthandler` enables the fault handler, which provides detailed tracebacks for segfaults. These are advanced options, typically used for specific debugging or runtime behaviors.
       - `-X dev` (Development Mode): This mode activates additional runtime checks that are too expensive to be enabled by default. It can help catch certain bugs more easily, like deprecated features or resource leaks.
       - `-X importtime`: This shows how long each import takes. It's helpful for performance analysis, especially if your application has a slow startup time.

20. **Standard Input Execution**
    - Command: `python -`
    - This tells Python to read the script from standard input (stdin). It can be useful when you're piping commands into Python from another program.

<br>

---

# Environment Variables

Environment variables are key-value pairs that can affect the behavior of running processes on a computer, including Python processes. They are used to configure and pass information to Python and other applications.

**Why Use Environment Variables?**

Environment variables provide a flexible way to configure how Python behaves in different environments. For example, you might have different settings for development and production environments, and environment variables are a convenient way to manage these differences.

**How to Set Environment Variables**

- **On Windows**: You can set environment variables through the System Properties, or by using the `set` command in the command prompt (e.g., `set PYTHONPATH=C:\MyPythonLibs`).
  
- **On Unix/Linux/macOS**: You typically set them in your shell profile file (like `.bash_profile` or `.bashrc`) using the `export` command (e.g., `export PYTHONPATH=/my/python/libs`).

**Important Tip**

- Use environment variables sparingly and only when necessary. Over-reliance can make your Python environments complex and harder to manage.

**Python Environment Variables**

1. **`PYTHONPATH`**: This is like a list of directories where Python looks for modules to import (sys.path directory list). If you have Python code in a folder that isn't normally searched by Python, you can add that folder to `PYTHONPATH`, so Python knows to look there too.

2. **`PYTHONHOME`**: This variable sets the location of the standard Python libraries. If you have Python installed in a non-standard location, or if you're using a different version of Python, you can use `PYTHONHOME` to point to the correct location.

3. **`PYTHONSTARTUP`**: If you set this to the path of a Python file, that file will be executed every time you start the Python interpreter. It's like having a script that automatically runs when you start Python, useful for initializing settings or importing frequently used modules.

4. **`PYTHONCASEOK`**: This is used in Windows to make Python imports case-insensitive. Normally, Python is case-sensitive, so `import mymodule` and `import MyModule` would be different. Setting `PYTHONCASEOK` changes this behavior.

6. **`PYTHONIOENCODING`**:
Defines the encoding used for stdin/stdout/stderr, useful for changing the default text encoding.

8. **`PYTHONWARNINGS`**:
Allows control over how Python displays warnings. You can use this to suppress or elevate the visibility of specific warning categories.

9. **`PYTHONOPTIMIZE`**:
Enables optimization. Setting it to 1 removes assert statements and setting it to 2 removes both assert statements and docstrings.

10. **`PYTHONDEBUG`**:
When set, Python runs in debug mode, which can provide more verbose diagnostic information.

14. **`PYTHONUSERBASE`**:
Specifies the base directory for user-based installations. When set, Python installs packages in this directory.

15. **`PYTHONNOUSERSITE`**:
When set, Python ignores the user's site-packages directory.

17. **`PYTHONLEGACYWINDOWSFSENCODING`**:
On Windows, use a legacy encoding for the filesystem and environment variables (affects how Python handles non-ASCII characters).

18. **`PYTHONPYCACHEPREFIX`**:
Specifies the root directory for bytecode cache files if you don't want to use the default `__pycache__` directories inside your source directories.

<br>

---

# Python on Unix systems

**Making Python Scripts Executable on Unix Systems:**
   - Unix systems, like Linux and macOS, require a special setting for any file to be run as a program. This is not about the content of the file but how the system sees it.
   - To make a Python script executable, you use a command called `chmod +x`. This command changes the "mode" of the file to make it executable. Think of it as telling the system, "Hey, this is not just a text file; it's a program that you can run."

**Adding a Shebang Line:**
   - A "Shebang" line is the first line in a script that tells the system where the Python interpreter is located. The Python interpreter is the program that reads and runs your Python code.
   - The Shebang line looks like this: `#!/usr/bin/env python3`.
   - This line does two things:
     - It starts with `#!`, which is the magic combo that Unix systems recognize as a signal to look for an interpreter.
     - `/usr/bin/env python3` is a way of telling the system, "Find the Python 3 interpreter wherever it is installed." It's like saying, "Don't worry about where Python is; I trust you to find it."

**Why Use `/usr/bin/env python3`?**
   - The advantage of using `/usr/bin/env python3` is flexibility. It searches for Python in all the standard places where programs are stored (`PATH`). So even if Python is not in the usual place, as long as it's somewhere in your system and in the `PATH`, it will be found and used.

**Alternative: Hardcoding the Interpreter Path:**
   - In some Unix systems, the `env` command might not be available. In such cases, you need to tell the system exactly where Python is.
   - You do this by replacing `/usr/bin/env python3` with the direct path to the Python interpreter, like `/usr/bin/python3`. This is like saying, "Don't look anywhere else; just use the Python interpreter located here."

<br>

---

# Python on Windows systems

In Windows, you can set Environment variables in two ways: temporarily for just your current session, or permanently.

#### Temporarily Setting Environment Variables

1. **Using Command Prompt**:
   - Open the Command Prompt.
   - Use the `set` command to change environment variables.
   - Example: 
     - `set PATH=C:\Program Files\Python 3.9;%PATH%` adds the Python 3.9 directory to the beginning of the PATH variable.
     - `set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib` adds a new directory to the PYTHONPATH.
   - These changes only last for the current session. If you close the Command Prompt, the changes are gone.

2. **How It Works**:
   - Adding `%PATH%` or `%PYTHONPATH%` in the command includes the existing value of the variable, so you're just adding new information to it, not replacing it.
   - Changing `PATH` like this is a common way to make sure the system uses the Python version you want.

#### Permanently Setting Environment Variables

1. **Accessing the Environment Variables Dialog**:
   - Click Start and search for ‘edit environment variables’ or go through System properties and Advanced system settings.
   - In the dialog that appears, you can add or change both User and System variables.

2. **User vs System Variables**:
   - User variables are specific to your user account, while System variables affect all users on the computer.
   - To change System variables, you need Administrator rights.

3. **Important Considerations**:
   - When setting variables, Windows adds User variables after System variables, which might cause unexpected results, especially when changing the PATH variable.
   - The PYTHONPATH variable affects all versions of Python on your system. If you set this permanently, make sure the paths you add are compatible with all your Python versions.


### UTF-8 Mode in Python

#### Background

- **System Encoding on Windows**:
   - Traditionally, Windows uses its own legacy encodings (known as the ANSI Code Page) for system encoding, which is the default way the system represents text.

- **Python's Default**:
   - Python, when running on Windows, uses this system encoding as its default for handling text files. This can cause problems because it's different from UTF-8.

- **UTF-8**:
   - UTF-8 is a modern way of encoding text that is widely used on the internet and in most Unix systems (like Linux), including WSL (Windows Subsystem for Linux).

#### Python UTF-8 Mode

- **Purpose**:
   - To avoid issues caused by different encodings, Python 3.7 introduced a UTF-8 Mode. This mode changes Python’s default text encoding to UTF-8.

- **How to Enable**:
   - You can turn on UTF-8 Mode in Python in two ways:
     - Using a command line option: `-X utf8`
     - Setting an environment variable: `PYTHONUTF8=1`

- **System Encoding Still Available**:
   - Even when UTF-8 Mode is enabled, you can still use the Windows legacy encoding through the "mbcs" codec.

#### Important Notes

- **Global Effect**:
   - If you add `PYTHONUTF8=1` to your system's default environment variables, it will affect all Python applications (version 3.7 and above) on your system.

- **Caution**:
   - If you have Python applications that depend on the old Windows system encoding, it's better to enable UTF-8 Mode temporarily (using the command line option or setting the environment variable only when needed) instead of setting it globally.

- **UTF-8 in Certain Areas**:
   - Regardless of whether UTF-8 mode is enabled, Python uses UTF-8 by default on Windows for:
     - Console input/output, including standard I/O (see PEP 528).
     - Filesystem encoding (see PEP 529).

### Python Launcher for Windows

#### Overview
- **Purpose**: The Python Launcher for Windows helps you find and run different versions of Python installed on your Windows system.
- **Functionality**: It allows you to specify a preferred Python version in scripts or the command line. The launcher then locates and executes that version.

#### Key Features
1. **Automatic Version Selection**:
   - Unlike manually setting the PATH variable, the launcher automatically selects the most appropriate Python version.
   - It prioritizes user-level installations over system-wide ones and chooses based on the Python version, not on the installation order.

2. **Getting Started**:
   - **From Command-Line**:
     - Type `py` in Command Prompt to start the latest Python version installed.
     - Use `py -3.7` to specifically start Python 3.7, or `py -2` for the latest Python 2 version.
     - If `py` is not recognized, it means the launcher isn't installed, or not added to PATH.
     - The command `py --list` shows all installed Python versions.

   - **Virtual Environments**:
     - If a virtual environment is active, `py` runs the Python version in that environment, unless specified otherwise.

   - **From a Script**:
     - Use a shebang line like `#! python` or `#! python3` in your Python script to specify which Python version to use.

   - **From File Associations**:
     - Double-clicking a Python file (.py, .pyw, .pyc) will use the launcher if it's associated, letting the script specify the Python version.

3. **Shebang Lines**:
   - A shebang line (`#!`) at the start of a script file indicates which Python version should be used.
   - The launcher supports various virtual commands in shebang lines to specify the Python interpreter (e.g., `/usr/bin/env python`, `/usr/bin/python`).
   - Shebang lines can include explicit version numbers and architecture (32-bit or 64-bit).

4. **Customization**:
   - **INI Files**:
     - Customize the launcher's behavior using `.ini` files located in the user's application data directory or the same directory as the launcher.
   - **Default Python Versions**:
     - Set default Python versions using `PY_PYTHON` and other environment variables or specify in the `.ini` file.
   - **Diagnostics**:
     - Set `PYLAUNCH_DEBUG` as an environment variable to get diagnostic information from the launcher.


### Finding Modules in Python for Windows

#### Python Library Location
- Python usually stores its library in the installation directory. For example, if Python is installed in `C:\Python\`, you'll find:
  - The default library in `C:\Python\Lib\`
  - Third-party modules in `C:\Python\Lib\site-packages\`

#### Overriding sys.path with ._pth Files
- To override `sys.path` (which is a list of directory names that Python uses to search for modules), you can create a `._pth` file with the same name as the Python DLL (like `python37._pth`) or the executable (like `python._pth`).
- This `._pth` file allows you to specify directories to add to `sys.path`. 
- The `._pth` file based on the DLL name overrides the one based on the executable.
- In this file, you can include or ignore certain paths (using `#` for comments). It disables all registry and environment variables, and enables isolated mode.
- `.pth` files (without leading underscore) are still processed normally when `import site` is specified.

#### How sys.path is Populated on Windows
- An empty entry (current directory) is added at the start.
- If `PYTHONPATH` environment variable exists, its entries are added next.
- Additional application paths can be added in the Windows registry under `\SOFTWARE\Python\PythonCore{version}\PythonPath`.
- `PYTHONHOME` environment variable or the path of the Python executable is used to deduce the “Python Home”. The subdirectories of this home are added to `sys.path`.
- In the absence of `PYTHONHOME`, a default path with relative entries is used.
- In the presence of a `pyvenv.cfg` file, the home path is adjusted based on its contents.

#### Python Executable Behavior
- When running `python.exe`, the core path is deduced, ignoring the core paths in the registry.
- For Python hosted in another `.exe`, the core path from the registry is used.
- If Python can't find its home and no registry values are present, default relative paths are used.


### Additional Windows-Specific Modules

#### Windows-Specific Standard Modules
- Python includes some modules that are specifically for Windows, documented in MS Windows Specific Services.

#### PyWin32
- PyWin32 by Mark Hammond provides advanced Windows-specific support. It includes utilities for:
  - Component Object Model (COM)
  - Win32 API calls
  - Registry, Event log
  - Microsoft Foundation Classes (MFC) user interfaces
- PythonWin, included in PyWin32, is an embeddable IDE with a built-in debugger.

<br>

---

### Exiting the Python Interpreter
- To close the Python program, press Control-D (on Unix systems like Linux or macOS) or Control-Z (on Windows). This will stop the program.
- If that doesn't work, you can also type `quit()` and press Enter to exit.

### Passing Arguments to a Script
- When you run a Python script, the script's name and any extra information you give it are stored in a list called `argv`, which is part of the `sys` module.
- To see this list, you need to include `import sys` in your script.
- This list always has at least one item. If you run Python without a script, the first item is an empty string.
- If you run a script by typing `-` (which means using input from your keyboard), the first item in the list is `-`.
- If you use `-c` (to run a specific command) or `-m` (to run a module), the first item shows `-c` or the module's full name, respectively.

### Python Files - Source Code Encoding
- Normally, Python files are written in a format called UTF-8. This lets you use many different characters from various languages in your code.
- To see these characters correctly, your text editor must support UTF-8 and use a suitable font.

- **Changing Encoding**:
  - If you need a different format than UTF-8, you can specify this with a special line at the start of your file: `# -*- coding: encoding -*-`, replacing `encoding` with your chosen format.
  - For instance, to use Windows-1252 encoding, start your file with `# -*- coding: cp1252 -*-`.
  - If your file begins with a shebang line (like `#!/usr/bin/env python3`), put the encoding line right after it. 


<br>

---

### Top-Level Components

- **Python Interpreter**: It's like the manager of a Python program. It reads your code and tells the computer what to do with it.

#### How Python Runs Code
- **Different Ways to Run Python**:
  - **Script File**: You can write your Python code in a file and run it. Example: Running `python script.py` in the command line.
  - **Interactive Mode**: Typing Python code directly into the Python prompt (`>>>`). It's like having a conversation with Python, where you type a command, and Python immediately responds.
  - **Module Source File**: When you import a module, Python runs the code in that module.

#### Running Complete Programs
- **Environment When Running a Program**:
  - Only a few parts of Python are ready to go (`sys` for system operations, `builtins` for basic functions and values, and `__main__` where your code runs).
  - Think of it as starting with a clean workspace with only essential tools.
- **Ways to Give Python Your Program**:
  1. Using `-c string` in the command line (for a short piece of code).
  2. As a file (like `python my_program.py`).
  3. Through standard input (typing or pasting code directly).

#### File Input
- **Reading from Files**: Python can read and execute code written in a file.
- **Usage**: This is how Python reads a complete program or module, or code given to `exec()`. `exec()` is for executing complex Python code.

#### Interactive Input
It's great for quick tests or learning by trying small pieces of code and seeing immediate results.
- **Interactive Mode Rules**: When you're typing code directly into Python:
  - After a complex command (like a multi-line `if` statement), you need to leave a blank line to let Python know you're done.
  
#### Expression Input for `eval()`
- **Using `eval()`**: This function is for running simple expressions, like `eval("3 + 4")`. It ignores spaces at the start.
- **Format**: You should give `eval()` a string that is just a Python expression.
- Use `eval()` for simple calculations or value evaluations. 
  
