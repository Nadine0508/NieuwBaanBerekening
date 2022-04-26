import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.widgets import Slider, Button
import matplotlib.quiver as VisuVecotor
import math 
from geomdl import BSpline
from mpl_toolkits import mplot3d


# Calculate choose area dependont on original pick
def CalcChooseArea(Time, OpX, OpY, OpZ):
    if Time < 142: 
        ChooseAreaXMin = OpX * 0.25
        ChooseAreaXMax = OpX * 1.4
        ChooseAreaYMin = OpX * 0.25
        ChooseAreaYMax = OpX * 1.4

    if Time > 142 and Time < 420: 
        ChooseAreaXMin = OpX * 0.75
        ChooseAreaXMax = OpX * 1.25
        ChooseAreaYMin = OpX * 0.75
        ChooseAreaYMax = OpX * 1.25

    if Time > 420 and Time < 565: 
        ChooseAreaXMin = OpX * 0.75
        ChooseAreaXMax = OpX * 1.50
        ChooseAreaYMin = OpX * 0.75
        ChooseAreaYMax = OpX * 1.50

    return (ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin)


def ChooseNewPick(ChooseAreaXMax, ChooseAreaXMin,ChooseAreaYMax, ChooseAreaYMin):
    NpX =  random.randint(ChooseAreaXMin,ChooseAreaXMax)
    NpY =  random.randint(ChooseAreaYMin,ChooseAreaYMax)
    NpZ =  0
    Time = random.randint(0,1000)
    return (NpX, NpY, NpZ, Time)


def CalcCubicPoinyd(OpX, OpY, OpZ, NpX, NpY, NpZ,Time):
    XposScale = OpX/NpX
    YposScale = OpY/NpY
    ZposScale = OpZ/NpZ

    if Time < 140: 

        CubicPointX1 = 0.25
        CubicPointX2 = 0.75 + ((XposScale - 1 ) * 0.32)
        CubicPointX3 = XposScale

        CubicPointY1 = 0.25
        CubicPointY2 = 0.75 + ((YposScale - 1) * 0.32)
        CubicPointY3 = YposScale

    elif Time < 420 and Time > 140: 

        CubicPointX1 = 0.25
        CubicPointX2 = 0.75 
        CubicPointX3 = XposScale

        CubicPointY1 = 0.25
        CubicPointY2 = 0.75
        CubicPointY3 = YposScale

    elif Time> 420 and Time < 565: 

        CubicPointX1 = 0.25
        CubicPointX2 = 0.75
        CubicPointX3 = XposScale

        CubicPointY1 = 0.25
        CubicPointY2 = 0.75 
        CubicPointY3 = YposScale
    
    else: 
        CubicPointX1 = 0.25
        CubicPointX2 = 0.75
        CubicPointX3 = 1.0

        CubicPointY1 = 0.25
        CubicPointY2 = 0.75 
        CubicPointY3 = 1.0

    return (CubicPointX1,CubicPointX2,CubicPointX3, CubicPointY1,CubicPointY2,CubicPointY3)


