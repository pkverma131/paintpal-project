from rest_framework import viewsets
from rest_framework.response import Response
from .models import YogaPath, Yogasana
from .serializers import YogaPathSerializer, YogasanaSerializer

class YogaPathViewSet(viewsets.ModelViewSet):
    queryset = YogaPath.objects.all()
    serializer_class = YogaPathSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Retrieve related Yogasana objects through the association model
        related_yogasanas = instance.yogasana_set.all()

        # Serialize the related Yogasana objects
        related_yogasanas_serializer = YogasanaSerializer(related_yogasanas, many=True)

        # Include the serialized related Yogasana objects in the response data
        response_data = serializer.data
        response_data['yogasanas'] = related_yogasanas_serializer.data

        return Response(response_data)

class YogasanaViewSet(viewsets.ModelViewSet):
    queryset = Yogasana.objects.all()
    serializer_class = YogasanaSerializer
