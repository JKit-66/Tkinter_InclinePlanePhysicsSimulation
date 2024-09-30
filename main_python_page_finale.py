import Tkinter as tk
import math, time, tkMessageBox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os 



root = tk.Tk()
root.configure(bg = "thistle1")
root.geometry("1077x731")
#1080 750
#width and height of the canvas
width = 550
high = 480

ig = Image.open("AnimationBG3.gif")
log = ImageTk.PhotoImage(ig)





c = tk.Canvas(root, width=width, height=high)
c.grid(row = 0 , column = 0 , padx = 10 , pady = 10,sticky='nwse')
c.config(highlightbackground = "black", highlightcolor= "black")
frame_1 =tk.Frame(root,width=170,height=100 ,bg = "thistle1")
frame_1.grid(row = 4 , column = 0 , padx = 10, pady = 10 )
 
global logo, logo_1
def help_1():
    root = tk.Toplevel()
    root.title(" Help")
    root.configure(bg = 'white')
    logo = tk.PhotoImage(file = "Help1.GIF")
    w1 = tk.Label(root, image= logo).pack(side = "left")
    logo_1 = tk.PhotoImage(file = "help2.GIF")
    w2 = tk.Label(root, image= logo_1).pack(side = "right")
    root.resizable(False,False)
    root.mainloop()



"""frame_2 =tk.Frame(main,width=75,height=30)
frame_2.place(x=300,y=450)

frame_3 =tk.Frame(main,width=75,height=30)
frame_3.place(x=450,y=450)"""


#title for the canvas
root.title("Motion on an Inclined Plane")

#fixed end's x and y coordinate for the inclined plane
x_2 = 400  #fixed 
y_2 = 390  #fixed

#the length of the inclined plane is fixed
#divisible by 15
length_ = 405


    
    
def obj_size():
    """ to obtain the mass of the object and the mass influence the volume of the object"""
    global heavy
     
    heavy = weight_scale.get()
    
        
    global ball_width, ball_height
    ball_width = (35.0 + (heavy/10))
    ball_height =(35.0 + (heavy/10))

    if heavy == 0:
        tkMessageBox.showinfo(title="WARNING !",message= "Object cannot be 0 mass! Try Again !!", icon='warning')
        weight_scale.set(0.1)
        

def set_angle():
    """ to obtain the angle of the inclined plane depending on the slider"""
    global length_ , x_2 , y_2 ,high, width
    global end_x , end_y , angle_in_rad , abc , kanina , hypotenuse
    abc = ptptangle.get()
    angle_in_rad = (((abc)/180.0) * math.pi)
    end_y =y_2 - (length_ * math.sin(angle_in_rad))
    end_x = x_2 - (length_ * math.cos(angle_in_rad))
    kanina = end_y #+ ((end_x) * (0-1) * math.tan(angle_in_rad))
    hypotenuse = ((x_2-end_x)**2.0 + (y_2-end_y)**2)**0.5
    



