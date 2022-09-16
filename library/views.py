from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Book, Track, Note, CustomUser
from .serializers import BookSerializer, TrackSerializer, NoteSerializer
from .permissions import IsOwnerOrReadOnly


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TrackList(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class TrackListCreate(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user, book=self.kwargs['book_pk'])

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs['book_pk'])
        serializer.save(user=self.request.user, book=book)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'tracks': reverse('track-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format),
    })
