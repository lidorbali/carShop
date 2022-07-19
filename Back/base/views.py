from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from . models import Car
# Create your views here.

def index(requset):
    return JsonResponse({"server":"alive"}, safe=False)


#login
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        #add custom claims
        
        
        token ['username']= user.username
        token ['email']= user.email
        
        #...
        return token
 

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



#regiser
@api_view(['POST'])
def register (request):
     User.objects.create_user(username=request.data['username'],password=request.data['password'],email=request.data['email'])
     return JsonResponse({'done':'test'}, safe=False)

@api_view(['GET'])#cant use GET
@permission_classes([IsAuthenticated]) #cant use if you not login
def test_members(request):
    return JsonResponse({'members':'only'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_car(request):
    print("username:",request.user)
    Car.objects.create(desc=request.data['desc'],company=request.data['company'],price=request.data['price'],user=request.user)
    return JsonResponse({'test':'done'}, safe=False)


@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def get_my_cars(request):
    
    user = request.user
    print(user.car_set.all())
    if request.method == "GET":
        res=[] #create an empty list
        for car in user.car_set.all(): #run on every row in the table...
         res.append({
            "company":car.company,
            "desc":car.desc,
            "price":car.price,
            "id":car._id}) #append row by to row to res list
        return JsonResponse(res,safe=False) #return array as json response
    
    if request.method == 'DELETE': #method delete a row
            Car.objects.get(_id=id).delete()
            return JsonResponse({'DELETE': id})

        
    

###  register --> login --> test (members only validtion) --> buy_car --> get_my_cars
    # user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # company=models.CharField(max_length=50,null=True,blank=True)
    # desc = models.CharField(max_length=50,null=True,blank=True)
    # price = models.DecimalField(max_digits=5,decimal_places=2)