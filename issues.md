
# Lab 5: Static Code Analysis - Issue Log

**Project:** Scholarship Disbursement  
**File:** `scholarship_disbursement.py`  
**Tools:** Pylint, Bandit, Flake8

## Issues Identified and Fixes Applied

| Issue | Type / Tool | Original Line(s) | Description | Fix Applied |
|---|---|---|---|---|
| SQL query string interpolation | Security - Bandit B608 | 10 | User values were inserted directly into an SQL query, creating a potential SQL injection vulnerability. | Replaced string interpolation with parameterized SQL queries using `?` placeholders. |
| Mutable default argument | Bug - Pylint W0102 | 9 | The default `audit=[]` list could be shared between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Shell command execution | Security - Bandit B605, B607 | 26 | `os.system()` launched a shell command unnecessarily. | Replaced shell execution with Python's `print()` function and removed the unused `os` import. |
| Broad exception handling | Quality - Pylint W0718, Bandit B110 | 27-28 | Catching all exceptions and ignoring them could hide errors. | Removed the unnecessary `try/except` block. |
| Global statement | Quality - Pylint W0603 | 15-16 | The `global` statement made the function depend on mutable global state. | Removed the global counter and calculated the disbursed total from the database. |
| Duplicate disbursement | Logic issue found during source review | 17-20 | An award could potentially be disbursed more than once. | Added a check for the existing `disbursed` status before returning the award amount. |
| Missing docstrings | Pylint C0114, C0116 | Multiple | The module and functions lacked documentation. | Added module and function docstrings. |
| Naming convention violations | Pylint C0103 | 6, 31 | Naming did not follow the expected Python naming conventions. | Removed the global total and renamed `bySchemeCount` to `by_scheme_count`. |
| Inconsistent return statements | Pylint R1710 | 15-20 | The function returned a value in one branch but implicitly returned `None` in another. | Added an explicit `return None` for unavailable or already-disbursed awards. |
| Incorrect None comparison | Pylint C0121, Flake8 E711 | 32 | The code used `== None` instead of an identity comparison. | Changed it to `scheme is None`. |
| Excessive line length | Pylint C0301, Flake8 E501 | Multiple | Several lines exceeded the configured line-length limits. | Split long statements and reformatted SQL queries. |
| Unnecessary string formatting | Pylint C0209 | 10 | The SQL statement used percent-based string formatting. | Replaced interpolation with parameterized SQL, addressing both the formatting warning and security concern. |

## Verification Results

- **Pylint before:** 5.00/10
- **Pylint after:** 10.00/10
- **Bandit before:** 1 medium-severity and 3 low-severity findings
- **Bandit after:** No issues identified
- **Flake8 before:** Multiple formatting violations
- **Flake8 after:** Empty report, indicating no reported violations
- **Runtime test:** Program executed successfully with the expected output.

### Program Output

```text
50000 None
1 50000
Archiving awards
```

## Conclusion

Static analysis helped identify potential security vulnerabilities, code-quality issues, naming violations, and formatting problems. The fixes improved readability, maintainability, and security while preserving the intended scholarship disbursement functionality.
