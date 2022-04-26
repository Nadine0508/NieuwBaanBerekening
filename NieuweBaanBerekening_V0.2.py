import matplotlib.pyplot as plt 
import matplotlib.quiver as VisuVecotor
import numpy as np
import math 
import random
from matplotlib.widgets import Slider, Button 
from geomdl import BSpline
from mpl_toolkits import mplot3d


# Calculate choose area dependont on original pick
# schaling van het kiesgebied klopy niet 
def MovetimeByAcc (ToPointX, TOPointY, MaxAcc):
    if ToPointX > 500: 
        MoveTime = int(np.sqrt(12243/MaxAcc) * np.sqrt(np.sqrt((0-ToPointX)**2+(0-TOPointY)**2)/1000))
    else: 
        MoveTime = int(np.sqrt(12243/MaxAcc) * np.sqrt(np.sqrt((0-500)**2+(0-500)**2)/1000))
    return (MoveTime)

def CalcChooseArea(Time, OpX, OpY, OpZ):
    if Time < 90: 
        ChooseAreaXMin = OpX * 0.75
        ChooseAreaXMax = OpX * 1.40
        ChooseAreaYMin = OpY * 0.75
        ChooseAreaYMax = OpY * 1.40

    elif Time > 90 and Time < 180: 
        ChooseAreaXMin = OpX * 0.75
        ChooseAreaXMax = OpX * 1.25
        ChooseAreaYMin = OpY * 0.75
        ChooseAreaYMax = OpY * 1.25

    elif Time > 180 and Time < 270: 
        ChooseAreaXMin = OpX * 0.10
        ChooseAreaXMax = OpX * 1.90
        ChooseAreaYMin = OpY * 0.10
        ChooseAreaYMax = OpY * 1.90

    elif Time > 270 and Time < 360: 
        ChooseAreaXMin = OpX * 0.40
        ChooseAreaXMax = OpX * 1.50
        ChooseAreaYMin = OpY * 0.40
        ChooseAreaYMax = OpY * 1.50

    elif Time > 360 and Time < 450: 
        ChooseAreaXMin = OpX * 0.80
        ChooseAreaXMax = OpX * 1.30
        ChooseAreaYMin = OpY * 0.80
        ChooseAreaYMax = OpY * 1.30
    
    elif Time > 450 and Time < 540: 
        ChooseAreaXMin = OpX * 0.90
        ChooseAreaXMax = OpX * 1.20
        ChooseAreaYMin = OpY * 0.90
        ChooseAreaYMax = OpY * 1.20

    else:  
        ChooseAreaXMin = OpX 
        ChooseAreaXMax = OpX 
        ChooseAreaYMin = OpY 
        ChooseAreaYMax = OpY 


    return (ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin)

# Generate OriginalPick 
def ChooseOriginalPick():
    #OpX =  random.randint(1,500)
    #OpY =  random.randint(1,500)
    OpX =  500
    OpY =  500
    OpZ =  0
    return (OpX, OpY, OpZ)

# Generate NewPick 
def ChooseNewPick(ChooseAreaXMax,ChooseAreaXMin,ChooseAreaYMax,ChooseAreaYMin):
    ChooseAreaXMax = int (abs(ChooseAreaXMax)) 
    ChooseAreaXMin = int (abs(ChooseAreaXMin)) 
    ChooseAreaYMax = int (abs(ChooseAreaYMax))
    ChooseAreaYMin = int (abs(ChooseAreaYMin)) 

    NpX =  random.randint(ChooseAreaXMin,ChooseAreaXMax)
    NpY =  random.randint(ChooseAreaYMin,ChooseAreaYMax)
    NpZ =  random.randint(0,75)
    NpZ =  0

    return (NpX, NpY, NpZ)

# Genereates choose moment
def GenTime ():
     Time = random.randint(0,800)
     #Time = 361
     return (Time)

 # Calc NewCubic Points
