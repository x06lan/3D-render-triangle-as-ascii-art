# 3D渲染

## 概念
![](https://i.imgur.com/R4PPWy0.png)
維基百科上
### 三維 直線
![](https://i.imgur.com/XXLV3bz.png)
### 三圍 面
![](https://i.imgur.com/DBoWX4W.png)
### 線與面的焦點
![](https://i.imgur.com/M4mM21C.png)
### 不同階矩陣相乘
![](https://pic3.zhimg.com/v2-70870223f10b4e050fe324a9d3de18fa_b.jpg)
## 定義 class
```python=
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

```
## 線與面的焦點
```python=
import numpy as np
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

```

## camera
```python=
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
```

