'''radius_of_circle=int(input("Enter the radius of circle"))
Xc,Yc=map(int,input("Enter coordinates of centre").split(','))
print(Xc)
print(Yc)
c=(Xc,Yc)
print("coorinates of centre of circle are:",c)
Xp,Yp=map(int,input("Enter coordinates of point").split(','))
d=(Xp,Yp)
print("coordinates of point are:",d)
e=(Xc-Xp)**2+(Yc-Yp)**2
sqrt=pow( e,0.5)
print(sqrt)
if sqrt>radius_of_circle:
    print("point",d,"is outside circle")
elif sqrt<radius_of_circle:
    print("point",d,"is inside circle")
elif sqrt==radius_of_circle:
    print("point",d,"is on the circle")'''

#Using import
import math
radius_of_circle=int(input("Enter the radius of circle"))
Xc,Yc=map(int,input("Enter coordinates of centre").split(','))
print(Xc)
print(Yc)
c=(Xc,Yc)
print("coorinates of centre of circle are:",c)
Xp,Yp=map(int,input("Enter coordinates of point").split(','))
d=(Xp,Yp)
print("coordinates of point are:",d)
e=(Xc-Xp)**2+(Yc-Yp)**2
h=math.sqrt(e)
print(h)
if h>radius_of_circle:
    print("point",d,"is outside circle")
elif h<radius_of_circle:
    print("point",d,"is inside circle")
elif h==radius_of_circle:
    print("point",d,"is on the circle")
    


