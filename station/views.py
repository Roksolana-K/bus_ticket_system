from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from station.models import Bus
from station.serializers import BusSerializer


class BusListView(generics.GenericAPIView,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin):

    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def get(self, request, *args, **kwargs) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) -> Response:
        return self.create(request, *args, **kwargs)

class BusDetailView(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    def retrieve(self, request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs) -> Response:
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs) -> Response:
        return self.destroy(request, *args, **kwargs)
