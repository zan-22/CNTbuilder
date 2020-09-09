try:
    from numpy import pi, sin, cos
except:
    print("Numpy not installed or not in python path.")
    exit(10)


# How to use:
#In interactive terminal, run the script and 
#call CNTbuilder(geometry, n, length of tube, C-C bond length)
#Geometry can either be "zigzag" or "armchair" (remember quotation marks)
#n is an integer where n > 0
#Length of tube is the length of the carbon nanotube in Ångstrøm
#C-C bond length is the bond length between the carbon atoms in Ångstrøm.
#Common C-C bond length is 1.42 Å
#The output is written as an .xyz file which has to be present in the same
#folder as this script. Currently the output file has to be named zan.xyz
#It is recommended to use Avogadro to visualize the Carbon Nanotube or any
#other molecular builder/visualizer that supports .xyz format
#Script is currently not able to generate chiral nanotubes.
#Example: CNTbuilder("armchair", 10, 10, 1.42), where n = 10 and length is 10Å

class CNTbuilder:
    
    def __init__(self, geometry, n, l, ccbond):
        self.geometry = geometry
        self.n = n
        self.l = l
        self.ccbond = ccbond
        
        if geometry == "armchair":
            
            atc=[]
            circ1=[]
            circ2=[]
            dx=ccbond*cos(120/2*(pi/180.0))
            dy=ccbond*sin(120/2*(pi/180.0))
            radius=(n*(2*dx+ccbond)+n*ccbond)/(2*pi)
            ycoord=+dy
            natoms=2*n
            #create circumferences
            for i in range(n):
                circ1.append(2*dx+ccbond)
                circ1.append(ccbond)
                circ2.append(ccbond)
                circ2.append(2*dx+ccbond)
            #adjust the circumferences
            circ1.insert(0,0.0)
            circ1.pop()
            circ2.insert(0,dx)
            circ2.pop()
            #Build CNT
            while ycoord>-l:
                ycoord-=dy
                arc=0.0
                for i in range(natoms):
                    tmpcoords=['C']
                    arc+=circ1[i]
                    theta=arc/radius
                    tmpcoords.append(radius*cos(theta))
                    tmpcoords.append(ycoord)
                    tmpcoords.append(radius*sin(theta))
                    atc.append(tmpcoords)
                ycoord-=dy
                arc=0.0
                for i in range(natoms):
                    tmpcoords=['C']
                    arc+=circ2[i]
                    theta=arc/radius
                    tmpcoords.append(radius*cos(theta))
                    tmpcoords.append(ycoord)
                    tmpcoords.append(radius*sin(theta))
                    atc.append(tmpcoords)
            
            pbc_l=abs(ycoord)+dy
            print('\n*******************************')
            print('armchair CNT: n= ',n,' l (ang)= ',abs(ycoord))
            print('periodicity (if apply) (ang)= ',pbc_l)
            print('diameter (ang): ',2*radius)
            
            file = open('zan.xyz', 'w')
            file.write(" "+str(len(atc))+"\nArmchair Carbon Nanotube\n")
            for line in atc:
               outline="%-3s%12.6f%12.6f%12.6f" % (line[0],float(line[1]),float(line[2])\
                                             ,float(line[3]))
               file.write(outline+"\n")
            
            
            return
        
        
        
        
        elif geometry == "zigzag":
            atc=[]
            circ1=[]
            circ2=[]
            dy=ccbond*cos(120/2*(pi/180.0))
            dx=ccbond*sin(120/2*(pi/180.0))
            radius=(n*2*dx)/(2*pi)
            ycoord=+ccbond
            #create circumferences
            for i in range(n):
                circ1.append(2*dx)
            #adjust the circumferences
            
            circ1.pop()
            circ2=list(circ1)  #copy list!!! circ2=circ1 make duplicate and are both modified in the same way
            circ1.insert(0,0.0)
            circ2.insert(0,dx)
            #Build CNT
            while ycoord>-l:
                ycoord-=ccbond
                arc=0.0
                for i in range(n):
                    tmpcoords=['C']
                    arc+=circ1[i]
                    theta=arc/radius
                    tmpcoords.append(radius*cos(theta))
                    tmpcoords.append(ycoord)
                    tmpcoords.append(radius*sin(theta))
                    atc.append(tmpcoords)
                ycoord-=dy
                arc=0.0
                for i in range(n):
                    tmpcoords=['C']
                    arc+=circ2[i]
                    theta=arc/radius
                    tmpcoords.append(radius*cos(theta))
                    tmpcoords.append(ycoord)
                    tmpcoords.append(radius*sin(theta))
                    atc.append(tmpcoords)
                ycoord-=ccbond
                arc=0.0
                for i in range(n):
                    tmpcoords=['C']
                    arc+=circ2[i]
                    theta=arc/radius
                    tmpcoords.append(radius*cos(theta))
                    tmpcoords.append(ycoord)
                    tmpcoords.append(radius*sin(theta))
                    atc.append(tmpcoords)
                ycoord-=dy
                arc=0.0
                for i in range(n):
                    tmpcoords=['C']
                    arc+=circ1[i]
                    theta=arc/radius
                    tmpcoords.append(radius*cos(theta))
                    tmpcoords.append(ycoord)
                    tmpcoords.append(radius*sin(theta))
                    atc.append(tmpcoords)
            pbc_l=abs(ycoord)+ccbond
            print('\n*******************************')
            print('zigzag CNT: n= ',n,' l (ang)= ',abs(ycoord))
            print('periodicity (if apply) (ang)= ',pbc_l)
            print('diameter (ang): ',2*radius)
            
            file = open('zan.xyz', 'w')
            file.write(" "+str(len(atc))+"\nZigzag Carbon Nanotube\n")
            for line in atc:
               outline="%-3s%12.6f%12.6f%12.6f" % (line[0],float(line[1]),float(line[2])\
                                             ,float(line[3]))
               file.write(outline+"\n")
        
            return