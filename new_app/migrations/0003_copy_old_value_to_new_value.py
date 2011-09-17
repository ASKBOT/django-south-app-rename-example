# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for item in orm.Something.objects.all():
            item.new_value = int(item.value)
            item.save()


    def backwards(self, orm):
        "Write your backwards methods here."
        return


    models = {
        'old_app.something': {
            'Meta': {'object_name': 'Something'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['old_app']
