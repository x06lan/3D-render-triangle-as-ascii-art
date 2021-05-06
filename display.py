import math
import time
import numpy as np

#  0-8


class point():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
    def __str__(self):
        return str(self.x)+" ,"+str(self.y)+" ,"+str(self.z)

    def set(self, inx:float, iny:float, inz:float):
        self.x = inx
        self.y = iny
        self.z = inz
        return self

def get_len(inpoint):
    s=inpoint.x**2+inpoint.y**2+inpoint.z**2
    s=s**0.5
    return s
def get_cos(v1,v2):
    x=v1.x*v2.x
    y=v1.y*v2.y
    z=v1.z*v2.z
    return  x+y+z

def hair(interface):
    
    in_p0 = interface[0]
    in_p1 = interface[1]
    in_p2 = interface[2]
    
    a=(in_p1.y-in_p0.y)*(in_p2.z-in_p0.z)-(in_p2.y-in_p0.y)*(in_p1.z-in_p0.z)
    b=(in_p1.z-in_p0.z)*(in_p2.x-in_p0.x)-(in_p2.z-in_p0.z)*(in_p1.x-in_p0.x)
    c=(in_p1.x-in_p0.x)*(in_p2.y-in_p0.y)-(in_p2.x-in_p0.x)*(in_p1.y-in_p0.y)

    return [a,b,c]


def face_and_line(inface, inline):
    p0 = inface[0]
    p1 = inface[1]
    p2 = inface[2]

    pa = inline[0]
    pb = inline[1]

    diff = np.array([[pa.x-pb.x, p1.x-p0.x, p2.x-p0.x],
                     [pa.y-pb.y, p1.y-p0.y, p2.y-p0.y],
                     [pa.z-pb.z, p1.z-p0.z, p2.z-p0.z],
                     ])
    line_ab = np.array([[pa.x-p0.x],
                        [pa.y-p0.y],
                        [pa.z-p0.z]
                        ])
    try:
        # 反矩陣
        g = np.linalg.inv(diff)
        
        m0 = np.array([[g[0][0], g[1][0], g[2][0]]])
        m1 = np.array([[g[0][1], g[1][1], g[2][1]]])
        m2 = np.array([[g[0][2], g[1][2], g[2][2]]])

        t = m0*line_ab[0][0]+m1*line_ab[1][0]+m2*line_ab[2][0]
        outx=(pa.x+t[0][0]*(pb.x-pa.x))
        outy=(pa.y+t[0][0]*(pb.y-pa.y))
        outz=(pa.z+t[0][0]*(pb.z-pa.z))

        out_point= [outx,outy,outz]
    except :
        return [False,"erorr"]

    if (t[0][1]+ t[0][2])<=1 and t[0][1]>=0 and t[0][2]>=0 :


        return [True,out_point]
    else:
        return [False,out_point ]


def camera(start_point,insize,point_size):
    all_line=[]
    s=start_point.x**2+start_point.y**2
    s=s**0.5
    for  z in range(0,insize[1]):


        for xy in range(0,insize[0]):
            px=point_size*start_point.y/s*(xy-insize[0]/2)
            py=point_size*start_point.x/s*(xy-insize[0]/2)
            pz=point_size*(-z+insize[1]/2)
            pl= point().set(start_point.x*0.5+px ,start_point.y*0.5+py ,start_point.z+pz)

            all_line.append(pl)
            pass
        pass
    return all_line




# p1 =point().set(0, -1, 0)
# p2 =point().set(-1, 0, 0)
# p3 =point().set(1, 1, 0)

p1 =point().set(0, 5, 0)
p2 =point().set(0, 0, -5)
p3 =point().set(0, -5, 5)
pa =point().set(0, 5, -10)

p4 = point().set(3, 2, -1)
p5 = point().set(1, 2, 1)

face = [p1, p2, p3]
aface=[p1,p2,pa]
line = [p4, p5]



# text_light=[".",":","-",'=','+','*',"#","%","@"]
text_light=[" ",".",":","-",'=','+','*',"#","%","@"]


size=[100,20]
k=0
r=100
fast=100
while  True:
    print(k)
    f = open("out.txt", "w")

    output=""

    start_point=point().set(r*math.cos(k*math.pi/fast),r*math.sin(k*math.pi/fast),0)

    k=k+1
    all_line=camera(start_point,size,0.5)
    # all_face=[face,aface]
    all_face=[face]


    for i in range(0 ,len(all_line)) :
        for j in range(0 , len(all_face)):
            if i%size[0]==0:
                output+="\n"
            lines=[all_line[i],start_point]
            v2=point().set(0,0,0)
            v2.x=all_line[i].x-start_point.x
            v2.y=all_line[i].y-start_point.y
            v2.z=all_line[i].z-start_point.z

            # print(line)

            data=face_and_line(all_face[j], lines)
        
            # print(data)
            if data[0]:
                # print(all_face[j])
                # print(data[1])
                v1=hair(all_face[j])
                v1=point().set(v1[0],v1[1],v1[2])
                dcos=get_cos(v1,v2)/get_len(v1)/get_len(v2)
                # print(dcos)
                light_and_dark=dcos/(1/len(text_light))
                output+=text_light[int(light_and_dark-0.3)]
                # output+="@"

            else :
                output+=" "
                pass
                # print("e")
    f.write(output)
    f.close()
    time.sleep(1/7)





