# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Service'
        db.create_table('people_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='services', to=orm['auth.User'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='users', to=orm['people.ServiceType'])),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('people', ['Service'])

        # Adding model 'ServiceType'
        db.create_table('people_servicetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('username_url', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('people', ['ServiceType'])

        # Deleting field 'HackerProfile.tumblr_username'
        db.delete_column('people_hackerprofile', 'tumblr_username')

        # Deleting field 'HackerProfile.facebook_username'
        db.delete_column('people_hackerprofile', 'facebook_username')

        # Deleting field 'HackerProfile.twitter_username'
        db.delete_column('people_hackerprofile', 'twitter_username')


    def backwards(self, orm):
        
        # Deleting model 'Service'
        db.delete_table('people_service')

        # Deleting model 'ServiceType'
        db.delete_table('people_servicetype')

        # Adding field 'HackerProfile.tumblr_username'
        db.add_column('people_hackerprofile', 'tumblr_username', self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True), keep_default=False)

        # Adding field 'HackerProfile.facebook_username'
        db.add_column('people_hackerprofile', 'facebook_username', self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True), keep_default=False)

        # Adding field 'HackerProfile.twitter_username'
        db.add_column('people_hackerprofile', 'twitter_username', self.gf('django.db.models.fields.CharField')(default='', max_length=64, blank=True), keep_default=False)


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.hackerprofile': {
            'Meta': {'object_name': 'HackerProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preferred_contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'people.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'users'", 'to': "orm['people.ServiceType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'to': "orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'people.servicetype': {
            'Meta': {'object_name': 'ServiceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username_url': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['people']
