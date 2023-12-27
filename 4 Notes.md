# Python Notes

---

1. **Checking Python Version**
    ```
    python3 --version
    ```

2. **Checking PIP Version**
    ```
    python3 -m pip --version
    ```

3. **Listing Installed Packages:**
    ```
    python3 -m pip list
    ```

4. **Updating pip, setuptools, and wheel**
    ```
    python3 -m pip install --upgrade pip setuptools wheel
    ```

---

5. **Creating New Virtual Environment**
    ```
    python3 -m venv <Directory-Name>
    ```

6. **Activating Virtual Environment**
   - On Windows:
     ```
     <Directory-Name>\Scripts\activate
     ```
   - On Unix/macOS:
     ```
     source <Directory-Name>/bin/activate
     ```

---

7. **Installing Packages**
   - To install a package (e.g., SomeProject):
     ```
     python3 -m pip install SomeProject
     ```
   - To install a specific version of a package:
     ```
     python3 -m pip install SomeProject==1.4
     ```

8. **Upgrading Packages**
    ```
    python3 -m pip install --upgrade SomeProject
    ```

9. **Uninstalling Packages**
    ```
    python -m pip uninstall sampleproject
    ```

10. **Install packages from a Requirements File**
    ```
    python3 -m pip install -r requirements.txt
    ```
  - Format of 'requirements.txt' File - 
    ```
    pytest  # Installs Latest version
    pandas==1.2.3  # Installs Specific version
    ```

---

11. **Basic Python Command Structure**
    ```
    python [options] [-c command | -m module-name | script - ] [args]
    ```
    - Basic Usage: `python script.py`
      This is the most common way to run a Python script. Replace `script.py` with the name of your Python file.

    - Executing Commands Directly: `python -c "command"`
      Use this to execute Python code directly in the command line. For example, `python -c "print('Hello, World!')"` will print "Hello, World!".

    - Interactive Mode: `python -i`
      This starts Python in interactive mode. It's a way to write and test Python code in a command-by-command manner similar to a live Python shell.

    - Running Modules as Scripts: `python -m module_name`
      This allows you to run a Python module as a script. For example, `python -m http.server` starts a simple HTTP server.

    - Help: `python -h` or `python --help`
      Displays help information about Python command line options.

---

12. **Environment variables**
are key-value pairs that can affect the behavior of running processes on a computer, including Python processes. They are used to configure and pass information to Python and other applications. Use environment variables only when necessary.

  - **How to Set Environment Variables**
    - **On Windows**: set environment variables through the System Properties (Environment Variables Dialog) - save in PATH=C:\Program Files\Python 3.9, or by using the `set` command in the command prompt (e.g., `set PYTHONPATH=C:\MyPythonLibs`).
    - **On Unix/Linux/macOS**: You typically set them in your shell profile file (like `.bash_profile` or `.bashrc`) using the `export` command (e.g., `export PYTHONPATH=/my/python/libs`).

  - **Important Python Environment Variables**
    - **`PYTHONPATH`**: This is a list of directories where Python looks for modules to import (sys.path directory list). If you have Python code in a folder that isn't normally searched by Python, you can add that folder to `PYTHONPATH`, so Python knows to look there too.
    - **`PYTHONHOME`**: This variable sets the location of the standard Python libraries. If you have Python installed in a non-standard location, or if you're using a different version of Python, you can use `PYTHONHOME` to point to the correct location.
    - **`PYTHONUSERBASE`**:
    Specifies the base directory for user-based installations. When set, Python installs packages in this directory.

---

**Making Python Scripts Executable on Linux Systems:**

  - To make a Python script executable, you use a command called `chmod +x`.

  - Adding a Shebang Line: `#!/usr/bin/env python3`
    A "Shebang" line is the first line in a script that tells the system where the Python interpreter is located.
    `/usr/bin/env python3` is a way of telling the system, "Find the Python 3 interpreter wherever it is installed.

---

