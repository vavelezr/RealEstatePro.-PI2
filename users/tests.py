from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class UserAuthTests(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.login_url = reverse("login")
        self.signup_url = reverse("register")

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_login_view_post_success(self):
        response = self.client.post(
            self.login_url, {"username": self.username, "password": self.password}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_login_view_post_failure(self):
        response = self.client.post(
            self.login_url, {"username": self.username, "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, "form", None, "Please enter a correct username and password."
        )

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_signup_view_post_success(self):
        response = self.client.post(
            self.signup_url,
            {
                "username": "newuser",
                "password1": "newpassword",
                "password2": "newpassword",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_signup_view_post_failure(self):
        response = self.client.post(
            self.signup_url,
            {
                "username": "newuser",
                "password1": "newpassword",
                "password2": "differentpassword",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, "form", "password2", "Las dos contraseñas no coinciden."
        )
