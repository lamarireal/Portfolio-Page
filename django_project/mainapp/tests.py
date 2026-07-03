from django.test import TestCase
from django.utils import timezone

from .models import ChronologyEntry, Project


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


class ProjectCardViewTests(TestCase):
    def test_index_renders_project_cards_with_detail_links(self):
        project = Project.objects.create(
            title="Sample project",
            description="A short project description.",
            tags="django, api",
            image="project_images/sample.png",
            pub_date=timezone.now(),
        )

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sample project')
        self.assertContains(response, 'django')
        self.assertContains(response, 'api')
        self.assertContains(response, f'/project/{project.pk}/?from=projects')

    def test_project_detail_page_renders_detail_layout(self):
        project = Project.objects.create(
            title="Detailed project",
            description="A detailed project description.",
            tags="python, django",
            image="project_images/sample.png",
            pub_date=timezone.now(),
        )

        response = self.client.get(f'/project/{project.pk}/?from=projects')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'project-detail-shell')
        self.assertContains(response, 'project-detail-stage')
        self.assertContains(response, 'Detailed project')
        self.assertContains(response, 'A detailed project description.')
        self.assertContains(response, 'Back to portfolio')
        self.assertContains(response, '/#projects')

    def test_project_detail_page_renders_description_only_once(self):
        project = Project.objects.create(
            title="Single description project",
            description="A single detailed description.",
            tags="python",
            image="project_images/sample.png",
            pub_date=timezone.now(),
        )

        response = self.client.get(f'/project/{project.pk}/?from=projects')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text.count('A single detailed description.'), 1)

    def test_project_detail_page_preserves_multiline_description(self):
        project = Project.objects.create(
            title="Styled project",
            description="First paragraph\n\nSecond paragraph",
            tags="python, django",
            image="project_images/sample.png",
            pub_date=timezone.now(),
        )

        response = self.client.get(f'/project/{project.pk}/?from=projects')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<p')
        self.assertContains(response, 'First paragraph')
        self.assertContains(response, 'Second paragraph')
