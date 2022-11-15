# from django.shortcuts import render
#
# # Create your views here.
# from django.shortcuts import render
# from .serializers import UserSerializer,RegisterSerializer
# from rest_framework.views import APIView
#
# from rest_framework.response import Response
#
# from rest_framework import permissions
# from rest_framework import generics
#
#
#
# # Create your views here.
#
#
#
# class RegisterAPI(generics.GenericAPIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = RegisterSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         # "token": AuthToken.objects.create(user)[1]
#         })




from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer
from rest_framework import response, status



class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