# The function to be called anytime a slider's value changes
def update(val):

    if Time_slider.val < 140: 
        Cubic1 = 0.6572
        Cubic2 = Cubic_slider1.val
        Cubic3 = Cubic_slider2.val
        Cubic4 = Cubic_slider.val

        Cubic5 = 0.25
        Cubic6 = 0.75 + ((XPos_slider.val - 1 ) * 0.32)
        Cubic7 = XPos_slider.val

        Cubic8 = 0.25
        Cubic9 = 0.75 + ((YPos_slider.val - 1) * 0.32)
        Cubic10 = YPos_slider.val

    elif Time_slider.val < 420 and Time_slider.val > 140: 
        Cubic1 = 0.6572
        Cubic2 = 1.0
        Cubic3 = Cubic_slider2.val 
        Cubic4 = Cubic_slider.val

        Cubic5 = 0.25
        Cubic6 = 0.75
        Cubic7 = XPos_slider.val

        Cubic8 = 0.25
        Cubic9 = 0.75
        Cubic10 = YPos_slider.val

    elif Time_slider.val > 420 and Time_slider.val < 565: 
        Cubic1 = 0.6572
        Cubic2 = 1.0
        Cubic3 = 1.0 #veranderen
        Cubic4 = Cubic_slider.val

        Cubic5 = 0.25
        Cubic6 = 0.75
        Cubic7 = 1.0


        Cubic8 = 0.25
        Cubic9 = 0.75
        Cubic10 = 1.0
    
    else: 
        Cubic1 = 0.6572
        Cubic2 = 1.0
        Cubic3 = 1.0
        Cubic4 = 0.6572 

        Cubic5 = 0.25
        Cubic6 = 0.75
        Cubic7 = 1.0

        Cubic8 = 0.25
        Cubic9 = 0.75
        Cubic10 = 1.0

    CubicPointY1 = (0,0,0,0,Cubic_slider1.val,Cubic_slider2.val,Cubic_slider5.val,Cubic_slider7.val,Cubic_slider8.val,Cubic_slider9.val,YPos_slider.val,YPos_slider.val,YPos_slider.val,YPos_slider.val)
    CubicPointX1 = (0,0,0,0,Cubic_slider1.val,Cubic_slider2.val,Cubic_slider5.val,Cubic_slider7.val,Cubic_slider8.val,Cubic_slider9.val,XPos_slider.val,XPos_slider.val,XPos_slider.val,XPos_slider.val)
    CubicPointZ1 = (0.6572,-0.02857391,-0.02857391,0.6572,1,1,0.6572,ZPos_slider.val,ZPos_slider.val,ZPos_slider.val)
  
    Number = 10

    XPoint1,YPoint1,ZPoint1,Time, VTotaal1,ATotaal1,VXTotaal1,AXTotaal1, VYTotaal1,AYTotaal1 = CubicSpline(CubicPointZ1,CubicPointY1,CubicPointX1, Number)
    XPoint1,YPoint1,Time, VTotaal1,AXTotaal1, VYTotaal1,AYTotaal1 = CubicSplineLong(CubicPointY1,CubicPointX1,14)
    line.set_ydata(ZPoint1)
    line.set_xdata(YPoint1)
    fig.canvas.draw_idle()

    XYpos.set_ydata(YPoint1)
    XYpos.set_xdata(XPoint1)
    figXY.canvas.draw_idle()

    # Plot the speed 
    VPlot.set_ydata(VTotaal1)
    VPlot.set_xdata(Time)
    fig2.canvas.draw_idle()
 

    # Plot the accelaration 
    APlot.set_ydata(ATotaal1)
    APlot.set_xdata(Time)
    fig3.canvas.draw_idle()

    # Plot the speed X
    VXPlot.set_ydata(VXTotaal1)
    VXPlot.set_xdata(Time)
    fig2X.canvas.draw_idle()
 

    # Plot the accelaration X 
    AXPlot.set_ydata(AXTotaal1)
    AXPlot.set_xdata(Time)
    fig3X.canvas.draw_idle()

    # Plot the speed Y
    VYPlot.set_ydata(VYTotaal1)
    VYPlot.set_xdata(Time)
    fig2Y.canvas.draw_idle()
 

    # Plot the accelaration Y
    AYPlot.set_ydata(AYTotaal1)
    AYPlot.set_xdata(Time)
    fig3Y.canvas.draw_idle()

    for i in range (300,len(ATotaal1),1):
        if ATotaal1[i] > 0.000065 or ATotaal1[i] < - 0.00005:
            print (ATotaal1[i])
            #print (i)
            # (Pos_slider.val)

def SaveData(Cubic5, Cubic6, Cubic7, Cubic8,Cubic9 ,Cubic10,X,Y,Z):   
    cubic5 = [] 
    cubic6 = []
    cubic7 = []
    cubic8 = []
    cubic9 = []
    cubic10 = []
    x = []
    y = []
    z = []
    i = 1

    cubic5.append(Cubic5)
    cubic6.append(Cubic6)
    cubic7.append(Cubic7)
    cubic8.append(Cubic8)
    cubic9.append(Cubic9)
    cubic10.append(Cubic10)
    x.append(X)
    y.append(Y)
    z.append(Z)

    print(cubic5,cubic6,cubic7,cubic8,cubic9,cubic10,x,y,z)
    return (cubic5,cubic6,cubic7,cubic8,cubic9,cubic10,x,y,z)            

