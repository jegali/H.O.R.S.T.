# openCV must be installed by
# pip install opencv-python
import cv2
import numpy as np


# state stores the cube configuration
# initially, every facelet will be set to white
state=  {
            'up':['white','white','white','white','white','white','white','white','white',],
            'right':['white','white','white','white','white','white','white','white','white',],
            'front':['white','white','white','white','white','white','white','white','white',],
            'down':['white','white','white','white','white','white','white','white','white',],
            'left':['white','white','white','white','white','white','white','white','white',],
            'back':['white','white','white','white','white','white','white','white','white',]
        }

sticker_size_recog = 50
sticker_size=30
sticker_padding = 4
padding = 20

left_sticker_x = padding
front_sticker_x = left_sticker_x + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
right_sticker_x = front_sticker_x + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
back_sticker_x = right_sticker_x + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
up_sticker_x = front_sticker_x
down_sticker_x = front_sticker_x

up_sticker_y = padding
left_sticker_y = up_sticker_y + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
front_sticker_y = up_sticker_y + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
right_sticker_y = up_sticker_y + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
back_sticker_y = up_sticker_y + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size
down_sticker_y = left_sticker_y + 2*(sticker_size + sticker_padding) + 2*sticker_padding + sticker_size

current_sticker_x = front_sticker_x
current_sticker_y = 400

# these arrays hold the position of
# main:     the facelets to present the cube in the camera
# current:  the facelets that show the recognized cube facelets
# left:     facelets of the left side
# ...

