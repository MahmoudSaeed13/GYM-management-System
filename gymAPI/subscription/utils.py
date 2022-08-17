from datetime import date
from dateutil.relativedelta import relativedelta


def set_subscription_end_date(self):
    print(type(self.plan_id.duration_months))
    self.end_date = date.today() + relativedelta(months=self.plan_id.duration_months)