def reset(event):
    Time_slider.reset()
    Pos_slider.reset()
    Cubic_slider.reset()

def CubicSplineLong(CubicPointY,CubicPointX, Number):

    #Init Variable
    time = 0
    Y = 0

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

    Weight = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    for i in range (0,1000,1):
        Y = Y + 1/1000
        
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


        elif BasePoint >= 8:
            SomeCubicpoint = 1

        # Calc of the speed and accelaration

        SomeCubicpointArrayX.append(SomeCubicpointX)
        VX.append(SomeCubicpointArrayX[i+1] - SomeCubicpointArrayX[i])
        AX.append(VX[i+1]- VX[i])

        SomeCubicpointArrayY.append(SomeCubicpointY)
        VY.append(SomeCubicpointArrayY[i+1] - SomeCubicpointArrayY[i])
        AY.append(VY[i+1]- VY[i])

       
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

    for x in range (5,1000,1):

        VXTotaal.append(VX[x-1]+ VX[x])
        AXTotaal.append(AX[x-1]+ AX[x])

        VYTotaal.append(VY[x-1]+ VY[x])
        AYTotaal.append(AY[x-1]+ AY[x])

        time = time + 1/1000
        Time.append(time)


    # return values complete dataset of the whole move
    return(XPoint,YPoint,Time,VXTotaal,AXTotaal, VYTotaal,AYTotaal)

# function for the calcuation of the movement
def CubicSpline(CubicPointZ,CubicPointY,CubicPointX, Number):

    #Init Variable
    time = 0
    Y = 0

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

    Weight = [1,1,1,1,1,1,1,1,1,1] 

    SomeCubicpointArray = [0]
    SomeCubicpointArrayX = [0]
    SomeCubicpointArrayY = [0]

    for i in range (0,1000,1):
        Y = Y + 1/1000
        
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
            #SomeCubicpointNurbsZ = ((Nc1* CubicPointZ[BasePoint-1]*Weight[BasePoint-1]) +(Nc2* CubicPointZ[BasePoint+0]*Weight[BasePoint+0]) +(Nc3* CubicPointZ[BasePoint+1]*Weight[BasePoint+1]) + (Nc4* CubicPointZ[BasePoint+2]*Weight[BasePoint+2]))/((Nc1*Weight[BasePoint-1]) +(Nc2*Weight[BasePoint+0]) +(Nc3*Weight[BasePoint+1]) + (Nc4*Weight[BasePoint+2]))
            SomeCubicpointY = Nc1* CubicPointY[BasePoint-1] + Nc2*CubicPointY[BasePoint+0] + Nc3*CubicPointY[BasePoint+1] + Nc4 *CubicPointY[BasePoint+2]
            #SomeCubicpointNurbsY = ((Nc1* CubicPointY[BasePoint-1]*Weight[BasePoint-1]) +(Nc2* CubicPointY[BasePoint+0]*Weight[BasePoint+0]) +(Nc3* CubicPointY[BasePoint+1]*Weight[BasePoint+1]) + (Nc4* CubicPointY[BasePoint+2]*Weight[BasePoint+2]))/((Nc1*Weight[BasePoint-1]) +(Nc2*Weight[BasePoint+0]) +(Nc3*Weight[BasePoint+1]) + (Nc4*Weight[BasePoint+2]))
            SomeCubicpointX = Nc1* CubicPointX[BasePoint-1] + Nc2*CubicPointX[BasePoint+0] + Nc3*CubicPointX[BasePoint+1] + Nc4 *CubicPointX[BasePoint+2]
            #SomeCubicpointNurbsX = ((Nc1* CubicPointX[BasePoint-1]*Weight[BasePoint-1]) +(Nc2* CubicPointX[BasePoint+0]*Weight[BasePoint+0]) +(Nc3* CubicPointX[BasePoint+1]*Weight[BasePoint+1]) + (Nc4* CubicPointX[BasePoint+2]*Weight[BasePoint+2]))/((Nc1*Weight[BasePoint-1]) +(Nc2*Weight[BasePoint+0]) +(Nc3*Weight[BasePoint+1]) + (Nc4*Weight[BasePoint+2]))

        elif BasePoint >= (Number - 2):
            SomeCubicpoint = 1

        # Calc of the speed and accelaration
        SomeCubicpointArray.append(SomeCubicpointZ)
        V.append(SomeCubicpointArray[i+1] - SomeCubicpointArray[i])
        A.append(V[i+1]- V[i])

        SomeCubicpointArrayX.append(SomeCubicpointX)
        VX.append(SomeCubicpointArrayX[i+1] - SomeCubicpointArrayX[i])
        AX.append(VX[i+1]- VX[i])

        SomeCubicpointArrayY.append(SomeCubicpointY)
        VY.append(SomeCubicpointArrayY[i+1] - SomeCubicpointArrayY[i])
        AY.append(VY[i+1]- VY[i])

        ZPoint.append(SomeCubicpointZ)
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

    for x in range (5,1000,1):
        VTotaal.append(V[x-1]+ V[x])
        ATotaal.append(A[x-1]+ A[x])

        VXTotaal.append(VX[x-1]+ VX[x])
        AXTotaal.append(AX[x-1]+ AX[x])

        VYTotaal.append(VY[x-1]+ VY[x])
        AYTotaal.append(AY[x-1]+ AY[x])

        time = time + 1/1000
        Time.append(time)


    #plt.plot(YPoint,ZPoint)

    # return values complete dataset of the whole move
    return(XPoint,YPoint,ZPoint,Time, VTotaal,ATotaal, VXTotaal,AXTotaal, VYTotaal,AYTotaal)

