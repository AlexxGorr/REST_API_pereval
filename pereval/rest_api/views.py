from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import PerevalAdded, PerevalAreas, PerevalCoords, PerevalImages
from .serializers import AddedSerializer, AreasSerializer, CoordsSerializer, ImagesSerializer, AddedUpdateSerializer


class AreasViewSet(ModelViewSet):
    queryset = PerevalAreas.objects.all()
    serializer_class = AreasSerializer


class CoordsViewSet(ModelViewSet):
    queryset = PerevalCoords.objects.all()
    serializer_class = CoordsSerializer


class AddedViewSet(ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = AddedSerializer


class ImagesViewSet(ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = ImagesSerializer


class AddedUpdate(UpdateAPIView):
    queryset = PerevalAdded.objects.all().prefetch_related('user', 'areas', 'coords')
    serializer_class = AddedUpdateSerializer


class AddedListView(ListAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = AddedSerializer

    def get_queryset(self):
        email = self.kwargs['email']
        return PerevalAdded.objects.filter(user_tourist__email=email)














