#coding: utf-8

from rest_framework import serializers

from .models import User, Entry

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    # author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('id', 'body', 'author', 'created_at', 'parent_id', 'score')
