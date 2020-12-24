from tkinter import *
import time
import tempfile
import base64, zlib

DoRound = True

AM = {"H" : 1.008, "He" : 4.003, "Li" : 6.941, "Be" : 9.012, 
	"B" : 10.811, "C" : 12.011, "N" : 14.007, "O" : 15.999, 
	"F" : 18.998, "Ne" : 20.180, "Na" : 22.990, "Mg" : 24.305, 
	"Al" : 26.982, "Si" : 28.086, "P" : 30.974, "S" : 32.066, 
	"Cl" : 35.453, "Ar" : 39.948, "K" : 39.098, "Ca" : 40.078, 
	"Sc" : 44.956, "Ti" : 47.867, "V" : 50.942, "Cr" : 51.996, 
	"Mn" : 54.938, "Fe" : 55.845, "Co" : 58.933, "Ni" : 58.693, 
	"Cu" : 63.546, "Zn" : 65.380, "Ga" : 69.732, "Ge" : 72.631, 
	"As" : 74.922, "Se" : 78.971, "Br" : 79.904, "Kr" : 84.798, 
	"Rb" : 84.468, "Sr" : 87.620, "Y" : 88.906, "Zr" : 91.224, 
	"Nb" : 92.906, "Mo" : 95.950, "Tc" : 98.907, "Ru" : 101.070, 
	"Rh" : 102.906, "Pd" : 106.42, "Ag" : 107.868, "Cd" : 112.414, 
	"In" : 114.818, "Sn" : 118.711, "Sb" : 121.760, "Te" : 127.600, 
	"I" : 126.904, "Xe" : 131.294, "Cs" : 132.905, "Ba" : 137.328, 
	"La" : 138.905, "Ce" : 140.116, "Pr" : 140.908, "Nd" : 144.243, 
	"Pm" : 144.913, "Sm" : 150.360, "Eu" : 151.964, "Gd" : 157.250, 
	"Tb" : 158.925, "Dy" : 162.500, "Ho" : 164.930, "Er" : 167.259, 
	"Tm" : 168.934, "Yb" : 173.055, "Lu" : 174.967, "Hf" : 178.490, 
	"Ta" : 180.948, "W" : 183.840, "Re" : 186.207, "Os" : 190.230, 
	"Ir" : 192.217, "Pt" : 195.085, "Au" : 196.967, "Hg" : 200.592, 
	"Tl" : 204.383, "Pb" : 207.200, "Bi" : 208.980, "Po" : 208.982, 
	"At" : 209.987, "Rn" : 222.018, "Fr" : 223.020, "Ra" : 226.025, 
	"Ac" : 227.028, "Th" : 232.038, "Pa" : 231.036, "U" : 238.029, 
	"Np" : 237.048, "Pu" : 244.064, "Am" : 243.061, "Cm" : 247.070, 
	"Bk" : 247.070, "Cf" : 251.080, "Es" : 254.000, "Fm" : 257.095, 
	"Md" : 258.100, "No" : 259.101, "Lr" : 262.000, "Rf" : 261.000, 
	"Db" : 262.000, "Sg" : 266.000, "Bh" : 264.000, "Hs" : 269.000, 
	"Mt" : 278.000, "Ds" : 281.000, "Rg" : 280.000, "Cn" : 285.000, 
        "Nh" : 286.000, "Fl" : 289.000, "Mc" : 289.000, "Lv" : 293.000, 
	"Ts" : 294.000, "Og" : 294.000,

        "h" : 1.008, "he" : 4.003, "li" : 6.941, "be" : 9.012, 
	"b" : 10.811, "c" : 12.011, "n" : 14.007, "o" : 15.999, 
	"f" : 18.998, "ne" : 20.180, "na" : 22.990, "mg" : 24.305, 
	"al" : 26.982, "si" : 28.086, "p" : 30.974, "s" : 32.066, 
	"cl" : 35.453, "ar" : 39.948, "k" : 39.098, "ca" : 40.078,
        "sc" : 44.956, "ti" : 47.867, "v" : 50.942, "cr" : 51.996, 
	"mn" : 54.938, "fe" : 55.845, "co" : 58.933, "ni" : 58.693, 
	"cu" : 63.546, "zn" : 65.380, "ga" : 69.732, "ge" : 72.631, 
	"as" : 74.922, "se" : 78.971, "br" : 79.904, "kr" : 84.798, 
	"rb" : 84.468, "sr" : 87.620, "y" : 88.906, "zr" : 91.224, 
	"nb" : 92.906, "mo" : 95.950, "tc" : 98.907, "ru" : 101.070, 
	"rh" : 102.906, "pd" : 106.42, "ag" : 107.868, "cd" : 112.414, 
	"in" : 114.818, "sn" : 118.711, "sb" : 121.760, "te" : 127.600, 
	"i" : 126.904, "xe" : 131.294, "cs" : 132.905, "ba" : 137.328, 
	"la" : 138.905, "ce" : 140.116, "pr" : 140.908, "nd" : 144.243, 
	"pm" : 144.913, "sm" : 150.360, "eu" : 151.964, "gd" : 157.250, 
	"tb" : 158.925, "dy" : 162.500, "ho" : 164.930, "er" : 167.259, 
	"tm" : 168.934, "yb" : 173.055, "lu" : 174.967, "hf" : 178.490, 
	"ta" : 180.948, "w" : 183.840, "re" : 186.207, "os" : 190.230, 
	"ir" : 192.217, "pt" : 195.085, "au" : 196.967, "hg" : 200.592, 
	"tl" : 204.383, "pb" : 207.200, "bi" : 208.980, "po" : 208.982, 
	"at" : 209.987, "rn" : 222.018, "fr" : 223.020, "ra" : 226.025, 
	"ac" : 227.028, "th" : 232.038, "pa" : 231.036, "u" : 238.029, 
	"np" : 237.048, "pu" : 244.064, "am" : 243.061, "cm" : 247.070, 
	"bk" : 247.070, "cf" : 251.080, "es" : 254.000, "fm" : 257.095, 
	"md" : 258.100, "no" : 259.101, "lr" : 262.000, "rf" : 261.000, 
	"db" : 262.000, "sg" : 266.000, "bh" : 264.000, "hs" : 269.000, 
	"mt" : 278.000, "ds" : 281.000, "rg" : 280.000, "cn" : 285.000, 
        "nh" : 286.000, "fl" : 289.000, "mc" : 289.000, "lv" : 293.000, 
	"ts" : 294.000, "og" : 294.000}

