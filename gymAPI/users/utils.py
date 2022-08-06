# function to calculate BMI for users    
from decimal import Decimal

def set_BMI(instance):
    bmi_value = instance.weight / Decimal(((instance.height / 100)**2))
    instance.bmi = bmi_value
