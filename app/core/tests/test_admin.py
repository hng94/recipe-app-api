from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@dev.com",
            password="123"
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="test@dev.com",
            password="123",
            name="test fullname"
        )

    def test_user_listed(self):
        # Test that list all users on user page
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    # def test_user_change_page(self):
    #     url = reverse("admin:core_user_change", args=[self.user.id])
    #     res = self.client.get(url)
    #
    #     self.assertEqual(res.status_code, 200)