**Python Library Location in Windows:**

  - Python usually stores its library in the installation directory. For example, if Python is installed in `C:\Python\`, you'll find:

    - The default library in `C:\Python\Lib\`
    - Third-party modules in `C:\Python\Lib\site-packages\`

---

**Exiting the Python Interpreter**
  - To close the Python program, press `Ctrl+D` (on Linux) or `Ctrl+Z` (on Windows). This will stop the program.
  - If that doesn't work, you can also type `quit()` and press Enter to exit.

---

**Python Files - Source Code Encoding**
  - Normally, Python files are written in UTF-8 format. This lets you use many different characters from various languages in your code. To see these characters correctly (including Emojis), your text editor must support UTF-8 and use a suitable font.
  - If you need a different format than UTF-8, you can specify this with a special line at the start of your file: `# -*- coding: encoding -*-`, replacing `encoding` with your chosen format. If your file begins with a shebang line (like `#!/usr/bin/env python3`), put the encoding line right after it.
  - For instance, to use Windows-1252 encoding, start your file with `# -*- coding: cp1252 -*-`.

---

### Physical and Logical Lines in Python

- **Physical Line**: This is what you see in your code as a single line. It ends when you press "Enter" to start a new line.
- **Logical Line**: This is what Python sees as a single statement or instruction. Sometimes, a logical line can be spread over several physical lines for better readability.

#### Explicit Line Joining: Using Backslashes

