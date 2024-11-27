from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from storeroom.filters import MobileFilter
from storeroom.models import Mobile
from storeroom.permissions import IsAdminOrReadOnly
from storeroom.serializers import MobileSerializer


class MobileViewSet(ModelViewSet):

    """
    A ViewSet for managing Mobile objects.

    This ViewSet provides the following functionalities:
        - Standard CRUD operations (list, retrieve, create, update, delete).
        - Filtering, searching, and ordering of Mobile objects.
        - Custom action to retrieve mobiles where specific fields match (`equal_fields`).

    Permissions:
        - Allows read-only access to all users.
        - Write access is restricted to admin users.

    Filtering:
        - Custom filtering with `DjangoFilterBackend` using the `MobileFilter` class.
        - Supports ordering by `status` and `price`.
        - Enables searching by the `nationality` field.

    Endpoints:
        - **GET /mobiles/**: Retrieve a list of all Mobile objects, with optional filters.
        - **GET /mobiles/{id}/**: Retrieve details of a specific Mobile object.
        - **POST /mobiles/**: Create a new Mobile object (admin only).
        - **PUT /mobiles/{id}/**: Update an existing Mobile object (admin only).
        - **DELETE /mobiles/{id}/**: Delete a Mobile object (admin only).
        - **GET /mobiles/equal_fields/**: Retrieve Mobile objects where `nationality` equals `made_in`.

    Example Usage:
        - Retrieve mobiles where nationality equals made_in:
          `GET /mobiles/equal_fields/`
        - Search for mobiles by nationality:
          `GET /mobiles/?search=Japan`
        - Order mobiles by price:
          `GET /mobiles/?ordering=price`

    Attributes:
        serializer_class: The serializer used for serializing and deserializing Mobile objects.
        queryset: The base queryset used for retrieving Mobile objects.
        filter_backends: The filters enabled for this ViewSet.
        permission_classes: The permissions applied to this ViewSet.
    """

    serializer_class = MobileSerializer
    queryset = Mobile.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['status', 'price']
    search_fields = ['nationality']
    filterset_class = MobileFilter

    permission_classes = [IsAdminOrReadOnly]


    @action(detail=False, methods=['get'])
    def equal_fields(self, request):
        """
        Custom action to retrieve Mobile objects where `nationality` equals `made_in`.

        Filters the Mobile queryset to include only objects where the `nationality`
        field matches the `made_in` field. This is a read-only action and does not
        modify the data.

        Endpoint:
            - GET /mobiles/equal_fields/

        Returns:
            - HTTP 200 OK with a JSON response containing the list of matching Mobile objects.

        Example Response:
        [
            {
                "id": 1,
                "name": "Mobile A",
                "price": 500,
                "nationality": "USA",
                "made_in": "USA",
                "status": "available"
            },
            {
                "id": 2,
                "name": "Mobile B",
                "price": 800,
                "nationality": "Japan",
                "made_in": "Japan",
                "status": "available"
            }
        ]
        """
        queryset = self.queryset.filter(nationality=F('made_in'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

