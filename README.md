# Password Strength Checker

## Overview

This project is a Python-based Password Strength Checker developed to evaluate the security level of user passwords based on multiple criteria.

The tool analyzes passwords using factors such as length, uppercase and lowercase letters, digits, special characters, and spacing rules. Based on these checks, it calculates a score and classifies the password strength from **Very Weak** to **Very Strong**.

This project demonstrates fundamental cybersecurity concepts related to authentication security and secure password practices.

## Features

* Password strength evaluation
* Detailed criteria-based analysis
* Strength classification (Very Weak to Very Strong)
* Password scoring system
* Improvement suggestions for weak passwords
* Input validation for safe execution
* User-friendly menu-driven interface

## Cybersecurity Concepts Demonstrated

### Password Security

Strong passwords are essential for protecting user accounts and sensitive information from unauthorized access.

This tool evaluates password complexity using industry-recommended practices.

### Authentication Security

Passwords serve as the first line of defense in authentication systems. Weak passwords increase the risk of unauthorized access.

The checker helps users create stronger and more secure credentials.

### Secure Password Policies

The application enforces common password security requirements, including:

* Minimum length requirements
* Use of uppercase and lowercase letters
* Inclusion of numeric digits
* Use of special characters
* Avoidance of spaces

### Input Validation

The program validates user input to ensure:

* Password fields are not empty
* Menu choices are valid

This improves application reliability and prevents runtime errors.

## Evaluation Criteria

The password is assessed using the following rules:

| Criteria           | Description                             |
| ------------------ | --------------------------------------- |
| Length ≥ 8         | Basic minimum password length           |
| Length ≥ 12        | Recommended secure length               |
| Length ≥ 16        | Highly secure password length           |
| Uppercase Letters  | Contains at least one A-Z character     |
| Lowercase Letters  | Contains at least one a-z character     |
| Digits             | Contains at least one numeric character |
| Special Characters | Contains symbols such as !@#$%^&*       |
| No Spaces          | Ensures passwords do not contain spaces |

## Strength Levels

Based on the final score, passwords are categorized as:

| Percentage Score | Strength Level |
| ---------------- | -------------- |
| 0% - 30%         | Very Weak      |
| 31% - 50%        | Weak           |
| 51% - 70%        | Moderate       |
| 71% - 85%        | Strong         |
| Above 85%        | Very Strong    |

## How the Scoring Works

Each security criterion contributes a specific score.

Example:

```text
Uppercase Present     → +1 point
Lowercase Present     → +1 point
Digit Present         → +1 point
Special Character     → +2 points
```

The total score is converted into a percentage and mapped to a strength category.

## Example Output

```text
==================================================
   PASSWORD STRENGTH REPORT
==================================================
Password  : ************
Length    : 12 character(s)
Score     : 8 / 9
Strength  : Strong (88.9%)

[+] Criteria Breakdown:
--------------------------------------------------
[+] At least 8 characters                 PASS
[+] At least 12 characters                PASS
[-] At least 16 characters                FAIL
[+] Contains uppercase letters (A-Z)     PASS
[+] Contains lowercase letters (a-z)     PASS
[+] Contains digits (0-9)                PASS
[+] Contains special characters          PASS
[+] No spaces                            PASS
--------------------------------------------------
```

## Requirements

* Python 3.x
* Built-in Python modules:

  * `re` (Regular Expressions)

No external libraries are required.
