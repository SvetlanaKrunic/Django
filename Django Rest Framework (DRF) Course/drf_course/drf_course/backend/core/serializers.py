from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):
	#u django models zovemo ga title description ali ovde yelimo da ga yovemo name
	#required=True ocekujemo od klijenta ako ne dobijemo dobijamo 404 message
	name = CharField(source="title", required=True)
	message = CharField(source="description", required=True)
	email = EmailField(required=True)
	
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)