def CalcCubicPoint(OpX, OpY, OpZ, NpX, NpY, NpZ,Time):

    YposScale = 1
    XposScale = 1
    ZposScale = 0
    #ZposScale = 0

    if OpX < NpX: 
        XposScale = NpX/OpX
        print("Groot")
    if NpX < OpX: 
        XposScale = NpX/OpX
        print("Klein")
    if OpY < NpY: 
        YposScale = NpY/OpY
        print("Groot")
    if NpY < OpY: 
        YposScale = NpY/OpY
        print("Klein")

    if Time < 90: 

        CubicPointX1 = 0.01 + (XposScale - 1) * 0.05
        CubicPointX2 = 0.13 + (XposScale - 1) * 0.08
        CubicPointX3 = 0.36 + (XposScale - 1) * 0.10
        CubicPointX4 = 0.64 + (XposScale - 1) * 0.21
        CubicPointX5 = 0.87 + (XposScale - 1) * 0.50
        CubicPointX6 = 0.99 + (XposScale - 1) * 0.85

        CubicPointY1 = 0.01 + (YposScale - 1) * 0.05
        CubicPointY2 = 0.13 + (YposScale - 1) * 0.08
        CubicPointY3 = 0.36 + (YposScale - 1) * 0.10
        CubicPointY4 = 0.64 + (YposScale - 1) * 0.21
        CubicPointY5 = 0.87 + (YposScale - 1) * 0.50
        CubicPointY6 = 0.99 + (YposScale - 1) * 0.85

        ActTime = 90


    elif Time >= 90 and Time < 180: 

        CubicPointX1 = 0.01
        CubicPointX2 = 0.13 + (XposScale - 1) * 0.05
        CubicPointX3 = 0.36 + (XposScale - 1) * 0.10
        CubicPointX4 = 0.64 + (XposScale - 1) * 0.21
        CubicPointX5 = 0.87 + (XposScale - 1) * 0.50
        CubicPointX6 = 0.99 + (XposScale - 1) * 0.85

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 + (YposScale - 1) * 0.05
        CubicPointY3 = 0.36 + (YposScale - 1) * 0.10
        CubicPointY4 = 0.64 + (YposScale - 1) * 0.21
        CubicPointY5 = 0.87 + (YposScale - 1) * 0.50
        CubicPointY6 = 0.99 + (YposScale - 1) * 0.85

        ActTime = 180

    elif Time >= 180 and Time < 270: 

        CubicPointX1 = 0.01
        CubicPointX2 = 0.13
        CubicPointX3 = 0.36 + (XposScale - 1) * 0.05
        CubicPointX4 = 0.64 + (XposScale - 1) * 0.21
        CubicPointX5 = 0.87 + (XposScale - 1) * 0.50
        CubicPointX6 = 0.99 + (XposScale - 1) * 0.85

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 
        CubicPointY3 = 0.36 + (YposScale - 1) * 0.05
        CubicPointY4 = 0.64 + (YposScale - 1) * 0.21
        CubicPointY5 = 0.87 + (YposScale - 1) * 0.50
        CubicPointY6 = 0.99 + (YposScale - 1) * 0.85

        ActTime = 270
    elif Time >= 270 and Time < 360: 

        CubicPointX1 = 0.01
        CubicPointX2 = 0.13
        CubicPointX3 = 0.36
        CubicPointX4 = 0.64 + (XposScale - 1) * 0.21
        CubicPointX5 = 0.87 + (XposScale - 1) * 0.55
        CubicPointX6 = 0.99 + (XposScale - 1) * 0.85

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 
        CubicPointY3 = 0.36
        CubicPointY4 = 0.64 + (YposScale - 1) * 0.21
        CubicPointY5 = 0.87 + (YposScale - 1) * 0.55
        CubicPointY6 = 0.99 + (YposScale - 1) * 0.85

        ActTime = 360
    elif Time >= 360 and Time < 450: 

        CubicPointX1 = 0.01
        CubicPointX2 = 0.13
        CubicPointX3 = 0.36
        CubicPointX4 = 0.64
        CubicPointX5 = 0.87 + (XposScale - 1) * 0.21
        CubicPointX6 = 0.99 + (XposScale - 1) * 0.48

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 
        CubicPointY3 = 0.36
        CubicPointY4 = 0.64
        CubicPointY5 = 0.87 + (YposScale - 1) * 0.21
        CubicPointY6 = 0.99 + (YposScale - 1) * 0.48
        ActTime = 450
    
    elif Time >= 450 and Time < 540: 

        CubicPointX1 = 0.01
        CubicPointX2 = 0.13
        CubicPointX3 = 0.36
        CubicPointX4 = 0.64
        CubicPointX5 = 0.87
        CubicPointX6 = 0.99 + (XposScale - 1) * 0.35

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 
        CubicPointY3 = 0.36
        CubicPointY4 = 0.64
        CubicPointY5 = 0.87
        CubicPointY6 = 0.99 + (YposScale - 1) * 0.35
        ActTime = 540
    elif Time >= 540 and Time < 630: 

        CubicPointX1 = 0.01
        CubicPointX2 = 0.13
        CubicPointX3 = 0.36
        CubicPointX4 = 0.64
        CubicPointX5 = 0.87
        CubicPointX6 = 0.99

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 
        CubicPointY3 = 0.36
        CubicPointY4 = 0.64
        CubicPointY5 = 0.87
        CubicPointY6 = 0.99
        ActTime = 630
    else: 
        CubicPointX1 = 0.01
        CubicPointX2 = 0.13
        CubicPointX3 = 0.36
        CubicPointX4 = 0.64
        CubicPointX5 = 0.87
        CubicPointX6 = 0.99
        XposScale    = 1

        CubicPointY1 = 0.01
        CubicPointY2 = 0.13 
        CubicPointY3 = 0.36
        CubicPointY4 = 0.64
        CubicPointY5 = 0.87
        CubicPointY6 = 0.99
        YposScale    = 1
        ActTime = Time

    CubicPointY = (0,0,0,0,CubicPointY1,CubicPointY2,CubicPointY3,CubicPointY4,CubicPointY5,CubicPointY6,YposScale,YposScale,YposScale,YposScale)
    CubicPointX = (0,0,0,0,CubicPointX1,CubicPointX2,CubicPointX3,CubicPointX4,CubicPointX5,CubicPointX6,XposScale,XposScale,XposScale,XposScale)
    CubicPointZ = (0.6572,-0.02857391,-0.02857391,0.6572,1,1,0.6572,-0.02857391,-0.02857391,0.6572)
    
    return (CubicPointX,CubicPointY,CubicPointZ,ActTime)