# Define initial parameters
init_ZPos = 0
init_XPos = 1
init_YPos = 1
init_Time = 500
init_Cubic = 0.6572
init_Cubic1 = 1
init_Cubic2 = 1
init_Cubic5 = 0.25
init_Cubic6 = 0.75
init_Cubic7 = 1
init_Cubic8 = 0.25
init_Cubic9 = 0.75
init_Cubic10 = 1

# Make a horizontal slider to control the frequency.

Zaxpos = plt.axes([0.25, 0.55, 0.65, 0.03])
ZPos_slider = Slider(
    ax=Zaxpos,
    label='ZPos [mm]',
    valmin=0,
    valmax=1,
    valinit=init_ZPos,
)

Xaxpos = plt.axes([0.25, 0.60, 0.65, 0.03])
XPos_slider = Slider(
    ax=Xaxpos,
    label='XPos [mm]',
    valmin=0,
    valmax=2,
    valinit=init_XPos,
)
Yaxpos = plt.axes([0.25, 0.50, 0.65, 0.03])
YPos_slider = Slider(
    ax=Yaxpos,
    label='YPos [mm]',
    valmin=0,
    valmax=2,
    valinit=init_YPos,
)

# Make a horizontal slider to control the frequency.
axtime = plt.axes([0.25, 0.15, 0.65, 0.03])
Time_slider = Slider(
    ax=axtime,
    label='Time [Sec]',
    valmin=1,
    valmax=1000,
    valinit=init_Time,
)

# Make a horizontal slider to control the frequency.
axCubic = plt.axes([0.25, 0.25, 0.65, 0.03])
Cubic_slider = Slider(
    ax=axCubic,
    label='CubicPoint [Sec]',
    valmin=0,
    valmax=1,
    valinit=init_Cubic,
)

# Make a horizontal slider to control the frequency.
axCubic1 = plt.axes([0.25, 0.3, 0.65, 0.03])
Cubic_slider1 = Slider(
    ax=axCubic1,
    label='CubicPoint1 [Sec]',
    valmin=0,
    valmax=1,
    valinit=init_Cubic1,
)

# Make a horizontal slider to control the frequency.
axCubic2 = plt.axes([0.25, 0.35, 0.65, 0.03])
Cubic_slider2 = Slider(
    ax=axCubic2,
    label='CubicPoint2 [Sec]',
    valmin=0,
    valmax=1,
    valinit=init_Cubic2,
)

