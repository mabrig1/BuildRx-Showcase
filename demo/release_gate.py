"""Standalone synthetic release gate; not BuildRx production code."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    tests_passed: bool = False
    review_approved: bool = False
    security_checked: bool = False


def release_allowed(evidence: Evidence) -> bool:
    """Fail closed unless each required signal is explicitly True."""
    return all(value is True for value in (
        evidence.tests_passed, evidence.review_approved,
        evidence.security_checked,
    ))


if __name__ == "__main__":
    print("Release permitted:", release_allowed(Evidence(True, True, True)))