gx = 390
gy = 470

scr = Tk()
scr.title("Prof.Brenmore")
scr.geometry("{}x{}".format(gx,gy))

ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

scr.iconbitmap(default=ICON_PATH)




f = Frame(scr)
f.place(x=10,y=10)
f2 = Frame(scr)
f2.place(x=gx/2,y=60)
f3 = Frame(scr)
f3.pack(side=BOTTOM)

SVs = [StringVar(value='') for i in range(8)]

Es = [Entry(f,width=5,font=("Calibri", 10),textvariable=SVs[i]) for i in range(8)]
Es[0].grid(row=0,column=0)

Ps = [Label(f,font=("Calibri", 10),text='+',state=DISABLED) for i in range(8)]
Ps[0].config(state=NORMAL)
Ps[0].grid(row=0,column=1)

Ps[1].grid(row=0,column=3)

Es[1].grid(row=0,column=2)



## S2

ins1 = Canvas(f2, width=160, height=88, borderwidth=0, highlightthickness=0,confine=1)
ins1.pack(side=RIGHT)

t1 = Listbox(ins1,font=("Calibri", 10),height=4, width=10, state=DISABLED)
t1.place(x=0,y=20)

Sb = Scrollbar(t1, command = t1.yview)
t1.config(yscrollcommand = Sb.set)
Sb.place(x=54,y=0,height=65)

tittxt = Label(ins1,font=("Calibri", 10),text='n, mol', state=DISABLED)
tittxt.place(x=100,y=0)

SV9 = StringVar()
Jb = Entry(ins1,width=8,font=("Calibri", 10),textvariable=SV9)
Jb.place(x=89,y=20)

## S3

