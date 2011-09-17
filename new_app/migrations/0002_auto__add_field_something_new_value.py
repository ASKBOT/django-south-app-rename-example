# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from new_app.migration_utils import was_applied

class Migration(SchemaMigration):

    def forwards(self, orm):

        if was_applied(__file__, 'old_app'):
            return
        
        # Adding field 'Something.new_value'
        db.add_column('old_app_something', 'new_value', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Something.new_value'
        db.delete_column('old_app_something', 'new_value')


    models = {
        'old_app.something': {
            'Meta': {'object_name': 'Something'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_value': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['old_app']