def pos_obj():
    """ to calculate the x and y coordinate of an object on the inclined plane for each object depending on the angle of inclined plane and the distance from the fiex end"""
    
    set_angle()
    obj_size()

    global points_box, points_ball, points_toy,sasuke,naruto, adjust_x, adjust_y
    naruto = dist_on_plane.get()
    sasuke = 15 - naruto

    if angle_in_rad > 0:
        #use multiple of 15
        adjust_x = 27 * sasuke * math.cos(angle_in_rad)
        adjust_y = 27 * sasuke * math.sin(angle_in_rad)
        
    else:
        adjust_x = 0
        adjust_y = 0

    if abc == 0:
        adjust_x = 27 * sasuke
        adjust_y = 0

    if abc == 90:
        adjust_x = 0
        adjust_y = 27 * sasuke

    #For box
    global points_box, points_ball, points_toy ,angle_left
    global rec_bottom_left_x,rec_bottom_left_y,rec_upper_left_x,rec_upper_left_y,rec_upper_right_x,rec_upper_right_y,rec_bottom_right_x,rec_bottom_right_y, rec_bottom_left, toy_bottom_right_x,toy_bottom_right_y
    global new_r_b_x , new_r_b_y , toy_bottom_right_x, toy_bottom_right_y 
    angle_left = (math.pi/2)- angle_in_rad
    rec_bottom_left_x = end_x
    rec_bottom_left_y = end_y 
    rec_upper_left_y = end_y - (ball_height* math.cos(angle_in_rad))
    rec_upper_left_x = ball_height* math.sin(angle_in_rad)+ end_x 
    rec_upper_right_y = rec_upper_left_y + (ball_width * math.sin(angle_in_rad))
    rec_upper_right_x = rec_upper_left_x + (ball_width * math.cos(angle_in_rad))
    rec_bottom_right_y = rec_upper_right_y + (ball_height * math.cos(angle_in_rad))
    rec_bottom_right_x = rec_upper_right_x - (ball_height * math.sin(angle_in_rad))
    new_r_b_x = rec_bottom_right_x+adjust_x
    new_r_b_y = rec_bottom_right_y+adjust_y
    
    
    points_box = [rec_bottom_left_x+adjust_x, rec_bottom_left_y + adjust_y ,rec_upper_left_x+adjust_x,rec_upper_left_y+adjust_y,rec_upper_right_x+adjust_x,rec_upper_right_y+adjust_y,new_r_b_x,new_r_b_y, rec_bottom_left_x+adjust_x, rec_bottom_left_y +adjust_y]



    #For toys
    toy_bottom_right_x = rec_bottom_right_x + (ball_height * math.sin(angle_left))+adjust_x
    toy_bottom_right_y = rec_bottom_right_y + (ball_width * math.cos(angle_left))+adjust_y
    points_toy = [rec_bottom_left_x+adjust_x, rec_bottom_left_y + adjust_y ,rec_upper_left_x+adjust_x,rec_upper_left_y+adjust_y,rec_upper_right_x+adjust_x,rec_upper_right_y+adjust_y,toy_bottom_right_x ,toy_bottom_right_y ,rec_bottom_left_x+adjust_x, rec_bottom_left_y+adjust_y]
   


    #For ball
    points_ball = [rec_bottom_left_x+adjust_x,rec_upper_left_y+adjust_y,rec_upper_right_x +adjust_x, new_r_b_y]
    

def c_o_fric():
    """ to obtain the coefficient of friction from the slider"""
    global aaa, count_place
    aaa = c_o_f.get()
    agent_si = 0.00 * aaa
    count_place = float("%.2f" % agent_si)

    
def obtain_data():
    """ To obain or calculate all the necessary data when an object sliding down"""
    global grav_force, fric_force, acc, hypoten, accele, time_taken ,fin_vel ,time_1, fric_f, gra_f, final_v
    set_angle()
    c_o_fric()
    obj_size()
    pos_obj()
    if math.sin(angle_in_rad) == 0:
        acc = 0
        timee = 0
        fric_force = 0
        fric_grav = 0
    else:
        acc = float("%.3f" % (9.81 * (math.sin(angle_in_rad) - aaa*math.cos(angle_in_rad))))

    grav_force = float("%.3f" % (heavy * 9.81 * math.sin(angle_in_rad)))
    
    
    fric_force = float("%.3f" % (heavy * 9.81 * math.cos(angle_in_rad) * aaa))

    time_1 = 0
    if grav_force > fric_force:
        time_1 = float("%.2f" % ((2.0* naruto)/acc)** 0.5)
    
    else:
        acc = 0
        time_1 = 0
    
    
    final_v = float("%.1f" % (acc * time_1))

    hypoten = "Distance","travelled" , ":", naruto , "m"
    accele = "Acceleration" , ":", acc , "m/s^2"
    time_taken = "Total","time" , ":", time_1 , "s"
    gra_f = "Gravitational","force" , ":", grav_force, "N"
    fric_f = "Frictional","force" , ":", fric_force, "N"
    fin_vel = "Final","velocity" , ":", final_v, "m/s"

    
    
    
    