# function for the calcuation of the movement
def CubicSpline(CubicPoint, Number,MoveTime,StartTime):

    #Init Variable
    time = StartTime/1000
    Y = StartTime

    ZPoint = []
    YPoint = []
    XPoint = []

    A      = []
    ATotaal = []

    AX      = []
    AXTotaal = []

    AY      = []
    AYTotaal = []

    RcV    = []
    angle  = []

    V      = [0]
    VTotaal = []

    VX      = [0]
    VXTotaal = []

    VY      = [0]
    VYTotaal = []

    Time = []

    SomeCubicpointArray  = [0]
    SomeCubicpointArrayX = [0]
    SomeCubicpointArrayY = [0]

    Weight = [1,1,1,1,1,1,1,1,1,1]

    for i in range (StartTime,MoveTime,1):

        Y = Y + 1/(MoveTime- StartTime)
        
        #Profile [Careful, Bounce, Dwell]
        #Timefrac = 2.0 + Y *(Number -3 -2.0) # Careful[2.0-7.0]
        #Timefrac = 1.5 + Y *(Number -3 -1.0) # Bounce [1.5-7.5]   
        Timefrac = 1.0 + Y *(Number -3 -0.0) # Dwell  [1.0-8.0]

        BasePoint = math.trunc(Timefrac)

        if BasePoint > 0 and BasePoint < (Number - 2): 
            NcT = Timefrac - BasePoint
            NcT2 = NcT * NcT
            NcT3 = NcT2 * NcT
            Nc1 = -(NcT3/6) + (NcT2/2) - (NcT/2) + (1/6)
            Nc2 = ((NcT3/2)-(NcT2)+(2/3))
            Nc3 = (-(NcT3)+(NcT2)+ NcT)/2 + (1/6)
            Nc4 = (NcT3/6)
            NC = [[Nc1],[Nc2],[Nc3],[Nc4]]

            SomeCubicpointZ = Nc1* CubicPointZ[BasePoint-1] + Nc2*CubicPointZ[BasePoint+0] + Nc3*CubicPointZ[BasePoint+1] + Nc4 *CubicPointZ[BasePoint+2]
            SomeCubicpointNurbsZ = ((Nc1* CubicPointZ[BasePoint-1]*Weight[BasePoint-1]) +(Nc2* CubicPointZ[BasePoint+0]*Weight[BasePoint+0]) +(Nc3* CubicPointZ[BasePoint+1]*Weight[BasePoint+1]) + (Nc4* CubicPointZ[BasePoint+2]*Weight[BasePoint+2]))/((Nc1*Weight[BasePoint-1]) +(Nc2*Weight[BasePoint+0]) +(Nc3*Weight[BasePoint+1]) + (Nc4*Weight[BasePoint+2]))
            

        elif BasePoint >= Number-2:
            SomeCubicpoint = 1

        # Calc of the speed and accelaration
        SomeCubicpointArray.append(SomeCubicpointZ)
        V.append(SomeCubicpointArray[i+1] - SomeCubicpointArray[i])
        A.append(V[i+1]- V[i])

        ZPoint.append(SomeCubicpointZ)

        #ZPoint.append(SomeCubicpointNurbsZ)
        #YPoint.append(SomeCubicpointNurbsY)
        #XPoint.append(SomeCubicpointNurbsX)

    #fig1 = plt.figure()

    # Arrows for the visualisation of the movement, the speed and the acceleration
    #for j in range (10,1000,50):
        #plt.quiver(YPoint[j],ZPoint[j],V[j]*math.cos(angle[j]),V[j+1]*math.sin(angle[j+1]),pivot='tail',color = 'r',scale_units = 'xy')
        #plt.quiver(YPoint[j],ZPoint[j],A[j]*math.sin(angle[j]),A[j]*math.cos(angle[j]), pivot='tail',scale_units = 'xy')

    for x in range (5,MoveTime,1):
        VTotaal.append(V[x-1]+ V[x])
        ATotaal.append(A[x-1]+ A[x])

        time = time + 1/(MoveTimeOG)
        Time.append(time + StartTime/1000)

    # return values complete dataset of the whole move
    return(ZPoint,VTotaal,ATotaal)

