import getallwin as gaw
from tkinter import*
from tkinter.ttk import*
from tkinter.messagebox import*
import timebomb as tb
import ctrlwin as cw
if(tb.return_()==1):
    showerror("请重新安装您的明奈图钉","本软件目前正在开发，运行尚不稳定，由于涉及系统相关操作，为了您的系统安全，您无法使用本软件。")
    exit(0)
hwndntitd_old = []
def aot_c():
    root.attributes('-topmost',aotvar.get())
def owin(type_):
    c=tv.item(tv.focus())['values'][1]
    if(type_==0):
        cw.wc.close(c)
    elif(type_==1):
        cw.wc.shownormal(c)
    elif(type_==2):
        cw.wc.minn(c)
    elif(type_==3):
        cw.wc.maxx(c)
    elif(type_==4):
        cw.wc.tl(c)
    elif(type_==5):
        cw.wc.untl(c)
def run():
    global hwndntitd_old
    hwndntitd = gaw.get()
    if(hwndntitd!=hwndntitd_old):
        items = tv.get_children()
        [tv.delete(item) for item in items]
        for i in hwndntitd:
            tv.insert('', END, values=[hwndntitd[i],i])
    hwndntitd_old = hwndntitd
    root.after(1,run)
root = Tk()
root.title("明奈 | 图钉 | 1.0 Beta")
root.iconbitmap("mingnai.ico")
card1 = Frame(root)
card1.pack(fill=BOTH,expand=True)
c1xscroll = Scrollbar(card1, orient=HORIZONTAL)
c1yscroll = Scrollbar(card1, orient=VERTICAL)
columns = ['窗口标题','窗口句柄']
tv = Treeview(card1,xscrollcommand=c1xscroll.set,yscrollcommand=c1yscroll.set,show="headings",columns=columns)
for column in columns:
        tv.heading(column=column, text=column, anchor=W)
        tv.column(column=column, width=(1-columns.index(column))*200+100,
                     minwidth=100, anchor=W)
def ohh(eve):
    tvmb.post(eve.x_root,eve.y_root)
c1xscroll.config(command=tv.xview)
c1xscroll.pack(side=BOTTOM, fill=X)
c1yscroll.config(command=tv.yview)
c1yscroll.pack(side=RIGHT, fill=Y)
tv.pack(fill=BOTH, expand=True)
aotvar = IntVar()
Always_on_top_b = Checkbutton(card1,text="强行前端固定",variable=aotvar,onvalue=1,offvalue=0,command=aot_c)
Always_on_top_b.pack(fill=X,expand=True)
tvmb = Menu(root,tearoff=0)
tvmb.add_command(label="关闭",command=lambda:owin(0))
tvmb.add_command(label="向下还原",command=lambda:owin(1))
tvmb.add_command(label="最小化",command=lambda:owin(2))
tvmb.add_command(label="最大化",command=lambda:owin(3))
tvmb.add_command(label="前端固定",command=lambda:owin(4))
tvmb.add_command(label="取消固定",command=lambda:owin(5))
tv.bind("<Double-Button-1>",ohh)
run()
root.mainloop()
