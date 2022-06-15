import pytest
from django.test import RequestFactory
from django.urls import reverse
from IssLocation import views


class TestISSView:
    def test_ISSlocation(self):
        req = RequestFactory().get(reverse("ISSlocation"))
        resp = views.ISSlocation(req)
        assert resp.status_code == 200

    def test_humanInSpace(self):
        req = RequestFactory().get(reverse("humanInSpace"))
        resp = views.humanInSpace(req)
        assert resp.status_code == 200