d1 = 80
d2 = 70
d3 = 70
d4 = 70
du=10

ins2 = Canvas(f3, borderwidth=0)
ins2.pack()

Vertleft = ins2.create_line(20,20,20,200)
Vertleftmid = ins2.create_line(20+d1,20,20+d1,200)
Vertmid = ins2.create_line(20+d1+d2,20,20+d1+d2,200)
Vertrightmid = ins2.create_line(20+d1+d2+d3,20,20+d1+d2+d3,200)
Vertright = ins2.create_line(20+d1+d2+d3+d4,20,20+d1+d2+d3+d4,200)

Hors = [ins2.create_line(20,i*20+20,20+d1+d2+d3+d4,i*20+20) for i in range(10)]

ins2.create_text(20+d1/2,20+du,anchor=CENTER,text='Molecule',font=("Calibri", 11))
ins2.create_text(20+d1+d2/2,20+du,anchor=CENTER,text='n, mol',font=("Calibri", 11))
ins2.create_text(20+d1+d2+d3/2,20+du,anchor=CENTER,text='M, g/mol',font=("Calibri", 11))
ins2.create_text(20+d1+d2+d3+d4/2,20+du,anchor=CENTER,text='m, g',font=("Calibri", 11))

MolecLabels = [None for i in range(8)]
NLabels = [None for i in range(8)]
MLabels = [None for i in range(8)]
MassLabels = [None for i in range(8)]


ErrorLabel = Label(ins2,font=("Calibri", 10),fg='#ee1111',text='Not enough data')
ErrorLabel.place(x=gx/2,y=gy/2-30)
CreditLabel = Label(ins2,font=("Calibri", 10),fg='#555555',text='Made by A.Mirror, A.Filin, Leo K., A.Gur\n MUCTR 2020, v1.1')
CreditLabel.place(x=80,y=gy/2-10)
###
Error = ''
def CheckMolar(text,frm='call1'):
    global Error
    terror = False
    MM = 0
    happened = False
    Fullct = ''
    Act = False
    elements = []
    for i in range(len(text)):
        if happened:
            happened = False
            continue
        if not Act and text[i] in ('0','1','2','3','4','5','6','7','8','9','.'):
            Fullct += text[i]
            continue
        else:
            Act = True
        if Act and text[i] not in ('0','1','2','3','4','5','6','7','8','9','.','[','(',')',']'):
            try:
                print(text[i]+text[i+1]+' ',AM[text[i]+text[i+1]])
                j = AM[text[i]+text[i+1]]
                if DoRound:
                    j1 = round(j,1)
                    if j1%1 < 0.4 or j1%1 > 0.6:
                        j = round(j)
                    else:
                        j = j1
                k = 0
                for ss in range(5):
                    try:
                        k = k*10+int(text[i+2+ss])
                    except:
                        k = k
                        if k == 0:
                            k = 1
                        break
                elements.append((text[i]+text[i+1],j,k))
                happened = True
            except:
                try:
                    print(text[i]+' ',AM[text[i]])
                    j = AM[text[i]]
                    if DoRound:
                        j1 = round(j,1)
                        if j1%1 != 0.5 or j1%1 != 0.4 or j1%1 != 0.6:
                            j = round(j)
                        else:
                            j = j1
                    k = 0
                    for ss in range(5):
                        try:
                            k = k*10+int(text[i+1+ss])
                        except:
                            k = k
                            if k == 0:
                                k = 1
                            break
                    elements.append((text[i],j,k))
                except:
                    ErrorLabel.config(text='Wrong element')
                    print('wrong element')
                    Error = 'Wrong element'
                    terror = True
    #print(elements, Fullct)
    Bct = 0
    for i in range(len(text)):
        if text[i] in ('[','('):
            Bct += 1
    text = text.replace("[",'(')
    text = text.replace("]",')')
    try:
        while Bct > 0:
            readtext = ''
            tBct = 0
            tct = 0
            tMM = 0
            #print('Bct = ',Bct)
            for i in range(len(text)):
                if text[i] == '(':
                    tBct += 1
                if tBct == Bct:
                    if text[i] == '(':
                        text = text[::-1].replace("(",'{',1)[::-1]
                    if text[i] == ')':
                        text = text[:i]+text[i:].replace(")",'}',1)
                        readtext += text[i]
                        tct = 0
                        for ss in range(5):
                            try:
                                tct = tct*10+int(text[i+1+ss])
                            except:
                                tct = tct
                                if tct == 0:
                                    tct = 1
                                break
                        break
                    #print(text)
                    readtext += text[i]
            ttext = readtext[::-1]
            for i in range(len(elements)-1,0,-1):
                #print(len(elements[i][0]))
                if elements[i][0][0] == "{":
                    if elements[i][0][::-1] in ttext:
                        tMM += elements[i][1] * elements[i][2]
                        ttext = ttext.replace(elements[i][0][::-1],'',1)
                        elements.pop(i)
                        continue
                for j in range(len(ttext)):
                    try:
                        if ttext[j] == elements[i][0][0] and ttext[j-1] == elements[i][0][1]:
                            tMM += elements[i][1] * elements[i][2]
                            ttext = ttext.replace(elements[i][0][::-1],'',1)
                            elements.pop(i)
                            break
                    except:
                        if ttext[j] == elements[i][0]:
                            tMM += elements[i][1] * elements[i][2]
                            ttext = ttext.replace(elements[i][0][::-1],'',1)
                            elements.pop(i)
                            break
            if tct == 0:
                raise
            elements.append((readtext,tMM,tct))
            #print(elements)
            Bct -= 1
    except:
        ErrorLabel.config(text='Wrong brackets')
        print('wrong brackets')
        Error = 'Wrong brackets'
        terror = True
    #print(elements)
    for i in elements:
        MM += i[1]*i[2]
    if frm=='call1' and terror == False and ErrorLabel.cget('text')!='Wrong Element':
        ErrorLabel.config(text='')
        Error = ''
    try:
        return (MM,float(Fullct))
    except:
        return (MM,1.0)


