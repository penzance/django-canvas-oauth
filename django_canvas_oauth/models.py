from django.db import models

class CustomModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def update(self, **kwargs):
        """ Helper method to update objects """
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
        self.save()


class OAuthUser(CustomModel):
    course_id = models.CharField(max_length=128, db_index=True)
    admin_id = models.CharField(max_length=128, db_index=True)
    
    class Meta:
        unique_together = (('course_id', 'admin_id'),)

class OAuthToken(CustomModel):
    token = models.CharField(max_length=128) #oauth_middleware token has length 64
    admin = models.ForeignKey(OAuthUser)
