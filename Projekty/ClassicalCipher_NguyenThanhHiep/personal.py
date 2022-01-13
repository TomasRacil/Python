#login
m_Password="123"

#substitution
m_Zobrazeni=["qwert","yuiop","asdfg","hjkl","zxcvb","nm","QWERT","YUIOP","ASDFG","HJKL","ZXCVB","NM","789","456","123","0"]

#Ceasar
m_KeyShift=5    

#Columnar 
m_Keyword="Vietnam" 

#XOR
m_XoredNumber=13
m_IndexVariable=0

def MakeCenter(root):  #Move tkinter to center of screen
    root.update_idletasks()
    width=root.winfo_width()
    height=root.winfo_height()
    x=(root.winfo_screenwidth()//2)-(width//2)
    y=(root.winfo_screenheight()//2)-(height//2)
    root.geometry(f'{width}x{height}+{x}+{y}')

