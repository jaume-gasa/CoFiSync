"""Test just to check travis integration when real code appears this should be deleted."""
from unittest import TestCase


class BaseTest(TestCase):
    """Test to check everything is ok with travis integration."""

    def test_maths(self):
        """Check maths still work at the most basic level."""

        self.assertEqual(2, 1 + 1)