def showin_data():
    """To show the data and value of and object sliding down the plane"""
    main_2 = tk.Toplevel(root,bg="lavenderblush")
    main_2.title("What happens !?!")
    
    obtain_data()
    set_angle()
    c_o_fric()

    if angle_in_rad == 0:
        a123_ = "Please","set","an", "angle!"
    elif abc == 90:
        a123_ = "Object", "is","experiencing","free","falling"
        a321_ = "without","any","air","resistance","or","frictional", "force!"

    elif aaa == 0 and angle_in_rad != 0:
        a123_ = "The" ,"gravitational", "force","parallel","to","the","plane","is", grav_force,"N"
        a321_ = "and", "is", "larger", "than",  "kinetic","friction" ,"force" ,"of",fric_force,"N."
        a331_ = "Hence,", "object", "can", "slide","down","with","acceleration","of",acc, "ms⁻²."

    elif grav_force > fric_force:
        a123_ = "The" ,"gravitational", "force","parallel","to","the","plane","is", grav_force,"N"
        a321_ = "and", "is", "larger", "than",  "kinetic","friction" ,"force" ,"of",fric_force,"N."
        a331_ = "Hence,", "object", "can", "slide","down","with","reduced","acceleration","of",acc, "ms⁻²."
    elif grav_force < fric_force:
        a123_ = "The" ,"gravitational", "force","parallel","to","the","plane","is", grav_force,"N"
        a321_ = "and", "is", "smaller", "than", "static", "friction" ,"force" ,"of", fric_force,"N."
        a331_ = "Hence,", "object", "cannot", "move!"

    else:
        a123_ = "The" ,"gravitational", "force","parallel","to","the","plane"
        a321_ = "is","same","as","the","maximum","static","friction","force"
        a331_ = "So,","object","cannot","move!"
        
            
        
    if angle_in_rad == 0:
        reason_motion_0 = tk.Label(main_2, text = a123_,bg="lavenderblush")
        reason_motion_0.pack()
        reason_motion_0.configure(font=("Segeo UI historic",10))
    elif abc == 90:
        reason_motion_001 = tk.Label(main_2, text = a123_,bg="lavenderblush")
        reason_motion_001.pack()
        reason_motion_001.configure(font=("Segeo UI historic",10))

        reason_motion_002 = tk.Label(main_2, text = a321_,bg="lavenderblush")
        reason_motion_002.pack()
        reason_motion_002.configure(font=("Segeo UI historic",10))
        
    else:
        reason_motion = tk.Label(main_2, text = a123_,bg="lavenderblush")
        reason_motion.pack()
        reason_motion.configure(font=("Segeo UI historic",10))

        reason_motion_1 = tk.Label(main_2, text = a321_,bg="lavenderblush")
        reason_motion_1.pack()
        reason_motion_1.configure(font=("Segeo UI historic",10))

        reason_motion_2 = tk.Label(main_2, text = a331_,bg="lavenderblush")
        reason_motion_2.pack()
        reason_motion_2.configure(font=("Segeo UI historic",10))
    
def back():
    global root
    root.destroy()
    execfile ("Homepage_2.py")

class A:
    
    def __init__(self, master):
        
        
        self.label_2=tk.Label(master,bg = "thistle1")
        self.label_2.grid(row=0, column=0)
        self.label_2.configure(text='',font=("Century Gothic", 11))
        self.count_2 = 0
        self.list_1 = []
        self.update_label_2()
        self.list_1 = []
        

        self.label_3=tk.Label(master,bg = "thistle1")
        self.label_3.grid(row=2, column=0)
        self.label_3.configure(text='',font=("Century Gothic", 11))
        self.count_3 = 0
        self.sec = 0
        self.update_label_3()

        
        self.label_4=tk.Label(master,bg = "thistle1")
        self.label_4.grid(row=4, column=0)
        self.label_4.configure(text='',font=("Century Gothic", 11))
        self.count_4 = 0
        self.count_lite = 0
        self.sec_1 = 0
        
        self.update_distance()

        


    def update_label_2(self):
        
        if status == True and self.count_2 <= agent_time:
                
                count_self_2 = float(self.count_2)
                text_21 = "Time:", count_self_2,"x", "10⁻²", "s"
                self.label_2.configure(text = text_21,width=40)
                self.label_2.after(10, self.update_label_2) # call this method again in 1,000 milliseconds
                self.count_2 += (1)
                
        
                
            
            
    def update_label_3(self):
        if status == True and self.count_3 <= agent_move:
        
                count_self_3 = float("%.2f" % self.count_3)
                text_23 = "Velocity:", count_self_3,"ms⁻¹"
                self.label_3.configure(text = text_23,width=40)
                self.count_3_assist = 0
                self.count_3_assist += (1)
                self.label_3.after(10, self.update_label_3)
                self.sec += 1
                self.list_1.append(self.sec)
                self.count_3 += (self.count_3_assist/100.0)* acc
                self.list_1.append(self.count_3)
                
                
                
        

    def update_distance(self):
        count = 0
        if status == True and self.sec_1 <= agent_time:
            count_self_4 = float("%.2f" % self.count_4)
            hello_bye = "Distance","travelled:",count_self_4,"m"
            self.label_4.configure(text = hello_bye,width=40)
            self.count_4_assist = 1
            self.list_2 = []
            
            if grav_force <= fric_force:
                self.label_4.after(10, self.update_distance)
                self.sec_1 += 1
                self.list_2.append(self.sec_1)
                self.count_4 = 0.00
                self.list_2.append(self.count_4)
            elif grav_force > fric_force:
                self.label_4.after(10, self.update_distance)
                self.sec_1 += 1
                self.list_2.append(self.sec_1)
                self.count_lite += (self.count_4_assist/100.0)* acc
                self.count_4 = (self.count_lite ** 2.0 / (2*acc))
                self.list_2.append(self.count_4)
        






     
            
        
