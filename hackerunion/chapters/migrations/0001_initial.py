# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Chapter'
        db.create_table('chapters_chapter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subdomain', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('chapters', ['Chapter'])


    def backwards(self, orm):
        
        # Deleting model 'Chapter'
        db.delete_table('chapters_chapter')


    models = {
        'chapters.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'subdomain': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['chapters']
