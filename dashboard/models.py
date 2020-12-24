from django.db import models
from django.contrib.auth.models import User
from time import sleep
# from timezone_field import TimeZoneField 


STATUS=((0,'Deactive'),(1,'Active'))
POLICY_TYPES=(
(0,"jan_dhan_yojna"),
(1,"jivan_bima"),
(2,"jivan_laabh"),

    )
# POLICY_TYPES=(
# (0,"jan_dhan_yojna"),
# (1,"jivan_bima"),
# (2,"jivan_laabh"),
# (3,"Lic's New Endowment Plan"),
# (4,"Lic's New Jeevan Anand"),
# (5,"Lic's New Bima Bachat"),
# (6,"Lic's Single Premium Endowment Plan"),
# (7,"LIC's Jeevan Lakshya"),
# (8,"Lic's Jeevan Labh"),
# (9,"LIC's Aadhaar Stambh"),
# (10,"LIC's Aadhaar Shila"),
# (11,"LICs Jeevan Umang"),
# (12,"LIC's NEW MONEY BACK PLAN - 20 YEARS"),
# (13,"LIC’s NEW MONEY BACK PLAN - 25 YEARS"),
# (14,"LICs Jeevan Umang"),
# (15,"LIC's NEW CHILDREN'S MONEY BACK PLAN"),
# (16,"LIC's Jeevan Tarun"),
# (17,"LIC's Jeevan Shiromani"),
# (18,"LIC's Bima Shree"),
# (19,"LIC's TECH TERM"),
# (20,"LIC's Jeevan Amar"),
# (21,"LIC's Linked Accidental Death Benefit Rider"),
# (22,"Pradhan Mantri Vaya Vandana Yojana "),
# (23,"LIC's Jeevan Akshay - VII"),
# (24,"LIC's New Jeevan Shanti"),
# (25,"LIC's NIVESH PLUS"),
# (26,"LIC's SIIP"),
# (27,"LIC's NEW ENDOWMENT PLUS"),
# (28,"LIC's Bhagya Lakshmi"),
# (29,"LICs New Jeevan Mangal"),
# (30,"LIC’s Micro Bachat Plan"),
# (31,"FAQ's under LIC's Health Protection Plus"),
# (32,"LIC's JEEVAN AROGYA"),
# (33,"LIC's Cancer Cover")
#     )

class Lic(models.Model):    
    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    dob=models.DateField(max_length=50)
    contact=models.IntegerField()
    address=models.CharField(max_length=100)
    policy_type=models.IntegerField(choices=POLICY_TYPES,null=False)
    policy_number=models.CharField(unique=True,null=False,max_length=10)
    premium=models.IntegerField()
    sum_assured=models.IntegerField()
    year_of_policy=models.IntegerField()
    beneficiary_name=models.CharField(max_length=50)
    created_on=models.DateField()
    renew_date=models.DateField()
    status=models.IntegerField(choices=STATUS,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
    	return self.name

    

       