def important_for_class():
    c_o_fric()
    set_angle()
    
    if aaa == 1:
        aa_left = 1 - aaa + 0.2
    else:
        aa_left = 1- aaa + 0.2


    
    if 50< abc < 90:
        shift_x = 3 * math.cos(angle_in_rad) * aa_left
        shift_y = 3 * math.sin(angle_in_rad) * aa_left
    elif abc == 90:
        shift_x = 3.69 * math.cos(angle_in_rad)
        shift_y = 3.69 * math.sin(angle_in_rad)
    elif abc == 0:
        shift_x = 0
        shift_y = 0
    elif 14< abc < 20:
        shift_x = 1.33 * math.cos(angle_in_rad)
        shift_y = 1.33 * math.sin(angle_in_rad)
    elif abc < 14:
        shift_x = math.cos(angle_in_rad)
        shift_y = math.sin(angle_in_rad)
    elif grav_force <= fric_force:
        shift_x = 0
        shift_y = 0
    else:
        shift_x = math.cos(angle_in_rad) * aa_left * 2.2
        shift_y = math.sin(angle_in_rad) * aa_left * 2.2
                

    hypon = (((end_x + adjust_x )-x_2)**2.0 +((end_y+adjust_y )-y_2)**2) ** 0.5
        
    shift_shift_x = shift_x
    shift_shift_y = shift_y

    tenuse = ((shift_shift_x)**2.0 +(shift_shift_y)**2) ** 0.5
    global agent_move, agent_time, agent_place, count_place

    if grav_force <= fric_force:
        agent_time = 0
        agent_move = 0
        agent_place = 0
        
    else:
        
        agent_abc = ((hypon/ tenuse))

        agent_time = int(agent_abc)
        agent_move = float( acc* (agent_time/100.0))
        
        agent_place = (agent_move**2) / (2* acc)
        if angle_in_rad == 0:
            agent_place = 0

        count_place = float("%.2f" % agent_place)
        
    
def data_class():
    global veloo , distt,tim
    important_for_class()
    veloo = []
    xxx_vel = 0
    xxx_dist = 0
    xxx_time = 0
    tim = [] 
    distt = []

    if grav_force <=fric_force:
        xxx_vel = 0
        xxx_dist = 0
    else:
        while xxx_vel <= agent_move:
            xxx_vel += (1/100.0)* acc
            veloo.append(xxx_vel)

            xxx_dist = (xxx_vel **2) / (2* acc)
            distt.append(xxx_dist)

            xxx_time += 0.01
            tim.append(xxx_time)
        



def velocity_gr():
    data_class()
    plt.clf()
    x = tim
    y = veloo
    plt.plot(x,y)
    plt.xlabel('Time (s)')
    # naming the y axis
    plt.ylabel('Velocity (ms^-1)')
    # giving a title to my graph
    plt.title('Velocity Time Graph')

    # function to show the plot
    plt.show()



def dist_gr():
    data_class()
    plt.clf()
    x = tim
    y = distt
    plt.plot(x,y)
    plt.xlabel('Time (s) ')
    # naming the y axis
    plt.ylabel('Distance (m) ')
    # giving a title to my graph
    plt.title('Distance Time Graph')

    # function to show the plot
    plt.show()



    
def velocity_update():
    obtain_data()
    obj_size()
    c_o_fric()
    set_angle()
    important_for_class()
    A(frame_1)
    data_class()
    #update_distance()

def distance_update():
    set_angle()
    pos_obj()
    c_o_fric()
    #B(frame_2)
    #C(frame_3)


