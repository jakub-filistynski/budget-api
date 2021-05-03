from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.budgets.factories import BudgetFactory
from apps.budgets.models import Budget
from apps.users.factories import UserFactory


class TestBudgetViewSet(APITestCase):
    LIST_USER_BUDGETS_URL = "/api/budgets/"
    LIST_USER_BUDGETS_REVERSE = "budget-list"

    @classmethod
    def setUpTestData(self):
        self.user = UserFactory.create()

    def test_urls(self):
        self.assertEquals(
            self.LIST_USER_BUDGETS_URL,
            reverse(self.LIST_USER_BUDGETS_REVERSE),
        )

    def test_budgets_list(self):
        user_one_budget = UserFactory.create()
        user_two_budgets = UserFactory.create()

        budget = BudgetFactory.create(owner=user_one_budget)
        budget.members.add(user_two_budgets)
        BudgetFactory.create(owner=user_two_budgets)

        keys = ["id", "name", "owner", "is_owner"]

        response = self.client.get(reverse(self.LIST_USER_BUDGETS_REVERSE))
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username=user_one_budget.username, password="password")
        response = self.client.get(reverse(self.LIST_USER_BUDGETS_REVERSE))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        results = response.data["results"]

        self.assertEquals(len(results), 1)
        for key in keys:
            self.assertTrue(key in results[0])

        self.client.logout()

        self.client.login(username=user_two_budgets.username, password="password")
        response = self.client.get(reverse(self.LIST_USER_BUDGETS_REVERSE))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        results = response.data["results"]

        self.assertEquals(len(results), 2)

    def test_budget_create(self):
        body = {}
        keys = ["name", "income_categories", "outcome_categories"]

        response = self.client.post(reverse(self.LIST_USER_BUDGETS_REVERSE), body)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.client.login(username=self.user.username, password="password")

        response = self.client.post(reverse(self.LIST_USER_BUDGETS_REVERSE), body)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        for key in keys:
            self.assertTrue(key in response.data)

        body = {"name": "", "income_categories": [], "outcome_categories": [""]}

        response = self.client.post(reverse(self.LIST_USER_BUDGETS_REVERSE), body)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        for key in keys:
            self.assertTrue(key in response.data)

        body = {
            "name": "Budget test",
            "income_categories": ["Income 1", "Income 2"],
            "outcome_categories": ["Outcome 1", "Outcome 2"],
        }
        budget_count_before = Budget.objects.count()
        response = self.client.post(reverse(self.LIST_USER_BUDGETS_REVERSE), body)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(budget_count_before < Budget.objects.count())
