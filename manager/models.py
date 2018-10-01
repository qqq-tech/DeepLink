from django.db import models

# Create your models here.

class Model_Link_Detail(models.Model):
  class Meta:
    unique_together = (('link_name','model_name','running_seq'))
  link_name= models.CharField(max_length=100)
  model_name= models.CharField(max_length=100)
  running_seq= models.IntegerField(default=0)

class Model_Link_Master(models.Model):
  link_name= models.CharField(primary_key=True, max_length=100)
  description= models.CharField(max_length=100,null=True)

  def __str__(self):
    return self.model_name+":"+ self.module_name

class Model_Master(models.Model):
  class Meta:
    unique_together = (('model_name', 'module_path'))
  model_name= models.CharField(max_length=100)
  module_path= models.CharField(max_length=300)
  module_function= models.CharField(max_length=100,null=True)
  module_input= models.CharField(max_length=100,null=True)
  module_output= models.CharField(max_length=100,null=True)
  select_pre_module_output= models.CharField(max_length=100,null=True)
  using_pre_prediction= models.BooleanField(default=False)
  pre_process_group= models.CharField(max_length=100,null=True)
  pre_process_name= models.CharField(max_length=100,null=True)
  pre_process_argument_json= models.TextField(default="")
  post_process_group= models.CharField(max_length=100,null=True)
  post_process_name= models.CharField(max_length=100,null=True)
  post_process_argument_json= models.TextField(default="")
  description= models.CharField(max_length=100,null=True)

  def __str__(self):
    return self.model_name+":"+ self.module_name



class Util_Mgmt(models.Model):
  class Meta:
    unique_together = (('group_name', 'process_name'))
  group_name= models.CharField(max_length=100)
  process_name= models.CharField(max_length=100)
  module_path= models.CharField(max_length=300,null=True)
  module_function= models.CharField(max_length=100,null=True)
  argument_json= models.TextField(default="")

  def __str__(self):
    return self.group_name+":"+ self.process_name
