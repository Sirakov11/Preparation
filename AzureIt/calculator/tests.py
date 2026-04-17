from django.test import TestCase
from django.urls import reverse


class CalculatorViewTests(TestCase):
    def test_get_request_renders_page(self):
        response = self.client.get(reverse("calculator"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "calculator/index.html")

    def test_post_addition_returns_result(self):
        response = self.client.post(
            reverse("calculator"),
            {
                "first": "5",
                "second": "3",
                "operation": "add",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["result"], 8.0)
        self.assertIsNone(response.context["error"])

    def test_post_divide_by_zero_returns_error(self):
        response = self.client.post(
            reverse("calculator"),
            {
                "first": "10",
                "second": "0",
                "operation": "divide",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["error"], "Cannot divide by zero.")
        self.assertIsNone(response.context["result"])