# current has flipped x axes - because the web cam picture is flipped for convenience
stickers = {
        'main': [
            [400, 400], [500, 400], [600, 400],
            [400, 500], [500, 500], [600, 500],
            [400, 600], [500, 600], [600, 600]
        ],
        'current': [
            [current_sticker_x, current_sticker_y], [current_sticker_x + (sticker_size + sticker_padding), current_sticker_y], [current_sticker_x + 2*(sticker_size + sticker_padding), current_sticker_y],
            [current_sticker_x, current_sticker_y + (sticker_size + sticker_padding)], [current_sticker_x + (sticker_size + sticker_padding), current_sticker_y + (sticker_size + sticker_padding)], [current_sticker_x + 2*(sticker_size + sticker_padding), current_sticker_y + (sticker_size + sticker_padding)],
            [current_sticker_x, current_sticker_y + 2*(sticker_size + sticker_padding)], [current_sticker_x + (sticker_size + sticker_padding), current_sticker_y + 2*(sticker_size + sticker_padding)], [current_sticker_x + 2*(sticker_size + sticker_padding), current_sticker_y + 2*(sticker_size + sticker_padding)]
        ],
        'left': [
            [left_sticker_x, left_sticker_y], [left_sticker_x + (sticker_size + sticker_padding), left_sticker_y], [left_sticker_x + 2*(sticker_size + sticker_padding), left_sticker_y],
            [left_sticker_x, left_sticker_y + (sticker_size + sticker_padding)], [left_sticker_x + (sticker_size + sticker_padding), left_sticker_y + (sticker_size + sticker_padding)], [left_sticker_x + 2*(sticker_size + sticker_padding), left_sticker_y + (sticker_size + sticker_padding)],
            [left_sticker_x, left_sticker_y + 2*(sticker_size + sticker_padding)], [left_sticker_x + (sticker_size + sticker_padding), left_sticker_y + 2*(sticker_size + sticker_padding)], [left_sticker_x + 2*(sticker_size + sticker_padding), left_sticker_y + 2*(sticker_size + sticker_padding)]
        ],
        'front': [
            [front_sticker_x, front_sticker_y], [front_sticker_x + (sticker_size + sticker_padding), front_sticker_y], [front_sticker_x + 2*(sticker_size + sticker_padding), front_sticker_y],
            [front_sticker_x, front_sticker_y + (sticker_size + sticker_padding)], [front_sticker_x + (sticker_size + sticker_padding), front_sticker_y + (sticker_size + sticker_padding)], [front_sticker_x + 2*(sticker_size + sticker_padding), front_sticker_y + (sticker_size + sticker_padding)],
            [front_sticker_x, front_sticker_y + 2*(sticker_size + sticker_padding)], [front_sticker_x + (sticker_size + sticker_padding), front_sticker_y + 2*(sticker_size + sticker_padding)], [front_sticker_x + 2*(sticker_size + sticker_padding), front_sticker_y + 2*(sticker_size + sticker_padding)]
        ],
        'right': [
            [right_sticker_x, right_sticker_y], [right_sticker_x + (sticker_size + sticker_padding), right_sticker_y], [right_sticker_x + 2*(sticker_size + sticker_padding), right_sticker_y],
            [right_sticker_x, right_sticker_y + (sticker_size + sticker_padding)], [right_sticker_x + (sticker_size + sticker_padding), right_sticker_y + (sticker_size + sticker_padding)], [right_sticker_x + 2*(sticker_size + sticker_padding), right_sticker_y + (sticker_size + sticker_padding)],
            [right_sticker_x, right_sticker_y + 2*(sticker_size + sticker_padding)], [right_sticker_x + (sticker_size + sticker_padding), right_sticker_y + 2*(sticker_size + sticker_padding)], [right_sticker_x + 2*(sticker_size + sticker_padding), right_sticker_y + 2*(sticker_size + sticker_padding)]
        ],
        'up': [
            [up_sticker_x, up_sticker_y], [up_sticker_x + (sticker_size + sticker_padding), up_sticker_y], [up_sticker_x + 2*(sticker_size + sticker_padding), up_sticker_y],
            [up_sticker_x, up_sticker_y + (sticker_size + sticker_padding)], [up_sticker_x + (sticker_size + sticker_padding), up_sticker_y + (sticker_size + sticker_padding)], [up_sticker_x + 2*(sticker_size + sticker_padding), up_sticker_y + (sticker_size + sticker_padding)],
            [up_sticker_x, up_sticker_y + 2*(sticker_size + sticker_padding)], [up_sticker_x + (sticker_size + sticker_padding), up_sticker_y + 2*(sticker_size + sticker_padding)], [up_sticker_x + 2*(sticker_size + sticker_padding), up_sticker_y + 2*(sticker_size + sticker_padding)]
        ],
        'down': [
            [down_sticker_x, down_sticker_y], [down_sticker_x + (sticker_size + sticker_padding), down_sticker_y], [down_sticker_x + 2*(sticker_size + sticker_padding), down_sticker_y],
            [down_sticker_x, down_sticker_y + (sticker_size + sticker_padding)], [down_sticker_x + (sticker_size + sticker_padding), down_sticker_y + (sticker_size + sticker_padding)], [down_sticker_x + 2*(sticker_size + sticker_padding), down_sticker_y + (sticker_size + sticker_padding)],
            [down_sticker_x, down_sticker_y + 2*(sticker_size + sticker_padding)], [down_sticker_x + (sticker_size + sticker_padding), down_sticker_y + 2*(sticker_size + sticker_padding)], [down_sticker_x + 2*(sticker_size + sticker_padding), down_sticker_y + 2*(sticker_size + sticker_padding)]
        ], 
        'back': [
            [back_sticker_x, back_sticker_y], [back_sticker_x + (sticker_size + sticker_padding), back_sticker_y], [back_sticker_x + 2*(sticker_size + sticker_padding), back_sticker_y],
            [back_sticker_x, back_sticker_y + (sticker_size + sticker_padding)], [back_sticker_x + (sticker_size + sticker_padding), back_sticker_y + (sticker_size + sticker_padding)], [back_sticker_x + 2*(sticker_size + sticker_padding), back_sticker_y + (sticker_size + sticker_padding)],
            [back_sticker_x, back_sticker_y + 2*(sticker_size + sticker_padding)], [back_sticker_x + (sticker_size + sticker_padding), back_sticker_y + 2*(sticker_size + sticker_padding)], [back_sticker_x + 2*(sticker_size + sticker_padding), back_sticker_y + 2*(sticker_size + sticker_padding)]
        ],
}

