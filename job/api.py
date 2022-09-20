## views
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def jobListApi(request):
    all_jobs = Job.objects.all()
    data= JobSerializer(all_jobs,many=True).data
    return Response({"data":data})

@api_view(['GET'])
def jobDetail(request,id):
    job = Job.objects.get(id=id)
    data= JobSerializer(job).data
    return Response({"data":data})

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'