def CubicSplineLong(CubicPointY,CubicPointX, Number,MoveTime,StartTime, MoveTimeOG):

    #Init Variable
    time = StartTime/MoveTime
    Y = StartTime/1000

    ZPoint = []
    YPoint = []
    XPoint = []

    A      = []
    ATotaal = []

    AX      = []
    AXTotaal = []

    AY      = []
    AYTotaal = []

    RcV    = []
    angle  = []

    V      = [0]
    VTotaal = []

    VX      = [0]
    VXTotaal = []

    VY      = [0]
    VYTotaal = []

    Time = []

    SomeCubicpointArray  = [0]
    SomeCubicpointArrayX = [0]
    SomeCubicpointArrayY = [0]

    Weight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    for i in range (StartTime,MoveTime,1):
        if StartTime > 0:
            Y = Y + 1/(MoveTime)
        else: 
            Y = Y + 1/(MoveTimeOG - StartTime)
        
        #Profile [Careful, Bounce, Dwell]
        #Timefrac = 2.0 + Y *(Number -3 -2.0) # Careful[2.0-7.0]
        #Timefrac = 1.5 + Y *(Number -3 -1.0) # Bounce [1.5-7.5]   
        Timefrac = 1.0 + Y *(Number -3 -0.0) # Dwell  [1.0-8.0]

        BasePoint = math.trunc(Timefrac)
        if BasePoint > 0 and BasePoint < (Number - 2): 
            NcT = Timefrac - BasePoint
            NcT2 = NcT * NcT
            NcT3 = NcT2 * NcT
            Nc1 = -(NcT3/6) + (NcT2/2) - (NcT/2) + (1/6)
            Nc2 = ((NcT3/2)-(NcT2)+(2/3))
            Nc3 = (-(NcT3)+(NcT2)+ NcT)/2 + (1/6)
            Nc4 = (NcT3/6)
            NC = [[Nc1],[Nc2],[Nc3],[Nc4]]

            SomeCubicpointY = Nc1* CubicPointY[BasePoint-1] + Nc2*CubicPointY[BasePoint+0] + Nc3*CubicPointY[BasePoint+1] + Nc4 *CubicPointY[BasePoint+2]
            SomeCubicpointNurbsY = ((Nc1* CubicPointY[BasePoint-1]*Weight[BasePoint-1]) +(Nc2* CubicPointY[BasePoint+0]*Weight[BasePoint+0]) +(Nc3* CubicPointY[BasePoint+1]*Weight[BasePoint+1]) + (Nc4* CubicPointY[BasePoint+2]*Weight[BasePoint+2]))/((Nc1*Weight[BasePoint-1]) +(Nc2*Weight[BasePoint+0]) +(Nc3*Weight[BasePoint+1]) + (Nc4*Weight[BasePoint+2]))
            SomeCubicpointX = Nc1* CubicPointX[BasePoint-1] + Nc2*CubicPointX[BasePoint+0] + Nc3*CubicPointX[BasePoint+1] + Nc4 *CubicPointX[BasePoint+2]
            SomeCubicpointNurbsX = ((Nc1* CubicPointX[BasePoint-1]*Weight[BasePoint-1]) +(Nc2* CubicPointX[BasePoint+0]*Weight[BasePoint+0]) +(Nc3* CubicPointX[BasePoint+1]*Weight[BasePoint+1]) + (Nc4* CubicPointX[BasePoint+2]*Weight[BasePoint+2]))/((Nc1*Weight[BasePoint-1]) +(Nc2*Weight[BasePoint+0]) +(Nc3*Weight[BasePoint+1]) + (Nc4*Weight[BasePoint+2]))


        elif BasePoint >= Number-2:
            SomeCubicpoint = 1

        # Calc of the speed and accelaration

        SomeCubicpointArrayX.append(SomeCubicpointX)
        VX.append(SomeCubicpointArrayX[i-StartTime+1] - SomeCubicpointArrayX[i-StartTime])
        AX.append(VX[i-StartTime+1]- VX[i-StartTime])

        SomeCubicpointArrayY.append(SomeCubicpointY)
        VY.append(SomeCubicpointArrayY[i-StartTime+1] - SomeCubicpointArrayY[i-StartTime])
        AY.append(VY[i-StartTime+1]- VY[i-StartTime])

       
        YPoint.append(SomeCubicpointY)
        XPoint.append(SomeCubicpointX)

        #ZPoint.append(SomeCubicpointNurbsZ)
        #YPoint.append(SomeCubicpointNurbsY)
        #XPoint.append(SomeCubicpointNurbsX)

    #fig1 = plt.figure()

    # Arrows for the visualisation of the movement, the speed and the acceleration
    #for j in range (10,1000,50):
        #plt.quiver(YPoint[j],ZPoint[j],V[j]*math.cos(angle[j]),V[j+1]*math.sin(angle[j+1]),pivot='tail',color = 'r',scale_units = 'xy')
        #plt.quiver(YPoint[j],ZPoint[j],A[j]*math.sin(angle[j]),A[j]*math.cos(angle[j]), pivot='tail',scale_units = 'xy')

    for x in range (5, (MoveTime-StartTime), 1):

        VXTotaal.append(VX[x-1]+ VX[x])
        AXTotaal.append(AX[x-1]+ AX[x])

        VYTotaal.append(VY[x-1]+ VY[x])
        AYTotaal.append(AY[x-1]+ AY[x])

        time = time + 1/(MoveTimeOG)
        Time.append(time)

    # return values complete dataset of the whole move
    return(XPoint,YPoint,Time,VXTotaal,AXTotaal, VYTotaal,AYTotaal)


