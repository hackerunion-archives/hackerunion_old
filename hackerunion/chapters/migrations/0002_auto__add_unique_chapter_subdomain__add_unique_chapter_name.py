# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'Chapter', fields ['subdomain']
        db.create_unique('chapters_chapter', ['subdomain'])

        # Adding unique constraint on 'Chapter', fields ['name']
        db.create_unique('chapters_chapter', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Chapter', fields ['name']
        db.delete_unique('chapters_chapter', ['name'])

        # Removing unique constraint on 'Chapter', fields ['subdomain']
        db.delete_unique('chapters_chapter', ['subdomain'])


    models = {
        'chapters.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'subdomain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        }
    }

    complete_apps = ['chapters']