- **Simplified Explanation**: If a line of code is too long, you can break it into multiple lines for easier reading. You do this by ending a line with a backslash (`\`). Python then understands that the next line is a continuation of the current one.
- **Why Use It**: Long lines of code can be hard to read. Splitting them makes your code cleaner and more understandable.
- **Remember**: 
  - Don't put a comment or a text (like a word in quotes) right after a backslash on the same line.
  - Example:
    ```python
    if 1900 < year < 2100 and 1 <= month <= 12 \
       and 1 <= day <= 31 and 0 <= hour < 24:
            print("Valid date")
    ```
    In this example, a long `if` condition is broken down into two lines using a backslash.

#### Implicit Line Joining: Using Parentheses, Brackets, or Braces

- **Simplified Explanation**: If you're writing something inside parentheses `()`, square brackets `[]`, or curly braces `{}`, you can naturally extend it over multiple lines without backslashes.
- **Why Use It**: This is handy for lists, long conditions, or grouped items. It keeps your code organized.
- **Remember**:
  - The indentation (spaces at the beginning of a line) of these continuation lines doesn't matter to Python.
  - You can include comments on these lines.
  - Example:
    ```python
    days = ["Monday", "Tuesday", "Wednesday",  # These are days
            "Thursday", "Friday"]              # of the week
    ```
    Here, a list of weekdays is split over two lines for clarity.

---


### Blank Lines in Python

- **What It Means**: In Python, if you have a line with nothing on it, or just spaces or tabs, Python mostly ignores this line. Think of blank lines as 'breaks' or 'pauses' in your code. They don't affect how your code runs.
- **Interactive Python**: If you're typing code directly into Python (like in an interactive shell), a completely blank line (with no spaces or comments) tells Python you've finished a command or a block of code, and it's time to run it.


### Indentation in Python

- **Why It Matters**: Python uses spaces at the start of a line (indentation) to figure out how your code is organized. It's like outlining an essay, where each level of indentation is a new section.
- **Tabs vs. Spaces**: Python can get confused if you mix tabs and spaces. It's like mixing two different types of bullets in a list. To stay safe, stick to one: either only use spaces or only use tabs.
- **What Happens with Tabs**: Python converts tabs into a set number of spaces to keep things consistent across different computers.


### Whitespace Between Tokens in Python

- **What's a Token**: Think of tokens as words in your code. They can be things like variable names, numbers, or operators.
- **Why Whitespace**: Just like in English, where you put spaces between words, in Python, you use spaces to separate these 'words' so Python can understand them clearly.
- **When You Need It**: You need spaces when two 'words' next to each other could be mistaken for a different word. For example, `isopen` could be read as one thing, but `is open` is two different things.

**Example**:
- Without enough space: `age=25`
- With proper space: `age = 25`

**Tip**: While Python is flexible with where you put spaces, using them well can make your code much easier to read.

- **Formfeed Characters**: These are rare, but if you see a `^L` character, it's a formfeed. In most cases, you won't need to use these in your Python code.

---

### Identifiers (Names) in Python

- **What They Are**: Identifiers are the names you give to things in your code, like variables or functions. 
- **Simple Rules for Creating Them**:
  - Start with a letter (A to Z, either upper or lower case) or an underscore (_).
  - After the first character, you can also use numbers (0 to 9).
  - Avoid using special characters except the underscore.
- **Why Care About Identifiers**: Picking the right names helps make your code clear and avoids conflicts with Python's built-in commands. Consistency and clarity in naming are key to writing good code.

**Example**:
- Valid identifiers: `my_variable`, `number1`, `Profile2`
- Invalid identifiers: `2things`, `my-variable`, `$money`

### Reserved Classes of Identifiers

- **Special Names with Underscores**:
  - Names starting with an underscore (`_name`) are special. They're not brought in when you use import command like `from module import *`.
  - A single underscore (`_`) is used in some specific cases, like in pattern matching, or in interactive mode to hold the last result.
  - Names with double underscores at both ends (`__name__`) (known as “dunder” names) are used by Python itself and have special meaning.
  - Names starting with double underscores (`__name`) are private within a class, meaning they're meant to be used only inside the class.

---

### Best practices for naming identifiers (such as variables, functions, classes, etc.)

These practices about making the code more readable, maintainable, and understandable. 

1. **PEP 8 Guidelines**: 
   - **Variables and Functions**: Use lowercase words or words separated by underscores (e.g., `my_variable`).
   - **Classes and Exceptions**: Use the CapWords convention (e.g., `MyClass`).
   - **Constants**: Use all uppercase letters with underscores separating words (e.g., `MY_CONSTANT`).

2. **Descriptive Names**: Choose names that are descriptive and give a clear idea about the purpose of the variable, function, or class. For example, `calculate_total_price` is better than `ctp` or `calc`.

3. **Avoid Ambiguity**: Avoid names that are too generic or vague. For example, `data` or `info` can be too ambiguous. Instead, use names like `customer_data` or `game_info`. Avoid using names that are too similar. For example, `user_list` and `users_list` might be confusing.

4. **Use Meaningful Names for Loops and Iterators**: For instance, instead of using `i` and `j` for loop variables, use names like `for employee in employees`.

5. **Single-letter Names**: Generally, avoid single-letter names except in certain contexts like loop iterators or lambda functions where their scope is very small and their purpose is obvious.

6. **Naming Private and Protected Members**: In Python, prefix a single underscore for protected members (e.g., `_protected_var`) and double underscore for private members of a class (e.g., `__private_var`).

7. **Use Verb Phrases for Functions**: Function names should typically be verb phrases (e.g., `calculate_total`, `read_file`) as they often represent actions. For functions handling specific events, include the event in the name (e.g., `on_click`, `after_save`).

8. **Use Noun Phrases for Classes**: Class names should typically be noun phrases (e.g., `Car`, `UserAccount`) as they often represent objects or concepts.

9. **Use Conventions for Specific Types of Variables**:
    - **Boolean Variables**: Use is, has, or can in names (e.g., `is_visible`, `has_completed`).
    - **Iterables**: Use plural names for lists or collections (e.g., `items`, `users`).

10. **Avoid Using Numbers in Names**: Names like `data1`, `data2`, etc., are not descriptive and should be avoided. Instead, use names that describe what the data represents.

11. **Naming in Test Cases**: In test functions, names should be very descriptive, explaining what condition or scenario is being tested.

12. **Prefix Unused Variables**: If a variable is intentionally not used, prefix it with an underscore (e.g., `_unused_var`).

---

### Keywords in Python

- **What They Are**: Keywords are special words that Python uses for its language and you can't use them as names. These words are like the commands and structure of the Python language. They're the basic building blocks of Python's syntax.
- **Keywords**:
```
They must be spelled exactly as written here:

False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### Soft Keywords in Python

- **What They Are**: These are words that are normal most of the time, but in specific situations, they become special.
- **Examples**:
  - `match` and `case` are used in pattern matching.
  - `_` can act as a placeholder or wildcard in certain contexts.

---

### Literals

#### What Are Literals?
- **Literals** are fixed values in your code. They can be text (strings) or data (bytes).

#### String and Bytes Literals

- **String Literals**:
  - Enclosed in quotes: Use single (`' '`) or double (`" "`) quotes for basic strings.
  - Triple quotes for multi-line: Use three single (`''' '''`) or double (`""" """`) quotes for strings that span multiple lines.
  - Prefixes change behavior:
    - `r` or `R`: Treats backslashes as regular characters (raw string). Example: `r"\n"` is two characters: a backslash and an `n`.
    - `f` or `F`: Allows embedding expressions (formatted string). Example: `f"Hello {name}"` inserts the value of `name`.

- **Bytes Literals**:
  - For binary data, not text.
  - Start with `b` or `B`. Example: `b'hello'` is a bytes literal.
  - Can only contain ASCII characters.

#### Important Rules

- **Raw Strings**: `r"\""` is a two-character string: backslash and quote. Raw strings can't end with a single backslash.
- **No Space Allowed**: Don't put space between prefix (`r`, `f`, `b`) and the quotes.
- **Triple-quoted Strings**: Can contain unescaped newlines and quotes.

### Escape Sequences

- Escape sequences allow you to include special characters in strings that would otherwise be difficult to type directly.
- They are especially useful for adding control characters (like newlines or tabs) and for escaping characters that have special meanings in Python strings (like the backslash, single, and double quotes).

### Common Escape Sequences (for both String and Bytes Literals)

1. `\\` - Backslash (`\`)
2. `\'` - Single quote (`'`)
3. `\"` - Double quote (`"`)
4. `\a` - ASCII Bell (BEL)
5. `\b` - ASCII Backspace (BS)
6. `\f` - ASCII Formfeed (FF)
7. `\n` - ASCII Linefeed (LF)
8. `\r` - ASCII Carriage Return (CR)
9. `\t` - ASCII Horizontal Tab (TAB)
10. `\v` - ASCII Vertical Tab (VT)
11. `\ooo` - Character with octal value `ooo`
12. `\xhh` - Character with hex value `hh`

### Additional Escape Sequences for String Literals

1. `\N{name}` - Character named `name` in the Unicode database
2. `\uxxxx` - 16-bit Unicode character with the value `xxxx` (4 hex digits)
3. `\Uxxxxxxxx` - 32-bit Unicode character with the value `xxxxxxxx` (8 hex digits)

#### Examples

- **String Literal**: `"Hello"`
- **Raw String**: `r"C:\User\name"`
- **Formatted String**: `f"Score: {score}"`
- **Bytes Literal**: `b"hello"`

### Why Use Different Literals?

- **Raw Strings**: Useful for file paths, regular expressions where you don't want backslashes treated as escape characters.
- **Formatted Strings**: Handy for inserting values into strings, like printing messages with variables.
- **Bytes Literals**: Used when dealing with binary data, not just text.

To enhance the explanation for a beginner, I'll add a bit more context and simplify the technical terms even further:

### String Literal Concatenation

#### What is String Concatenation?
- **String Concatenation**: It's like putting sentences together to make a longer sentence. In Python, if you write two or more string or byte sequences next to each other, they automatically join together to form one longer string or byte sequence.

#### How Does It Work?
- **No Need for `+` with Literals**: Normally, you might use a `+` to add strings together, like `string1 + string2`. But with string literals (the text you write directly in your code inside quotes), Python does this automatically if they are next to each other.
- **Mixing Quotes is Okay**: You can use different types of quotes (single `' '`, double `" "`, or triple `''' '''`/`""" """`) side by side. Python doesn't mind and treats them as one.
- **Example**: Writing `"hello" 'world'` is just like writing `"helloworld"`.

#### Why Use This Feature?
- **Helpful for Long Text**: It's great for breaking up a really long string into smaller, more readable pieces.
- **Fewer Backslashes Needed**: Sometimes, you need to use a backslash `\` in strings for special characters. By splitting the string, you might reduce the need for these backslashes.
- **Adding Comments**: You can even put comments next to each part of your string for better explanation.

#### Example of String Concatenation in Code

```python
re.compile("[A-Za-z_]"       # This is for a letter or underscore
           "[A-Za-z0-9_]*"   # This adds letters, digits or underscores
          )
```
Here, we split a complex string (used in a function called `re.compile`) into two parts and added comments to each part. Python treats these two parts as one continuous string.

---

### Formatted String Literals (f-strings)

#### What are f-strings?
- **f-strings**: Special strings in Python that start with `f` or `F` before the quotes. They allow you to include Python code, like variables or calculations, right inside the string.

#### How f-strings Work
- **Basic Idea**: You write an f-string with curly braces `{}` where you want to insert code. For example, `f"Hello, {name}"` will replace `{name}` with the value of the `name` variable.
- **Parts of an f-string**:
  - **Regular Text**: Everything outside `{}` is normal text and Python just prints it as is.
  - **Double Curly Braces**: To show an actual curly brace, use `{{` or `}}`. Python will change these to single curly braces.
  - **Inside Curly Braces**: This is where you put your Python code. It can be a simple variable, a calculation, or something more complex.

#### Examples of f-strings

1. **Simple Variable**: 
   ```python
   name = "Fred"
   f"He said his name is {name}."
   ```
   Output: `"He said his name is Fred."`

2. **Debugging with `=`**: 
   ```python
   today = datetime(year=2017, month=1, day=27)
   f"{today=:%B %d, %Y}"
   ```
   Output: `"today=January 27, 2017"`

3. **Formatting Numbers**: 
   ```python
   width = 10
   precision = 4
   value = decimal.Decimal("12.34567")
   f"result: {value:{width}.{precision}}"
   ```
   Output: `"result:      12.35"`

4. **Using Date Format Specifier**: 
   ```python
   f"{today:%B %d, %Y}"
   ```
   Output: `"January 27, 2017"`

5. **Integer Formatting**: 
   ```python
   number = 1024
   f"{number:#0x}"
   ```
   Output: `"0x400"`

6. **Preserving Whitespace**: 
   ```python
   foo = "bar"
   f"{ foo = }"
   ```
   Output: `" foo = 'bar'"`

7. **Escaping Quotes**: 
   ```python
   line = "The mill's closed"
   f"{line = :20}"
   ```
   Output: `"line = The mill's closed   "`

8. **Using Raw String**: 
   ```python
   f"{line = !r:20}"
   ```
   Output: `'line = "The mill\'s closed" '`

#### Special Notes

- **Quotes in Expressions**: If your f-string uses double quotes, use single quotes inside the curly braces and vice versa to avoid errors.
- **No Backslashes in Expressions**: You can't use backslashes inside the curly braces. Use a variable instead.

#### f-strings vs. Regular Strings

- **f-strings are Dynamic**: They can include changing data, like the current value of a variable.
- **Regular Strings are Static**: They always show exactly what you write.

---

### Numeric Literals
Numbers written directly in your code.

#### Types of Numeric Literals
- **Three Types**: Integers (whole numbers), floating point numbers (with decimals), and imaginary numbers (used in complex math).

#### Integers
- **Decimal (Base 10)**: Regular numbers without any prefix, like `7` or `2147483647`.
- **Binary (Base 2)**: Numbers that start with `0b` or `0B`, made up of only `0` and `1`. Example: `0b101` (equals 5 in decimal).
- **Octal (Base 8)**: Start with `0o` or `0O`, use digits from 0 to 7. Example: `0o10` (equals 8 in decimal).
- **Hexadecimal (Base 16)**: Start with `0x` or `0X`, use digits and letters A to F. Example: `0x1A` (equals 26 in decimal).
- **Underscores for Readability**: Like `100_000` to make large numbers easier to read.
- **No Leading Zero Rule**: You can't start a non-zero decimal number with extra zeros.

#### Floating Point Numbers
- **Structure**: Numbers with a decimal point (`.`) or an exponent (`e` or `E`). Example: `3.14`, `2e2` (equals 200).
- **Digit Grouping**: You can use underscores here too, like `1_000.000_1`.

#### Imaginary Numbers
- **Imaginary Literals**: Numbers ending with `j` or `J`, representing the imaginary part of complex numbers. Example: `3j`.
- **Creating Complex Numbers**: Combine them with real numbers, like `2 + 3j`.

#### Examples

- **Integer Examples**:
  - Decimal: `123`, `100_000`
  - Binary: `0b101` (equals 5)
  - Octal: `0o10` (equals 8)
  - Hexadecimal: `0x1A` (equals 26)
- **Floating Point Examples**:
  - `3.14`, `10.0`, `1_000.000_1`, `2e2`, `3.14e-10`
- **Imaginary Number Examples**:
  - `3j`, `10j`, `1e100j`, `3.14_15_93j`

---

### Operators

**Operators**: These are special symbols in Python that carry out arithmetic or logical computation.

#### Arithmetic Operators
- `+`: Add
- `-`: Subtract
- `*`: Multiply
- `/`: Divide
- `//`: Floor Division
- `%`: Modulus (Remainder)
- `**`: Exponentiation

#### Bitwise Operators
- `<<`: Bitwise Left Shift
- `>>`: Bitwise Right Shift
- `&`: Bitwise AND
- `|`: Bitwise OR
- `^`: Bitwise XOR
- `~`: Bitwise NOT

#### Comparison Operators
- `<`: Less Than
- `>`: Greater Than
- `<=`: Less Than or Equal To
- `>=`: Greater Than or Equal To
- `==`: Equal To
- `!=`: Not Equal To

#### Assignment Operator
- `:=`: Walrus Operator (Assigns values from expressions)

### Delimiters 
These are symbols that mark the beginning or end of a segment of code.

#### Basic Delimiters
- `(`, `)`: Parentheses
- `[`, `]`: Square Brackets
- `{`, `}`: Curly Braces
- `,`: Comma
- `:`: Colon
- `.`: Period (used in floating points too)
- `;`: Semicolon
- `@`: At symbol (used for decorators)
- `=`: Equal sign (assignment)
- `->`: Arrow (used in function annotations)

#### Augmented Assignment Operators
- `+=`: Add and Assign
- `-=`: Subtract and Assign
- `*=`: Multiply and Assign
- `/=`: Divide and Assign
- `//=`: Floor Divide and Assign
- `%=`: Modulus and Assign
- `@=`: At and Assign
- `&=`: AND and Assign
- `|=`: OR and Assign
- `^=`: XOR and Assign
- `>>=`: Right Shift and Assign
- `<<=`: Left Shift and Assign
- `**=`: Exponent and Assign


### Special Characters

#### Significant Characters
- `'`: Single Quote
- `"`: Double Quote
- `#`: Hash (for comments)
- `\`: Backslash (for escaping characters)

#### Unused Characters
These are not used in Python and cause errors outside strings or comments.
- `$`: Dollar Sign
- `?`: Question Mark
- `` ` ``: Backtick

**Ellipsis Literal (`...`)**: Special use in Python, like slicing.

<br>

---