###
def callback1(i):
    global MolecLabels
    av = SVs[i].get()
    if i == 0:
        if av != '':
            t1.config(state=NORMAL)
            tittxt.config(state=NORMAL)
            Jb.config(state=NORMAL)
        elif SVs[1].get()=='' and SVs[2].get()=='' and SVs[3].get()=='' and SVs[4].get()=='' and SVs[5].get()=='' and SVs[6].get()=='' and SVs[7].get()=='':
            t1.delete(0,END)
            t1.config(state=DISABLED)
            tittxt.config(state=DISABLED)
            Jb.config(state=DISABLED)
    if len(av) > 5 and len(av) < 20:
        num = len(av)
        ct = 0
        for j in av:
            if j in ('[','('):
                ct+=0.8
        ct/=2
        num-=int(ct)
        Es[i].config(width= num) 
    else:
        Es[i].config(width= 5)
    #print(CheckMolar(av))
    j = i+1

    if (i!=0 and i!=7) and av !='':
        Es[j].grid(row=j//4,column=(j%4)*2)
        Ps[i].config(state=NORMAL)        
        if j!=4:
            Ps[j].grid(row=j//4,column=(j%4)*2-1)
        else:
            Ps[j].grid(row=0,column=7)            
    else:
        t1.delete(i)
        if av!='':
            t1.insert(i, av)
    
    for k in range(8):
        try:
            ins2.delete(MolecLabels[k])
        except:
            continue
        try:
            jk = SVs[k].get()[0]
        except:
            jk = ''
        if CheckMolar(SVs[k].get(),'no')[1] == 1 and jk != '1':
            veryGREG = SVs[k].get()
            #print(1)
        else:
            if CheckMolar(SVs[k].get(),'no')[1] != int(CheckMolar(SVs[k].get(),'no')[1]):
                veryGREG = SVs[k].get().replace(str(CheckMolar(SVs[k].get(),'no')[1]),'',1)
            else:
                veryGREG = SVs[k].get().replace(str(int(CheckMolar(SVs[k].get(),'no')[1])),'',1)
        if len(veryGREG) >= 11:
            MolecLabels[k] = ins2.create_text(20+d1/2,40+du+k*20,anchor=CENTER,text=veryGREG[0:7]+'...',font=("Calibri", 11))
        else:
            MolecLabels[k] = ins2.create_text(20+d1/2,40+du+k*20,anchor=CENTER,text=veryGREG,font=("Calibri", 11))

        try:
            ins2.delete(MLabels[k])
        except:
            continue
        GREG = CheckMolar(SVs[k].get(),'no')[0]
        if GREG - int(GREG) == 0:
            GREG = int(GREG)
        if SVs[k].get()!='':
            MLabels[k] = ins2.create_text(20+d1+d2+d3/2,40+du+k*20,anchor=CENTER,text=GREG,font=("Calibri", 11))
        
        t1.delete(k)
        t1.insert(k, SVs[k].get())
        if k!= 0 and k!=1 and k != 7 and SVs[k].get() == '' and SVs[k+1].get() == '':
            Es[k+1].grid_forget()
            Ps[k+1].grid_forget()
            Ps[k].config(state=DISABLED)

            if SVs[k-1].get()=='':
                Es[k].grid_forget()
                Ps[k].grid_forget()
                Ps[k-1].config(state=DISABLED)
    t1.see(i)
    LBselect(1)

##
GlobalSelection = 0
def callback2():
    global GlobalSelection
    Length = 0
    av = SV9.get()
    try:
        I = t1.curselection()[0]
    except:
        I = GlobalSelection
        t1.select_set(I)
    #print(av,I)
    try:
        av = float(av)
        if ErrorLabel.cget('text') == 'Not a valid value of n':
            ErrorLabel.config(text=Error)
    except:
        if Error == '':
            ErrorLabel.config(text='Not a valid value of n')
        print('not a number')
        av = 0.0
    alsoGREG = 0.0
    #print('aaa',CheckMolar(SVs[I].get(),'call2')[1])
    try:
        GREG = float(CheckMolar(SVs[I].get(),'call2')[1])
    except:
        GREG = 0
    Length = len(str(av).split('.')[1])
    for k in range(8):
        try:
            ins2.delete(NLabels[k])
        except:
            continue    
        
        if SVs[k].get() != '':
            try:
                alsoGREG = float(CheckMolar(SVs[k].get(),'call2')[1])
            except:
                alsoGREG = 0
            if alsoGREG > 0:
                const = round(alsoGREG*av/GREG,Length)
                    
            else:
                const=''
        else:
            const=''
        if k == I:
            NLabels[k] = ins2.create_text(20+d1+d2/2,40+du+k*20,text=av,font=("Calibri", 12))
        else:
            #print(k,'as',const)
            NLabels[k] = ins2.create_text(20+d1+d2/2,40+du+k*20,text=const,font=("Calibri", 11))

        try:
            ins2.delete(MassLabels[k])
        except:
            continue
        if SVs[k].get() != '':
            #print('bss',alsoGREG)
            #print(k,'ass',round(CheckMolar(SVs[k].get(),'call2')[0]*alsoGREG*av/GREG,Length))
            MassLabels[k] = ins2.create_text(20+d1+d2+d3+d4/2,40+du+k*20,text=round(CheckMolar(SVs[k].get(),'call2')[0]*alsoGREG*av/GREG,Length),font=("Calibri", 11))
        
##
def  LBselect(x):
    global GlobalSelection
    try:
        GlobalSelection = t1.curselection()[0]
    except:
        None == None
    callback2()

    
SVs[0].trace("w", lambda name, index, mode:callback1(0))
SVs[1].trace("w", lambda name, index, mode:callback1(1))
SVs[2].trace("w", lambda name, index, mode:callback1(2))
SVs[3].trace("w", lambda name, index, mode:callback1(3))
SVs[4].trace("w", lambda name, index, mode:callback1(4))
SVs[5].trace("w", lambda name, index, mode:callback1(5))
SVs[6].trace("w", lambda name, index, mode:callback1(6))
SVs[7].trace("w", lambda name, index, mode:callback1(7))

t1.bind('<<ListboxSelect>>', LBselect)

SV9.trace("w", lambda x,y,z: callback2())

mainloop()
