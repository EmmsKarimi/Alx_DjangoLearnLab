from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_notifications(request):
    notifications = request.user.notifications.filter(read=False).order_by('-timestamp')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
