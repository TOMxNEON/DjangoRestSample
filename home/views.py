from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer
from .models import Task


# Create your views here.

@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status' : 200,
            'message' : "Yes! It's Working!!!",
            'method_called' :'GET' 
        })
    elif request.method == 'POST':
        return Response({
            'status' : 200,
            'message' : "Yes! It's Working!!!",
            'method_called' :'POST' 
        })
    elif request.method == 'PATCH':
        return Response({
            'status' : 200,
            'message' : "Yes! It's Working!!!",
            'method_called' :'PATCH' 
        })
    else:
        return Response({
            'status' : 400,
            'message' : "Yes! It's Working!!!",
            'method_called' :'Invalid Method' 
        })
    

@api_view(['POST'])
def post_task(request):
    try:
        data = request.data
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Task added successfully',
                'data': serializer.data
            })
        return Response({
                'status': False,
                'message': 'Input all fields',
                'data': serializer.errors
            })

    except Exception as e :
        print(e)

    return Response({
        'status': False,
        'message': 'Something went wrong'
    })
    
@api_view(['GET'])
def get_tasks(request):
    task_objs = Task.objects.all()
    serializer = TaskSerializer(task_objs, many = True)

    return Response({
        'status': True,
        'message': 'tasks fetched',
        'data' : serializer.data
    })


@api_view(['PATCH'])
def patch_task(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
        obj = Task.objects.get(uid= data.get('uid'))
        serializer =  TaskSerializer(obj, data= data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Task added successfully',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'Invalid data',
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Invalid uid',
        'data': {}
    })

