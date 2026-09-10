import unittest

from src.devops_course import project_summary


class ProjectSummaryTests(unittest.TestCase):
    def test_summary_mentions_devops(self) -> None:
        self.assertIn("DevOps", project_summary())


if __name__ == "__main__":
    unittest.main()