faces = ("Show blue face, white face up", "Show orange face, white face up", "Show green face, white face up", "Show white face, blue face up", "Show yellow face, green face up", "Show red face, white face up")
face_colors = ("back", "left", "front", "up", "down", "right")
face_stickers = ("B", "L", "F", "U", "D", "R")
current_face = 0



#YELLOW_MIN = cv2.Scalar(22,95,123)
#YELLOW_MAX = cv2.Scalar(60,255,195)
#WHITE_MIN = cv2.Scalar(26,38,139)
#WHITE_MAX = cv2.Scalar(128,170,255)
#ORANGE_MIN = cv2.Scalar(5,120,90)
#ORANGE_MAX = cv2.Scalar(19,213,255)
#RED_MIN = cv2.Scalar(0,130,0)
#RED_MAX = cv2.Scalar(7,255,255)
#BLUE_MIN = cv2.Scalar(95,123,94)
#BLUE_MAX = cv2.Scalar(128,255,255)
#GREEN_MIN = cv2.Scalar(61,94,64)
#GREEN_MAX = cv2.Scalar(70,255,255)

color = {
        'red'    : (0,0,255),
        'orange' : (0,165,255),
        'blue'   : (255,0,0),
        'green'  : (0,255,0),
        'white'  : (255,255,255),
        'yellow' : (0,255,255)
        }

def color_detect(h,s,v):
    if h <=19 and h>=3 and s<=213 and s>=120 and v>=90:
        return 'orange'
    # in hsv, the red space wraps around 180 and has to be [0..10] and [170..180]
    elif (h>=170) and s>=130 :
        return 'red'          
    elif h <= 60 and h>=22 and s>=130 and v>=190:
        return 'yellow'
    elif h <=94 and h>=61 and s>=94 and v>=64:
        return 'green'
    elif h<=128 and h>=95 and s>=123 and v>=94:
        return 'blue'
    elif h<=128 and h>=26 and s<=40 and v>=139:
        return 'white'
    return 'white'



def draw_stickers(frame,stickers,name):
    ''' This method draws the rectangles for the webcam recognition area 
    '''
    global sickersize
    for x,y in stickers[name]:
        cv2.rectangle(frame, (x,y), (x+sticker_size_recog, y+sticker_size_recog), (255,255,255), 2)



def draw_preview_stickers(frame,stickers):
    ''' This method draws the rectangles for all facelets
    '''
    stick=['front','back','left','right','up','down']
    for name in stick:
        for x,y in stickers[name]:
            cv2.rectangle(frame, (x,y), (x+sticker_size, y+sticker_size), (255,255,255), 2)


def draw_preview_text(cv2, img):
    ''' This method draws small letters inside the faces
    '''
    for faces in range(6):
        x,y = stickers[face_colors[faces]][4]
        cv2.putText(img, face_stickers[faces], (x+8,y+24), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0), 1, cv2.LINE_AA)  


def fill_stickers(frame,stickers,sides):    
    ''' This method takes the "screenshots" and draws the
        colored stickers inside the facelets
    '''
    for side,colors in sides.items():
        num=0
        for x,y in stickers[side]:
            cv2.rectangle(frame,(x,y),(x+sticker_size,y+sticker_size),color[colors[num]],-1)
            num+=1