def rad_2():
    """To determine the x and y coordinate of each corner of the inclined plane"""
    #Part 1
    set_angle()
    obj_size()
    pos_obj()

    
    c.delete(tk.ALL)
    c.create_image(0,0,image = log , anchor = "nw")
    draw_plane(end_x, end_y)
    
    if kanina == y_2:
        c.create_line(end_x, y_2, x_2 , y_2, fill='Gray22')
    if end_x == x_2:
        c.create_line(x_2, y_2, end_x , end_y, fill='Gray22')


def draw_plane(x_1,y_1):
    """ To plot the inclined plane on the canvas"""
    points = [x_2,y_2,x_1,y_1,x_1,y_2,x_2,y_2]
    c.create_polygon(points, fill='Gray22')

    
def obj_slidin(x):
    """To allow users to choose which object to slide down the inclined plane"""
    ali = x, 21
    set_angle()
    global circle , x_obj
    x_obj = root.v.get()
    pos_obj()
        
    if x_obj == "box":
        c.delete(tk.ALL)
        rad_2()
        circle = c.create_polygon(points_box,fill="sienna4")
        mainom.place(x= 494, y=458)
        
    if x_obj == "ball" :
        c.delete(tk.ALL)
        rad_2()
        circle = c.create_oval(points_ball,fill="SlateGray3")
        mainom.place(x= 495, y=458)
             
    if x_obj == "trapezium":
        c.delete(tk.ALL)
        rad_2()
        circle = c.create_polygon(points_toy,fill= "red3")
        mainom.place(x= 461, y=458)
        
        
def motion_15(x):
    """To allow the users to change the distance of an object on the inclined plane from the fixed points"""
    nanin = x,21
    c.delete(tk.ALL)
    obj_slidin(2)
    pos_obj()
    c_o_fric()
    obtain_data()
    important_for_class()
    
    set_angle()
    if angle_in_rad ==0:
        test_input_1 = "0.00","m"
        text_test_var.set(test_input_1)
    else:
        test_input = count_place, "m"
        text_test_var.set(test_input)
        

def bigger_smaller(x):
    """To show the change in mass and volume of the object """
    nanii = x, 21
    c.delete(tk.ALL)
    pos_obj()
    obj_size()
    obj_slidin(2)

def incline_angle(x):
    """To allow the inclined plane to change its angle together with the object on it"""
    defuq = x ,21
    set_angle()
    rad_2()
    bigger_smaller(2)
    pos_obj()
    motion_15(2)
    abc_plus_deg = abc , u"\N{DEGREE SIGN}"
    show_angle_var.set(abc_plus_deg)




def moveball():
    """To determine how much the object has to slide going down the inclined plane"""
    #Part 1
    set_angle()
    
    #Part 2
    pos_obj()
    c_o_fric()
    
    
    obj_slidin(3)
     
        
    #total_move = ((shift_x) **2 + (shift_y)** 2 ) ** 0.5

    total_slide_distance = 0
    
    if x_obj == "box":
        total_slide_distance = ((x_2 - end_x)**2 + (y_2 - end_y)**2)**0.5       
        
    if x_obj == "ball":
        total_slide_distance = ((x_2 - end_x)**2 + (y_2 - end_y)**2)**0.5
    if x_obj == "trapezium":
        total_slide_distance = ((x_2 - end_x)**2 + (y_2 - end_y)**2)**0.5

        
    #Part 3
    #pause_butt()
    #resume_butt()
    
    if aaa == 1:
        aa_left = 1 - aaa + 0.2
    else:
        aa_left = 1- aaa + 0.2
    global new_l_b_y, end_new
    
    new_l_b_y = rec_bottom_left_y + adjust_y
    end_new_y = end_y
    end_new = end_new_y + adjust_y
    global T_O_F

    obtain_data()

    grav_var = tk.StringVar()

    g_force = tk.Label(root, textvariable=grav_var,bg="plum2",width=25)
    g_force.place(x=130,y=430)
    g_force.config(font=("Lucida Sans", 11))
    #root.wm_attributes("-transparentcolor", 'plum1')

    
    fric_var = tk.StringVar()
    f_force = tk.Label(root, textvariable=fric_var,bg="plum2",width=25)
    f_force.place(x=130,y=450)
    f_force.config(font=("Lucida Sans", 11))
    data_for_force = "Gravitational" ,"force:",grav_force,"N"
    grav_var.set(data_for_force)

    data_for_fric = "Frictional","force:",fric_force,"N"
    fric_var.set(data_for_fric) 


    while new_l_b_y <= y_2 or end_new < y_2 :
        if status:
            #obtain_data_from_class()
            if 50< abc < 90:
                shift_x = 3 * math.cos(angle_in_rad) * aa_left 
                shift_y = 3 * math.sin(angle_in_rad) * aa_left
            elif abc == 90:
                shift_x = 3.69 * math.cos(angle_in_rad)  
                shift_y = 3.69 * math.sin(angle_in_rad)
            elif abc == 0:
                shift_x = 0
                shift_y = 0
            elif 14< abc < 20:
                shift_x = 1.33 * math.cos(angle_in_rad)  
                shift_y = 1.33 * math.sin(angle_in_rad)
            elif abc < 14:
                shift_x = math.cos(angle_in_rad)  
                shift_y = math.sin(angle_in_rad)
            
            else:
                shift_x = math.cos(angle_in_rad) * aa_left * 2.2
                shift_y = math.sin(angle_in_rad) * aa_left * 2.2

            if grav_force <= fric_force:
                shift_x = 0
                shift_y = 0
            T_O_F = False
            
            new_l_b_y += shift_y
            end_new +=shift_y
        
            c.move(circle, shift_x, shift_y)
            root.update()
            time.sleep(0.01)
            
        else:
            T_O_F = True
            break
    

    
