
"""Manage scholarship awards, disbursements, and scheme counts."""

import sqlite3

CONN = sqlite3.connect(":memory:")
CONN.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER
    )
    """
)


def grant(student, scheme, amount, audit=None):
    """Create a scholarship award and record the student in the audit list."""
    if audit is None:
        audit = []

    CONN.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, 0)
        """,
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse an award once and return its amount, or None if unavailable."""
    row = CONN.execute(
        "SELECT amount, disbursed FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row is None or row[1]:
        return None

    CONN.execute(
        "UPDATE awards SET disbursed = 1 WHERE id = ?",
        (award_id,),
    )
    return row[0]


def archive():
    """Display an archive status message."""
    print("Archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scheme, or zero for None."""
    if scheme is None:
        return 0

    return CONN.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Demonstrate scholarship grants, disbursement, and reporting."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)

    print(disburse(1), disburse(9))

    disbursed_total = CONN.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM awards WHERE disbursed = 1"
    ).fetchone()[0]

    print(by_scheme_count("Merit"), disbursed_total)
    archive()


if __name__ == "__main__":
    main()