def updateGraph(event):
   MoveTime = 2000
   MoveTimeOG = 1000  

   ActTime =  GenTime()
   OpX,OpY,OpZ = ChooseOriginalPick()
   ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin = CalcChooseArea(ActTime,OpX,OpY,OpZ)
   NpX,NpY,NpZ = ChooseNewPick(ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin)
   CubicPointX,CubicPointY,CubicPointZ,ActTime1 = CalcCubicPoint (OpX,OpY,OpZ,NpX, NpY, NpZ, ActTime)

   MoveTimeOG = MovetimeByAcc(OpX,OpY,0.01)
   MoveTime= MovetimeByAcc(NpX,NpY,0.01)

   CubicPointXOG,CubicPointYOG,CubicPointZOG,ActTime1 = CalcCubicPoint (OpX,OpY,OpZ,OpX,OpY,OpZ,ActTime)
   XPoint,YPoint,Time,VXTotaal,AXTotaal,VYTotaal,AYTotaal = CubicSplineLong(CubicPointY, CubicPointX,14,MoveTime,0,MoveTimeOG)
   XPointOG,YPointOG,TimeOG,VXTotaalOG,AXTotaalOG, VYTotaalOG,AYTotaalOG = CubicSplineLong(CubicPointYOG, CubicPointXOG,14,MoveTimeOG,0,MoveTimeOG)
   ZPoint,VTotaal,ATotaal = CubicSpline(CubicPointZ,10,MoveTime,0)
   ZPointOG,VTotaalOG,ATotaalOG = CubicSpline(CubicPointZOG,10,MoveTimeOG,0)

   print("Nieuw tijde is:", MoveTime)
   print("De originele positie was:", OpX,OpY,OpZ)
   print("De nieuwe positie is:", NpX,NpY,NpZ)


   XYPlot.set_ydata(YPoint)
   XYPlot.set_xdata(XPoint)
   XYPlotOG.set_ydata(YPointOG)
   XYPlotOG.set_xdata(XPointOG)
   Fig1.canvas.draw_idle()

   YZPlot.set_ydata(ZPoint)
   YZPlot.set_xdata(YPoint)
   YZPlotOG.set_ydata(ZPointOG)
   YZPlotOG.set_xdata(YPointOG)
   Fig2.canvas.draw_idle()

   VPlot.set_ydata(VXTotaal)
   VPlot.set_xdata(Time)
   VPlotOG.set_ydata(VXTotaalOG)
   VPlotOG.set_xdata(TimeOG)
   VYPlot.set_ydata(VYTotaal)
   VYPlot.set_xdata(Time)
   VYPlotOG.set_ydata(VYTotaalOG)
   VYPlotOG.set_xdata(TimeOG)
   Fig3.canvas.draw_idle()

   APlot.set_ydata(AXTotaal)
   APlot.set_xdata(Time)
   APlotOG.set_ydata(AXTotaalOG)
   APlotOG.set_xdata(TimeOG)
   AYPlot.set_ydata(AYTotaal)
   AYPlot.set_xdata(Time)
   AYPlotOG.set_ydata(AYTotaalOG)
   AYPlotOG.set_xdata(TimeOG)
   Fig4.canvas.draw_idle()

   print ("het kies moment is:", ActTime)

   return (XPoint,YPoint,ZPoint)


# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
Savetax = plt.axes([0.8, 0.05, 0.1, 0.04])
button = Button(Savetax, 'Update Graph', hovercolor='0.975')
button.on_clicked(updateGraph)

MoveTime = 2000
MoveTimeOG = 1000 

ActTime =  GenTime()
OpX,OpY,OpZ = ChooseOriginalPick()
ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin = CalcChooseArea(ActTime,OpX,OpY,OpZ)
NpX, NpY, NpZ = ChooseNewPick(ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin)

MoveTimeOG = MovetimeByAcc(OpX,OpY,0.01)
MoveTime= MovetimeByAcc(NpX,NpY,0.01)

CubicPointX,CubicPointY,CubicPointZ,ActTime1 = CalcCubicPoint (OpX,OpY,OpZ,NpX, NpY, NpZ, ActTime)
CubicPointXOG,CubicPointYOG,CubicPointZOG,ActTimeOG = CalcCubicPoint (OpX,OpY,OpZ,OpX,OpY,OpZ,ActTime)
XPoint,YPoint,Time,VXTotaal,AXTotaal, VYTotaal,AYTotaal = CubicSplineLong(CubicPointY, CubicPointX,14,ActTime1,0,MoveTimeOG)
XPointNa,YPointNa,TimeNa,VXTotaalNa,AXTotaalNa, VYTotaalNa,AYTotaalNa = CubicSplineLong(CubicPointY,CubicPointX,14,MoveTime,ActTime1,MoveTime)
XPointOG,YPointOG,TimeOG,VXTotaalOG,AXTotaalOG, VYTotaalOG,AYTotaalOG = CubicSplineLong(CubicPointYOG,CubicPointXOG,14,MoveTimeOG,0,MoveTimeOG)
ZPoint,VTotaal,ATotaal = CubicSpline(CubicPointZ,10,MoveTime,0)
ZPointOG,VTotaalOG,ATotaalOG = CubicSpline(CubicPointZOG,10, MoveTimeOG,0)

