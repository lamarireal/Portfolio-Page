from django.test import TestCase
from django.utils import timezone

from .models import ChronologyEntry


class ChronologyEntryModelTests(TestCase):
    def test_create_entry_with_side_and_timestamp(self):
        entry = ChronologyEntry.objects.create(
            title="First milestone",
            date_label=timezone.now(),
            description="A major step in my journey.",
            side="right",
        )

        self.assertEqual(entry.side, "right")
        self.assertEqual(entry.date_label, entry.date_label)
