import itertools
import unittest
from release_gate import Evidence, release_allowed

class ReleaseGateTests(unittest.TestCase):
    def test_all_boolean_combinations(self):
        for signals in itertools.product((False, True), repeat=3):
            with self.subTest(signals=signals):
                self.assertEqual(release_allowed(Evidence(*signals)), all(signals))

    def test_default_denies(self):
        self.assertFalse(release_allowed(Evidence()))

    def test_non_boolean_denies(self):
        self.assertFalse(release_allowed(Evidence(1, True, True)))

if __name__ == "__main__":
    unittest.main()
