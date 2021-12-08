from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snacks

class TestSnackDetailView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.thing = Snacks.objects.create(
            title="Pizza", purchaser=self.user, description="pizza",
        )

    def test_string_representation(self):
        self.assertEqual(str(self.thing), "Pizza")

    def test_snack_content(self):
        self.assertEqual(f"{self.thing.title}", "Pizza")
        self.assertEqual(f"{self.thing.purchaser}", "tester")
        self.assertEqual(self.thing.description, "pizza")
    
    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pizza")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("create_snack"),
            {
                "title": "Pizza",
                "purchaser": self.user.id,
                "description": "pizza",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        

    
    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update_snack", args="1"),
            {"title": "Updated name","description":"new Pizza","purchaser":self.user.id}
        )
        print (response)
        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("delete_snack", args="1"))
        self.assertEqual(response.status_code, 200)