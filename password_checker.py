"""
Password Strength Checker
SkillCraft Technology - Cybersecurity Internship - Task 3

Evaluates password strength based on:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters

Author: Hamsini
"""

import re


# Scoring weights for each criterion
CRITERIA = {
    "length_8":       ("At least 8 characters",           1),
    "length_12":      ("At least 12 characters",          1),
    "length_16":      ("At least 16 characters",          1),
    "has_upper":      ("Contains uppercase letters (A-Z)", 1),
    "has_lower":      ("Contains lowercase letters (a-z)", 1),
    "has_digit":      ("Contains digits (0-9)",            1),
    "has_special":    ("Contains special characters (!@#...)", 2),
    "no_spaces":      ("No spaces",                        1),
}

SPECIAL_CHARS = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]"


def evaluate_password(password):
    """
    Evaluates a password and returns a detailed strength report.

    Args:
        password (str): The password to evaluate.

    Returns:
        dict: Contains score, max_score, strength label, and passed/failed criteria.
    """
    results = {}
    score = 0
    max_score = sum(w for _, w in CRITERIA.values())

    # Length checks
    results["length_8"]   = len(password) >= 8
    results["length_12"]  = len(password) >= 12
    results["length_16"]  = len(password) >= 16

    # Character type checks
    results["has_upper"]   = bool(re.search(r"[A-Z]", password))
    results["has_lower"]   = bool(re.search(r"[a-z]", password))
    results["has_digit"]   = bool(re.search(r"\d", password))
    results["has_special"] = bool(re.search(SPECIAL_CHARS, password))
    results["no_spaces"]   = " " not in password

    # Calculate score
    for key, passed in results.items():
        if passed:
            score += CRITERIA[key][1]

    # Determine strength label
    percentage = (score / max_score) * 100
    if percentage <= 30:
        strength = "Very Weak"
    elif percentage <= 50:
        strength = "Weak"
    elif percentage <= 70:
        strength = "Moderate"
    elif percentage <= 85:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "max_score": max_score,
        "percentage": round(percentage, 1),
        "strength": strength,
        "criteria_results": results,
    }


def display_report(password, report):
    """
    Prints a formatted strength report to the console.
    """
    print("\n" + "=" * 50)
    print("   PASSWORD STRENGTH REPORT")
    print("=" * 50)
    print(f"Password  : {'*' * len(password)}")
    print(f"Length    : {len(password)} character(s)")
    print(f"Score     : {report['score']} / {report['max_score']}")
    print(f"Strength  : {report['strength']}  ({report['percentage']}%)")
    print("\n[+] Criteria Breakdown:")
    print("-" * 50)

    for key, passed in report["criteria_results"].items():
        label = CRITERIA[key][0]
        status = "PASS" if passed else "FAIL"
        icon = "[+]" if passed else "[-]"
        print(f"  {icon} {label:<45} {status}")

    print("-" * 50)

    # Give suggestions if not Very Strong
    if report["strength"] != "Very Strong":
        print("\n[*] Tips to improve your password:")
        if not report["criteria_results"]["length_12"]:
            print("  - Use at least 12 characters.")
        if not report["criteria_results"]["has_upper"]:
            print("  - Add uppercase letters (A-Z).")
        if not report["criteria_results"]["has_lower"]:
            print("  - Add lowercase letters (a-z).")
        if not report["criteria_results"]["has_digit"]:
            print("  - Include at least one number.")
        if not report["criteria_results"]["has_special"]:
            print("  - Add special characters like !@#$%^&*.")
        if not report["criteria_results"]["no_spaces"]:
            print("  - Avoid spaces in your password.")


def main():
    print("\n" + "=" * 50)
    print("   PASSWORD STRENGTH CHECKER - SCT_CS_3")
    print("   SkillCraft Cybersecurity Internship")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Check password strength")
        print("  2. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            # Use getpass in real use — using input() here for demo purposes
            password = input("Enter password to check: ")
            if not password:
                print("[!] Password cannot be empty.")
                continue
            report = evaluate_password(password)
            display_report(password, report)

        elif choice == "2":
            print("\nExiting Password Strength Checker. Goodbye!")
            break

        else:
            print("[!] Invalid option. Try again.")


if __name__ == "__main__":
    main()