def print_cubestring():
    ''' this methd takes the "screenshots"
        and creates the cube configration string 
        used by main gui and solver
    '''
    cubestring = ""

    for face in range(9):
        cubestring += state['up'][face].capitalize()[0]

    for x in range(3):
        for face in range(3):
            cubestring+=state['left'][face+3*x].capitalize()[0]
        for face in range(3):
            cubestring+=state['front'][face+3*x].capitalize()[0]
        for face in range(3):
            cubestring+=state['right'][face+3*x].capitalize()[0]
        for face in range(3):
            cubestring+=state['back'][face+3*x].capitalize()[0]

    for face in range(9):
        cubestring += state['down'][face].capitalize()[0]

    # hier noch: String zurückgeben
    return cubestring


def write_cubeconfig():
    print("Writing cubeconfig file...")
    print("Content: ", print_cubestring())
    with open("cubeconfig.txt", "w") as text_file:
        text_file.write(print_cubestring())
    print("Done...")
    print("Returning to main GUI...")


# without cv2.CAP_DSHOW it took verly long to access the webcam
# 0 hp envy (external)
# 1 internal (crashes)
# 2 logistream (external)

# if no dock is connected, 0 is the laptop's cam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,800)
cv2.namedWindow('frame')

check_state=[]

while True:
    #event, values = window.read(timeout=20)
    hsv=[]
    current_state=[]
    success, img = cap.read()

    img=cv2.flip(img,1)
    frame=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # zeichne die Boxen für die Kameraerkennung
    draw_stickers(img, stickers,'main')
    # zeichne alle facelets
    draw_preview_stickers(img,stickers)
    # zeichne die facelets mit ihren bereits zugewiesenen Farben
    fill_stickers(img,stickers,state)
    draw_preview_text(cv2, img)

    # hier wird aus einem einzelnen pixel der Farbwert gebildet
    # Geht, ist aber nicht sehr aussagekräftig
    for i in range(9):
        x = stickers['main'][i][0]
        y = stickers['main'][i][1]
        # in drawsticker wird ein rechteck gezeichnet, das 30x30 breit ist
        # Bildausschnitte können mit [y:y+höhe][x:x+breite] bestimmt werden
        hsv.append(cv2.mean(frame[y+2:y+sticker_size_recog-4,x+2:x+sticker_size_recog-4]))
        #hsv.append(frame[stickers['main'][i][1]+10][stickers['main'][i][0]+10])

    a=0
    for x,y in stickers['current']:
        color_name=color_detect(hsv[a][0],hsv[a][1],hsv[a][2])
        cv2.rectangle(img,(x,y),(x+sticker_size,y+sticker_size),color[color_name],-1)
        a+=1
        current_state.append(color_name)
    # flip around the y axis, because cam image is flipped    
    current_state[0], current_state[2] = current_state[2], current_state[0]
    current_state[3], current_state[5] = current_state[5], current_state[3]
    current_state[6], current_state[8] = current_state[8], current_state[6]


    cv2.putText(img, faces[current_face], (262,52), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img, faces[current_face], (260,50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2, cv2.LINE_AA)

    cv2.putText(img, "Space: proceed, s: set, q: quit", (262,92), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img, "Space: proceed, s: set, q: quit", (260,90), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2, cv2.LINE_AA)

    cv2.imshow('frame',img[0:1600,0:800])


    keypress = cv2.waitKey(5) & 0xFF
    
    if keypress  == ord('q'):
        write_cubeconfig()
        break
    elif keypress == ord('u'):
        current_state[4] = 'white'
        state['up']=current_state
        #check_state.append('u')
    elif keypress == ord('l'):
        state['left']=current_state
        check_state.append('l')
    elif keypress == ord('f'):
        state['front']=current_state
        check_state.append('f')
    elif keypress == ord('r'):
        state['right']=current_state
        check_state.append('r')
    elif keypress == ord('b'):
        state['back']=current_state
        check_state.append('b')
    elif keypress == ord('d'):
        state['down']=current_state
        check_state.append('d')
    elif keypress == ord('s'):
        # gan cube has a blue sticker on the white face
        if (current_face == 3):
            current_state[4] = 'white'
        state[face_colors[current_face]]=current_state
    elif keypress == ord(' '):
        current_face = (current_face + 1) % 6

