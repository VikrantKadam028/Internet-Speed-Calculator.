from tkinter import *
import speedtest

def speed_check():
    st = speedtest.Speedtest()
    # st.get_servers()
    st.get_best_server()
    down = str(round(st.download()/(10**6), 3)) + " Mbps"
    up = str(round(st.upload()/(10**6), 3)) + " Mbps"
    lab_down_speed.config(text=down)
    lab_up_speed.config(text=up)

root = Tk()
root.title("Internet Speed Test")
root.geometry("400x500")
root.config(bg="black")

lab_title = Label(root, text="Internet Speed Test", font=("Times New Roman", 20), bg="black", fg="white")
lab_title.place(x=90, y=30, height=40, width=220)

lab_down = Label(root, text="Download Speed", font=("Times New Roman", 20), bg="white", fg="black")
lab_down.place(x=90, y=120, height=40, width=220)

lab_down_speed = Label(root, text="00 Mbps", font=("Times New Roman", 25), bg="black", fg="white")
lab_down_speed.place(x=90, y=160, height=40, width=220)

lab_up = Label(root, text="Upload Speed", font=("Times New Roman", 20), bg="white", fg="black")
lab_up.place(x=90, y=220, height=40, width=220)

lab_up_speed = Label(root, text="00 Mbps", font=("Times New Roman", 25), bg="black", fg="white")
lab_up_speed.place(x=90, y=260, height=40, width=220)

check_button = Button(root, text="Check Speed", font=("Poppins", 15, "bold"), relief=RAISED, cursor="plus", command=speed_check)
check_button.place(x=65, y=340, height=40, width=280)

root.mainloop()

