# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('old_app_something', 'new_app_something')


    def backwards(self, orm):
        db.rename_table('new_app_something', 'old_app_something')


    models = {
        'new_app.something': {
            'Meta': {'object_name': 'Something'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['new_app']
