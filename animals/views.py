# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from .models import Animal
from .serializers import AnimalSerializer


class AnimalView(APIView):
    def post(self, request: Request):
        serializer = AnimalSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request: Request, animal_id: int):
        try:
            animal = Animal.objects.get(pk=animal_id)
        except Animal.DoesNotExist:
            return Response({"message": "Animal not found"}, status=status.HTTP_404_NOT_FOUND)
        # animal = get_object_or_404(Animal, pk=animal_id)

        serializer = AnimalSerializer(animal, request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except KeyError as err:
            return Response(
                {"message": err.args[0]},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, _, animal_id: int=None):
        if animal_id:
            # animal = get_object_or_404(Animal, pk=animal_id)
            try:
                animal = Animal.objects.get(pk=animal_id)
            except Animal.DoesNotExist:
                return Response({"message": "Animal not found"}, status=status.HTTP_404_NOT_FOUND)

            serializer = AnimalSerializer(animal)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # print(_.headers)
        animals = Animal.objects.all()

        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)

    def delete(self, request, animal_id):
        try:
            animal = Animal.objects.get(pk=animal_id)
        except Animal.DoesNotExist:
            return Response({"message": "Animal not found"}, status=status.HTTP_404_NOT_FOUND)
        animal.delete()

        return Response('', status=status.HTTP_204_NO_CONTENT)