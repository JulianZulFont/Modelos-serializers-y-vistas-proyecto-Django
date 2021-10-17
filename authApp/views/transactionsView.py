from django.conf import settings
from django.db.models import query
from django.http import request
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.account import Account
from authApp.models.transaction import Transaction
from authApp.serializers.transactionSerializer import TransactionSerializer


class TransactionsDetailView(generics.RetrieveAPIView):  
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)


class TransactionsAccountView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset (self):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Transaction.objects.filter(origin_account_id=self.kwargs['account'])
        return queryset


class TransactionsCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args:", args)
        print("KWArgs", kwargs)

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TransactionSerializer(
            data=request.data['transaction_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Transacción exitosa chafa", status=status.HTTP_201_CREATED)


class TransactionsUpdateView(generics.UpdateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def update(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)


class TransactionsDeleteView(generics.DestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Transaction.objects.all()

    def delete(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().delete(request, *args, **kwargs)
        
