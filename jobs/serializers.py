from rest_framework import serializers
from jobs.models import JobTitle, JobDescription, Portal


class PortalSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=250)
    description = serializers.CharField(required=False, max_length=250)

    def create(self, validated_data):
        """
        Create and return a new `Portal` instance, given the validated data.
        """
        return Portal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Portal` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class JobDescriptionSerializer(serializers.Serializer):
    role = serializers.CharField(required=False, max_length=250)
    description_text = serializers.CharField(required=False, max_length=250)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `JobDescription` instance, given the validated data.
        """
        return JobDescription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `JobDescription` instance, given the validated data.
        """
        instance.role = validated_data.get('role', instance.name)
        instance.description_text = validated_data.get('description_text', instance.description_text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        return instance


class JobTitleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=250)
    last_updated = serializers.DateTimeField()
    job_description = JobDescriptionSerializer(required=True)
    portal = PortalSerializer(required=True)

    def create(self, validated_data):
        """
        Create and return a new `JobTitle` instance,
        given the validated data.
        """
        return JobTitle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `JobTitle` instance,
        given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.last_updated = validated_data.get(
            'last_updated', instance.last_updated
        )
        instance.job_description = validated_data.get(
            'job_description', instance.job_description
        )
        instance.portal = validated_data.get('portal', instance.portal)
        instance.save()
        return instance