# Make a horizontal slider to control the frequency.
axCubic5 = plt.axes([0.25, 0.40, 0.65, 0.03])
Cubic_slider5 = Slider(
    ax=axCubic5,
    label='CubicPoint5 [Sec]',
    valmin=0,
    valmax=2,
    valinit=init_Cubic5,
)
# Make a horizontal slider to control the frequency.
axCubic6 = plt.axes([0.25, 0.45, 0.65, 0.03])
Cubic_slider6 = Slider(
    ax=axCubic6,
    label='CubicPoint6 [Sec]',
    valmin=0,
    valmax=2,
    valinit=init_Cubic6,
)

# Make a horizontal slider to control the frequency.
axCubic7 = plt.axes([0.25, 0.65, 0.65, 0.03])
Cubic_slider7 = Slider(
    ax=axCubic7,
    label='CubicPoint7 [Sec]',
    valmin=0,
    valmax=2,
    valinit=init_Cubic7,
)
# Make a horizontal slider to control the frequency.
axCubic8 = plt.axes([0.25, 0.70, 0.65, 0.03])
Cubic_slider8 = Slider(
    ax=axCubic8,
    label='CubicPoint8 [Sec]',
    valmin=0,
    valmax=2,
    valinit=init_Cubic8,
)

# Make a horizontal slider to control the frequency.
axCubic9 = plt.axes([0.25, 0.75, 0.65, 0.03])
Cubic_slider9 = Slider(
    ax=axCubic9,
    label='CubicPoint9 [Sec]',
    valmin=0,
    valmax=2,
    valinit=init_Cubic9,
)
# Make a horizontal slider to control the frequency.
axCubic10 = plt.axes([0.25, 0.80, 0.65, 0.03])
Cubic_slider10 = Slider(
    ax=axCubic10,
    label='CubicPoint10 [Sec]',
    valmin=0,
    valmax=2,
    valinit=init_Cubic10,
)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
Savetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(Savetax, 'Save', hovercolor='0.975')
#button.on_clicked()

# CubicPoint sets for baanberekening
CubicPointZ = (0.6572,-0.02857391,-0.02857391,0.6572,1,1,0.6572,-0.02857391,-0.02857391,0.6572)
CubicPointY = (0,0,0,0,0.25,0.75,1,1,1,1)
CubicPointX = (0,0,0,0,0.25,0.75,1,1,1,1)

CubicPointZ1 = (0.6572,-0.02857391,-0.02857391,0.6572,1,1,0.6572,-0.02857391,-0.02857391,0.6572)
CubicPointY1 = (0,0,0,0,0.01,0.13,0.36,0.64,0.87,0.99,YPos_slider.val,YPos_slider.val,YPos_slider.val,YPos_slider.val)
CubicPointX1 = (0,0,0,0,0.01,0.13,0.36,0.64,0.87,0.99,XPos_slider.val,XPos_slider.val,XPos_slider.val,XPos_slider.val)

#CubicPointZ2 = (0,0,0,0.6572,1,1.1,0.72292,0,0,0)
#CubicPointY2 = (0,0,0,0,0.25,0.75,1.1,1.1,1.1,1.1)
#CubicPointX2 = (0,0,0,0,0.25,0.75,0.75,0.75,0.75,0.75)

Number = 10

# Calling of the cubicSpline function 
XPoint,YPoint,ZPoint,Time, VTotaal,ATotaal,VXTotaal,AXTotaal, VYTotaal,AYTotaal = CubicSpline(CubicPointZ,CubicPointY,CubicPointX, 10)
XPoint,YPoint,Time,VXTotaal,AXTotaal, VYTotaal,AYTotaal = CubicSplineLong(CubicPointY,CubicPointX, 10)
XPoint1,YPoint1,ZPoint1,Time, VTotaal1,ATotaal1,VXTotaal1,AXTotaal1, VYTotaal1,AYTotaal1 = CubicSpline(CubicPointZ1,CubicPointY1,CubicPointX1, 10)
XPoint1,YPoint1,Time,VXTotaal1,AXTotaal1, VYTotaal1,AYTotaal1 = CubicSplineLong(CubicPointY1,CubicPointX1, 14)
#XPoint2,YPoint2,ZPoint2,Time, VTotaal2,ATotaal2 = CubicSpline(CubicPointZ2,CubicPointY2,CubicPointX2, Number)

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
# adjust the main plot to make room for the sliders
#plt.subplots_adjust(left=0.2, bottom=0.4)
ax.set(xlim=(-0.1,2.1), ylim=(0,1))
#ax = plt.axes(projection = '3d')
line, = plt.plot(YPoint1,ZPoint1, lw=2)
plt.plot(YPoint,ZPoint, lw=2)
ax.set_xlabel('Y [mm]')
ax.set_ylabel('Z [mm]')