frame_3  =tk.Frame(root , bg = "thistle1")
frame_3.grid(row = 1 , column = 0)
frame_3.config(highlightbackground = "black", highlightcolor= "black")

        


def start_ani():
    '''To animate the motion of an object going down the slide'''
    obj_slidin(3)
    
    
    obtain_data()


    global status

    status = True
    reset = False

    
    
    ok.config(fg="thistle1" ,highlightbackground="thistle1",\
              highlightcolor="thistle1",\
              highlightthickness=4,bd=0,state = "disabled", bg="thistle1",height=0,font = ("Nirmala UI", "8"),disabledforeground="thistle1")
    

    
    
    def motion1():
        

        anime_button.config(state = "disabled" ,bg="snow3",fg = "grey",height=2)

        pause_button.config(state = "normal" ,bg="red",fg = "black",height=2)


        reset_button.config(state = "normal" ,bg = "goldenrod1", fg = "black",height=2)
        
        global reset,status
        reset = True
        obtain_data()
        set_angle()
        velocity_update()
        
        while reset:
            if status:
                
                if grav_force > fric_force :
                    c_o_fric()
                    acceleration_shown = "Acceleration", ":",acc , "ms⁻²"
                    show_acc_var.set(acceleration_shown)
                    
                    moveball()
                    
                    
                    """if T_O_F == False:
                        pause_button.config(text = "Restart\n Animation" , bg = "goldenrod1", \
                                state = "normal", fg = "black")"""
                    break
                   

                    
    
                else:                        
                    acceleration_shown = "Acceleration", ":","0.00" , "ms⁻²"
                    show_acc_var.set(acceleration_shown)
                    moveball()
                    
            if not reset:
                break

            if not status:
                break

            pos = c.coords(circle)
            

            if pos[3] > high:
                pause_button.config(state = "disabled", bg="brown4",fg = "grey")
                break
            
    def pausebut():
        pos_obj()

        global status

        if status:
            status = False
            pause_button.config(text = "Replay" , bg = "green", \
                                state = "normal", fg = "black",height=2)
        
            
                      
        else:
            status = True
            pause_button.config(text = "Pause" , bg = "red", \
                                state = "normal", fg = "black",height=2)

            # continue the animation
            motion1()

    
       
    def resetkey():
        '''
        function for reset the animation
        '''

        global reset, status

        pos_obj()

        

        status = True

        reset = False
    
        c.delete(tk.ALL)

        #obj_slidin(2)
        rad_2()

        text_47 = "Time:","0",".00", "x", "10⁻²", "s"
        Label_1 = tk.Label(frame_1, text = text_47,bg = "thistle1")
        Label_1.config(font=("Century Gothic", 11))
        Label_1.grid(row=0,column=0,sticky='nwse')

        text_57 = "Velocity:",  "0",".00", "ms⁻¹"
        Label_2 = tk.Label(frame_1, text = text_57,bg = "thistle1")
        Label_2.config(font=("Century Gothic", 11))
        Label_2.grid(row=2,column=0,sticky='nwse')

        text_67 = "Distance", "travelled:","0",".00", "m"
        Label_3 = tk.Label(frame_1, text = text_67,bg = "thistle1")
        Label_3.config(font=("Century Gothic", 11))
        Label_3.grid(row=4,column=0,sticky='nwse')
        
        zero_acc = "0.00"
        acceleration_shown = "Acceleration", ":", zero_acc , "ms⁻²"
        show_acc_var.set(acceleration_shown)


        anime_button.config(state = "normal", bg="white", fg = "black",height=2)

        pause_button.config(text = "Pause" , bg = "brown4", state = "disabled",\
                            fg = "grey",height=2)

        reset_button.config(state = "disabled",bg="DarkGoldenrod4" ,fg = "grey",height=2)



    anime_button = tk.Button(frame_3, text="Start Animation", \
                          state="normal",bg="snow",  height=2,command= motion1)
    anime_button.grid(row = 0, column = 1, padx=5, pady=5)
    anime_button.configure (relief = "solid", width = 15, height = 2, borderwidth = 1)

    pause_button = tk.Button(frame_3, text="Pause", bg="brown4",height=2,command=pausebut, state="disabled", fg="grey")
    pause_button.grid(row = 0, column = 2, padx=5, pady=5)
    pause_button.configure (relief = "solid", width = 10, height = 2, borderwidth = 1)

    reset_button = tk.Button(frame_3, text="Reset", height=2,command=resetkey, \
                          state = "disabled" ,bg="DarkGoldenrod4", fg = "grey")
    reset_button.grid(row = 0, column = 3, padx=5, pady=5)
    reset_button.configure (relief = "solid", width = 10, height = 2, borderwidth = 1)
      
    
        

                


