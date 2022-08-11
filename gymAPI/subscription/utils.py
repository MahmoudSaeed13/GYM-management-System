from datetime import date
from dateutil.relativedelta import relativedelta


def set_subscription_end_date(self):
    self.end_date = self.start_date + relativedelta(months=self.plan_id["duration_months"])
