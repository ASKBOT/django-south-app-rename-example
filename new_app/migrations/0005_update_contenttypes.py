# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.contenttypes.models import ContentType

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        content_types = ContentType.objects.filter(app_label='old_app')
        content_types.update(app_label='new_app')
    
    
    def backwards(self, orm):
        "Write your backwards methods here."
        content_types = ContentType.objects.filter(app_label='new_app')
        content_types.update(app_label='old_app')


    models = {
        'new_app.something': {
            'Meta': {'object_name': 'Something'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['new_app']