figXY, ax = plt.subplots()
# adjust the main plot to make room for the sliders
#plt.subplots_adjust(left=0.2, bottom=0.4)
ax.set(xlim=(-0.1,2.1), ylim=(-0.1,2.1))
#ax = plt.axes(projection = '3d')
XYpos, = plt.plot(XPoint1,YPoint1, lw=2)
null1 = np.full((1150),0.25)
null2 = np.full((1150),1.40)
Y1 = null1 + np.full((1150), 0.25) + null2 + np.full((1150), 1.40)
X1 = np.full((1150), 0.25) + null1 + np.full((1150), 1.40) + null1

plt.plot (Y1,X1)

plt.plot(XPoint,YPoint, lw=2)
ax.set_xlabel('X [mm]')
ax.set_ylabel('Y [mm]')


# register the update function with each slider
Time_slider.on_changed(update)
ZPos_slider.on_changed(update)
XPos_slider.on_changed(update)
YPos_slider.on_changed(update)
Cubic_slider.on_changed(update)
Cubic_slider1.on_changed(update)
Cubic_slider2.on_changed(update)
Cubic_slider5.on_changed(update)
Cubic_slider6.on_changed(update)
Cubic_slider7.on_changed(update)
Cubic_slider8.on_changed(update)
Cubic_slider9.on_changed(update)
Cubic_slider10.on_changed(update)

#Plot the speed 
fig2, ax2 = plt.subplots()
plt.plot(Time, VTotaal)
VPlot, = ax2.plot(Time, VTotaal1)
#plt.plot(Time, VTotaal2)

# Plot the accelaration 
AMax = np.full((995), 0.000065)
AMin = np.full((995), -0.00005)

fig3,ax3 = plt.subplots()
plt.plot(Time,AMax)
plt.plot(Time,AMin)
APlot, = ax3.plot(Time, ATotaal1)
plt.plot(Time, ATotaal)
#plt.plot(Time, ATotaal2)

#Plot the speed X
fig2X, ax2X = plt.subplots()
plt.plot(Time, VXTotaal)
VXPlot, = ax2X.plot(Time, VXTotaal1)
#plt.plot(Time, VTotaal2)

# Plot the accelaration 
AXMax = np.full((995), 0.000065)
AXMin = np.full((995), -0.00005)

fig3X,ax3X = plt.subplots()
plt.plot(Time,AXMax)
plt.plot(Time,AXMin)
AXPlot, = ax3X.plot(Time, AXTotaal1)
plt.plot(Time, AXTotaal)
#plt.plot(Time, ATotaal2)

#Plot the speed Y
fig2Y, ax2Y = plt.subplots()
plt.plot(Time, VYTotaal)
VYPlot, = ax2Y.plot(Time, VYTotaal1)
#plt.plot(Time, VTotaal2)

# Plot the accelaration 
AYMax = np.full((995), 0.000065)
AYMin = np.full((995), -0.000065)

fig3Y,ax3Y = plt.subplots()
plt.plot(Time,AYMax)
plt.plot(Time,AYMin)
AYPlot, = ax3Y.plot(Time, AYTotaal1)
plt.plot(Time, AYTotaal)
#plt.plot(Time, ATotaal2)

# Plot the movement in 3D
fig4, ax4 = plt.subplots()
ax = plt.axes(projection = '3d')
ax.plot3D (XPoint,YPoint,ZPoint)
DrieDplot = ax.plot3D (XPoint1,YPoint1,ZPoint1)
#ax.plot3D (XPoint2,YPoint2,ZPoint2)
ax.plot(XPoint,YPoint)
TweeDplot = ax.plot(XPoint1,YPoint1)
#ax.plot(XPoint2,YPoint2)

plt.show()