#These are the widgets used in the application
##show_data = tk.Button(root, text="Show Data", command=showin_data)
##show_data.grid()



frame_2 = tk.Frame(root ,bg = 'lavenderblush')
#frame_2.grid(row =0, column = 5 , padx = 10, pady =10)
frame_2.place(x=630, y= 100)
frame_2.configure (relief = "solid", width = 31, height = 1, borderwidth = 1)
label_chem = tk.Label(frame_2, text='INPUTS')
label_chem.grid(row=0, column=2, padx=5, pady=5)
label_chem.configure( bg = "lavenderblush")






dist_on_plane= tk.Scale(frame_2, from_ = 15, to = 0,fg = "lavenderblush" ,bg = "lavenderblush",command= motion_15, resolution = 0.1, orient="horizontal" )
dist_on_plane.set(15)
dist_on_plane.grid(row=4, column=3, padx=5, pady=10)

text_test_var = tk.StringVar()
ideal_dist = tk.Label(frame_2, bg="lavenderblush", fg =  "black", textvariable = text_test_var)
ideal_dist.place(x=222,y=145)




w5 = tk.Label(frame_2 ,  text = "Mass(kg)")
w5.grid(row = 5 , column = 1 , padx =5 ,pady =5)
w5.configure( bg = "lavenderblush")
weight_scale= tk.Scale(frame_2,from_ = 0, to = 100,command=bigger_smaller,resolution = 0.1,orient="horizontal", bg = "lavenderblush")
weight_scale.set(0.1)
weight_scale.grid(row = 5 ,column = 3 , padx =5 , pady =5)







optionList = ('box', 'ball', 'trapezium')
root.v = tk.StringVar()
root.v.set(optionList[0])
mainom = tk.OptionMenu(root, root.v, *optionList, command=obj_slidin)
mainom.place(x= 496, y=460)
mainom.config(bg='thistle1')
mainom["menu"].config(bg='thistle1')
#mainom.grid(padx=5, pady=5)



ok= tk.Button(frame_3, text="Ready to start application", command=start_ani,height=2,font = ("Nirmala UI", "13") ,fg="snow",bg="DarkOrchid2")

ok.grid(row =0, column = 1, padx=5, pady=5)
ok.configure (relief = "solid", width = 21, height = 2, borderwidth = 1)



text_99 = 'Ramp', 'angle', "(",u"\N{DEGREE SIGN}",")"
label_glyc = tk.Label(frame_2,  text=text_99)
label_glyc.grid(row=2, column=1, padx=5, pady=5)
label_glyc.configure( bg = "lavenderblush")
ptptangle=tk.Scale(frame_2, from_ = 0, to = 90, command=incline_angle, orient="horizontal", bg = "lavenderblush")
ptptangle.grid(row=2, column=3, padx=5, pady=5)
ptptangle.set(0)


