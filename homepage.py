from tkinter import *
from tkinter import ttk
from bubbleSort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort

#Configuring Tkinter Root window
window=Tk()
window.title("Sorting Visualizer")
window.minsize(height=300,width=550)
w=window.winfo_screenwidth() 
h =window.winfo_screenheight()
window.geometry('%dx%d'%(w,h))

#variables
selected_alg = StringVar()
data = []
arr_data=StringVar()


#Function represent array in graphical form
def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 500
    c_width = 1400
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 480
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    
    window.update_idletasks()


#function to generate graph
def GenerateGraph():
	global data
	arraydata=arr_data.get()
	x = arraydata.split(",")
	data = []
	for i in x:
		data.append(int(i))
	drawData(data, ['red' for x in range(len(data))]) #['red', 'red' ,....]	


#Function to start Algorithm
def StartAlgorithm():
    global data
    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
    
    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Selection Sort':
        selection_sort(data, drawData, speedScale.get())

    elif algMenu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, speedScale.get())        

    elif algMenu.get() == 'Merge Sort':
        merge_sort(data, drawData, speedScale.get())
    
    drawData(data, ['green' for x in range(len(data))])


#Menu Frame
UI_frame = Frame(window, width=w,height=100,bg='#242424')
UI_frame.grid(row=0, padx=0, pady=0)

#canvas
canvas = Canvas(window, width=w, height=h, bg='#f1f3f4')
canvas.grid(row=1, column=0, padx=0,pady=0,columnspan=3)


#ArrayEntry
Label1=Label(UI_frame,text="Array",bg='#242424',fg='#08BD80',font=("URW Palladio L","15","bold"))
Label1.grid(row=0,column=0,padx=2,pady=5)
inputField=Entry(UI_frame,textvariable=arr_data,width=50,font=("URW Palladio L","15","bold"))
inputField.grid(row=0,column=1,padx=2,pady=5)

#generate graph button
b1=Button(UI_frame, text="Generate Graph", command=GenerateGraph,bg='#242424',fg='#08BD80',borderwidth=0,highlightthickness=0,width=30,font=("URW Palladio L","15","bold"))
b1.grid(row=0, column=2, padx=2, pady=5)

#Dropdown list
Label2=Label(UI_frame, text="Algorithm: ",bg='#242424',fg='#08BD80',width=20,font=("URW Palladio L","15","bold"))
Label2.grid(row=1, column=0, padx=2, pady=5)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort'],width=50,font=("URW Palladio L","15","bold"))
algMenu.grid(row=1, column=1, padx=2, pady=5)
algMenu.current(0)

#speed scale
speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=300, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [seconds]",bg='#242424',fg='#08BD80',width=20,borderwidth=0,highlightthickness=0,font=("URW Palladio L","15","bold"))
speedScale.grid(row=1, column=2, padx=2, pady=5)


#sort button
b2=Button(UI_frame, text="Sort", command=StartAlgorithm, bg='#242424',fg='#08BD80',borderwidth=0,highlightthickness=0,width=30,font=("URW Palladio L","15","bold"))
b2.grid(row=1, column=3, padx=2, pady=5)


window.mainloop()
