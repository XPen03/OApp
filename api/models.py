from django.db import models

# Create your models here.

class Picture(models.Model):
    #name = models.CharField(max_length=50)
    image = models.ImageField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    pill = models.CharField(max_length=20)
    matches = models.BooleanField
    def __str__(self):
        return self.name # has to be changed afterwards

    def update(self, instance, validated_data):
    # 更新的特别之处在于你已经获取到了这个对象instance
        instance.name = validated_data.get('name')
        instance.save()
        return instance