label_nic = tk.Label(frame_2,  text='Coefficient of Friction')
label_nic.grid(row=1, column=1, padx=5, pady=5)
label_nic.configure( bg = "lavenderblush")
c_o_f =tk.Scale(frame_2, from_ = 0, to = 1, digits = 3, resolution = 0.01, orient="horizontal", bg = "lavenderblush")
c_o_f.grid(row=1, column=3, padx=5, pady=5)






label_gli = tk.Label(frame_2 , text="Distance(m)")
label_gli.grid(row=4, column=1, padx=5, pady=5)
label_gli.configure( bg = "lavenderblush")

def text():
     #os.startfile("MY_own.pyc")
    os.startfile("notepad functi .py")

    
frame_4 = tk.Frame(root, bg = "lavenderblush")
frame_4.config(relief = "solid", width = 31, height = 1, borderwidth = 1)
#frame_4.grid(row = 4 , column = 5, padx = 10, pady = 10)
frame_4.place(x=660,y=520)
bt = tk.Button(frame_4, text = " Velocity Time graph" , command = velocity_gr, bg = "DarkOrchid2", fg="snow",font = ("Adobe Song Std", "10"))
bt.grid(row =2 , column = 1 , columnspan = 3 , pady = 5 , padx = 5)
bt.configure(relief = "solid", width = 31, height = 1, borderwidth = 1)
nt = tk.Button(frame_4, text = " Notepad"  , command = text, bg = "DarkOrchid2",fg="snow", font = ("Adobe Song Std", "10"))
nt.grid(row = 6 , column = 1 , padx = 5 ,  pady = 5 , columnspan = 3)
nt.configure(relief = "solid", width = 31, height = 1, borderwidth = 1)
dt = tk.Button(frame_4, text = " Distance Time graph" , command =  dist_gr , bg = "DarkOrchid2",fg="snow", font = ("Adobe Song Std", "10"))
dt.grid(row = 4 , column = 1 , padx = 5 ,  pady = 5 , columnspan = 3,sticky='nwse')
gh = tk.Button(frame_4, text = " Explanation" , command = showin_data, bg = "DarkOrchid2",fg="snow", font = ("Adobe Song Std", "10"))
gh.grid(row = 8 , column = 1 , padx = 5 ,  pady = 5 , columnspan = 3,sticky='nwse')
gh.configure (relief = "solid", width = 31, height = 1, borderwidth = 1)
dt.configure (relief = "solid", width = 31, height = 1, borderwidth = 1)

show_angle_var = tk.StringVar()
show_angle = tk.Label(root, textvariable=show_angle_var,bg="grey78")
show_angle.place(x=380,y=403)
#grid(row=2, column=4 , padx=5, pady=5)



show_acc_var = tk.StringVar()
show_acc = tk.Label(frame_1, textvariable=show_acc_var,bg ="thistle1")


show_acc.config(font=("Century Gothic", 11))
show_acc.grid(row=45, column=0 , padx=5, pady=5)
#r 45 c 0



pic_help0 = Image.open ("Help.gif")
pic_help0 = pic_help0.resize((35, 35), Image.ANTIALIAS)
pic_help = ImageTk.PhotoImage(pic_help0)
pic_bac = Image.open ("back_1.gif")
pic_bac = pic_bac.resize((35,35), Image.ANTIALIAS)
pic_back = ImageTk.PhotoImage(pic_bac)
button_back = tk.Button (root, image = pic_back, command = back , text = " Back ", fg="snow",font = ("Adobe Song Std", "16"),compound = tk.RIGHT, relief = "solid")
button_back.place(x = 0, y = 700, anchor = "nw")
button_back.config(highlightbackground = "black", highlightcolor= "black")
##place (x = 837, y = 445, anchor = "nw")
button_back.configure (width = 110, heigh = 25, borderwidth = 1, bg = "DarkOrchid2")


button_help = tk.Button(root, text = "  Help!", image = pic_help, compound = tk.RIGHT, fg="snow",relief = "solid",font = ("Adobe Song Std", "16"), command = help_1)
button_help.configure(height = 25, width = 110, borderwidth =1, bg = "DarkOrchid2")
button_help.place(x = 961, y = 700, anchor = "nw")



root.resizable(False,False)
root.mainloop()
