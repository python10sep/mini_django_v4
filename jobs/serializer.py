from rest_framework import serializers   # sub-module
from jobs.models import Portal, JobDescription, JobTitle


class PortalSerializer(serializers.Serializer):
    """
    Serlializer for `Portal`
    """

    name = serializers.CharField(
        required=True, max_length=250
    )
    description = serializers.CharField(max_length=250)

    def create(self, validated_data):
        return Portal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.save()
        return instance


class JobDescriptionSerializer(serializers.Serializer):
    """

    """

    role = serializers.CharField(max_length=250)
    description_text = serializers.CharField(max_length=250)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return JobDescription.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.role = validated_data.get("role", instance.role)
        instance.description_text = validated_data.get("description_text", instance.description_text)
        instance.pub_date = validated_data.get("pub_date", instance.pub_date)
        instance.save()
        return instance


class JobTitleSerializer(serializers.Serializer):
    """

    """

    title = serializers.CharField(max_length=250)
    last_updated = serializers.DateTimeField(required=True)
    job_description = JobDescriptionSerializer(required=True)
    portal = PortalSerializer(required=True)

    def create(self, validated_data):
        return JobTitle.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.last_update = validated_data.get("last_updated", instance.last_updated)
        instance.job_description = validated_data.get("job_description", instance.job_description)
        instance.portal = validated_data.get("portal", instance.portal)
        instance.save()
        return instance


# if __name__ == "__main__":
#     data = [{"name": "Prashant", "description": "foosfa"}, {"name": "Prashant", "description": 1}]
#     obj = PortalSerializer(data=data, many=True)
#     obj.is_valid()
#     data =