XPoint.extend(XPointNa) 
YPoint.extend(YPointNa)
Time.extend (TimeNa)
VXTotaal.extend (VXTotaalNa)
AXTotaal.extend(AXTotaalNa)
VYTotaal.extend(VYTotaalNa)
AYTotaal.extend(AYTotaalNa)

print ("het kies moment is:", ActTime)
print ("Er wordt van de baan afgeweken:", ActTime1)
print ("De beweegtijd van de nieuwe beweging is:", MoveTime)

Fig1,Ax1 = plt.subplots()
XYPlot, = Ax1.plot(XPoint,YPoint)
XYPlotOG, = Ax1.plot(XPointOG,YPointOG)
Ax1.set(xlim=(-0.1,2.1), ylim=(0,2))
Ax1.set_xlabel('X [mm]')
Ax1.set_ylabel('Y [mm]')

Fig2,Ax2 = plt.subplots()
YZPlot, = Ax2.plot(YPoint,ZPoint)
YZPlotOG, = Ax2.plot(YPointOG, ZPointOG)
Ax2.set(xlim=(-0.1,2.1), ylim=(0,1))
Ax2.set_xlabel('Y [mm]')
Ax2.set_ylabel('Z [mm]')

Fig3,Ax3 = plt.subplots()
VPlot, = Ax3.plot(Time,VXTotaal)
VPlotOG, = Ax3.plot(TimeOG,VXTotaalOG)
VYPlot, = Ax3.plot(Time,VYTotaal)
VYPlotOG, = Ax3.plot(TimeOG,VYTotaalOG)
Ax3.set(xlim=(-0.1,1.1), ylim=(-0.01,0.01))
Ax3.set_xlabel('Time [sec]')
Ax3.set_ylabel('V [mm/s]')

Fig4,Ax4 = plt.subplots()
APlot, = Ax4.plot(Time,AXTotaal)
APlotOG, = Ax4.plot(TimeOG,AXTotaalOG)
AYPlot, = Ax4.plot(Time, AYTotaal,)
AYPlotOG, = Ax4.plot(TimeOG,AYTotaalOG)

#AYMax = np.full((995), 0.000065)
#AYMin = np.full((995), -0.000065)
#plt.plot(Time,AYMax)
#plt.plot(Time,AYMin)

Ax4.set(xlim=(-0.1,1.1), ylim=(-0.00007,0.00007))
Ax4.set_xlabel('Time [sec]')
Ax4.set_ylabel('A [mm/s^2]')

plt.show()