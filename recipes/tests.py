from django.test import TestCase
from recipes.models import MealPlan
from django.contrib.auth.models import User

from freezegun import freeze_time
from datetime import tzinfo, datetime
import pytz

# Create your tests here.
class MealPlanTestCase(TestCase):

  # TODO figure out how to reference this constant more Pythonicly
  @freeze_time("1955-11-12", tz_offset=0)
  def test_meal_plan_created_at(self):
    # TODO figure out how to create this object only once.
    john = User.objects.create_user(username='testuser', password='12345')
    mealplan = MealPlan.objects.create(owner=john, title="Great Meal Plan")
    self.assertEqual(mealplan.created_at, datetime(1955,11,12, tzinfo=pytz.UTC))

  def test_meal_plan_modified_at(self):
    john = User.objects.create_user(username='testuser', password='12345')
    with freeze_time("1955-11-12", tz_offset=0):
      mealplan = MealPlan.objects.create(owner=john, title="Great Meal Plan")
    with freeze_time("1966-12-10", tz_offset=0):
      mealplan.title = "A whole new title"
      mealplan.save()
    self.assertEqual(mealplan.created_at, datetime(1955,11,12, tzinfo=pytz.UTC))
    self.assertEqual(mealplan.modified_at, datetime(1966,12,10, tzinfo=pytz.UTC))
