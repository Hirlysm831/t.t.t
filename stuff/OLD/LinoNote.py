# -*- coding: cp936 -*-
#[[[[[TODO]]]]]
#����listbox��3d����
#ʹlistbox����ռ30%�ٷֱȵĿ��
#===���ؿ���̨����
import ctypes
whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)
#======

help_text=u'�����򿽱���һ������.txt�ļ����ļ����£�Ȼ������LinoNote.exe��\n�����ıʼ��嵥��ѡ��ʼǣ����Ҳ�ı༭���ڱ༭��\n���˳������ѡ�������ļ�ʱ���ʼǻᱻ�Զ����档\n�༭�������Ǳ����������Զ��ļ����и������ļ���ת�ơ���ע�⣬�ļ��еġ�\\����������á�>������ʾ����������Ϊ�ļ������չ����\n�ڡ�<New Note>������ʼ��У�������ֱ�Ӵ����µıʼǡ�\n����ϵtslimingyang@126.com����ȡ������Ϣ�����עhttp://tslmy.tk��\n'

version='LinoNote 1.0'
new_note_title='<New Note>'
jinzhishixiang=['?','/','*',':','��','<','>','|']
import Tkinter as tk#װ��һ����ƽ̨�����е�GUI�⣺Tkinter
import tkMessageBox#װ�ضԻ���⣨tkMessageBox���������ڡ���
import Tix as tx
from time import strftime#װ��ʱ�������
import md5#װ��MD5��
def getsignature(contents): #�õ�MD5��
    return md5.md5(contents).digest()
import os #װ��os��
root = tk.Tk()#����������
root.title(version)#   �˷������Ը��Ĵ��ڱ���
root.geometry('800x400')#   ���������ڵĳ�ʼ��С
#   �˵���
#����func:   lambda : None
menu = tk.Menu(root)
root.config(menu=menu)
#filemenu.add_separator()
helpmenu = tk.Menu(menu)
menu.add_cascade(label=u"����", menu=helpmenu)
helpmenu.add_command(label=u"ʹ�÷�����", command=lambda : tkMessageBox.showwarning(u'ʹ�÷���',help_text))
helpmenu.add_command(label=u"���ڡ�", command=lambda : tkMessageBox.showwarning(u'����',u'��ŵ�ʼ��������������������'))
#label��ʹ�÷�����
#   w = tk.Label(master=top_frame, text="Hello, world!")
#   w.pack(side=tk.LEFT)
#��ť��ʹ�÷�����
#   button = tk.Button(top_frame, text="QUIT", fg="red", command=root.quit)
#   button.pack(side=tk.RIGHT)
#frame������һ��������ʹ�÷������£�
#   frame = tk.Frame(root)
#   frame.pack(side=tk.TOP)
#�������У������������֣�
#   ��
left = tk.Frame(root)
left.pack(side=tk.LEFT,ipadx='40',fill='y') #��ʵ���Ｔʹfill='both'Ҳ����Ϊside�Ĵ��ڵ��谭��ʹ��Ч����ͬ��fill='y'
#   ��ƫ�ҵ�scrollbar����������
l_bar = tk.Frame(left)
l_bar.pack(side=tk.RIGHT,fill='y')
#   ��
right = tk.Frame(root)
right.pack(expand='yes',fill='both')
#   ��ƫ�ҵ�scrollbar����������
r_bar = tk.Frame(right)
r_bar.pack(side=tk.RIGHT,fill='y')
#Ԫ����װ�أ�
#   ������ߣ�
#       ��ֱ������1��
scrollbar_l = tk.Scrollbar(master=l_bar)
scrollbar_l.pack( side = tk.RIGHT,padx=3, fill=tk.Y ) #padx:thick board on X direction, pixels
#       LISTBOX��
listbox = tk.Listbox(relief=tk.SUNKEN,borderwidth=1,font='���� 11',master=left,selectmode=tk.BROWSE,yscrollcommand = scrollbar_l.set)
listbox.pack(expand='yes',fill='both') #expand='yes',fill='both' will make it fill the whole container
scrollbar_l.config( command = listbox.yview )#hook��scrollbar
#   �����ұߣ�
#       һ��Entry��������ʾ�ļ��������Ǳ���������
biaoti=tk.Entry(master=right)#text ��������
biaoti.pack(side=tk.TOP,fill='x')#Ĭ��side=tk.TOP
#       ��ֱ������2��
scrollbar_r = tk.Scrollbar(master=r_bar)
scrollbar_r.pack( side = tk.RIGHT ,padx=0, fill=tk.Y ) #padx:thick board on X direction, pixels
#       ���ֱ༭���֣�
t=tk.Text(master=right)
t.pack(expand='yes',fill='both')#expand='yes'����ص�side��Ч������ʹfill�ܹ�����������������
t.config(state=tk.NORMAL,font='���� 12',yscrollcommand=scrollbar_r.set)#font setting
scrollbar_r.config( command = t.yview )#hook��scrollbar
#���Ĳ��֣�
#   ȫ������
cur_file=''#��Ŀǰ���򿪵��ļ����ǡ���ǰӦ�б��⡱����չ
cur_name=''
cur_md5=''#������Ÿմ��ļ�ʱ��MD5ֵ
cur_index=listbox.index(tk.ACTIVE) #�洢Ŀǰ�����ļ�������λ��

def get_folder(fila):
    last_sprtor=fila.rfind('\\')
    if last_sprtor==-1:
        folder=''
    else:
        folder=fila[:last_sprtor]
    print 'folder for '+fila+' is:'+folder
    return (folder)
##def folderize(fila): �Ѿ����ϲ�����file_save�С�
##    folder=get_folder(fila)
##    if not os.path.isdir(folder):
##        print os.popen('md '+folder).read()
def file_save(file_path,context):
    folder=get_folder(file_path)
    if not os.path.isdir(folder):
        print os.popen('md "'+folder+'"').read()
    fila=open(file_path,'w+')
    fila.write(context.encode('GBK')[:-1])# [:-1] will get rid of a additional \n created by encode()
    fila.close()
    print 'File Saved to '+file_path #��ֻ�ڿ���̨�г���


listbox.insert(tk.END,new_note_title)
#   �����ļ���Ŀ
files = os.popen('dir /b /s *.txt').readlines()
if len(files)==0:
    file_save(u"ʹ��ָ��.txt",help_text)
    listbox.insert(tk.END,u'ʹ��ָ��')
else:
	for item in files:
		listbox.insert(tk.END, item[len(os.getcwd())+1:-5].decode('GBK').replace('\\','>'))#���Ƕ���GBK����ģ�
    #       os.getcwd()�����õ���ǰpython�Ĺ���·����+1��ɾ������ġ�\\����-1��ɾ������Ļ��з�����Ϊ��readlines���������������û���Ҳ���ԣ���
    #       add a entry "aaa" at the END of the listbox: listbox.insert(tk.END, "aaa")



def if_folder_empty(folder):
    if folder<>'':
        print os.listdir(folder) #DEBUG
        if len(os.listdir(folder))==0: #�������
            os.popen('rd '+folder.encode('GBK'))#ɾ���ļ���
            print 'Deleted folder: '+folder
    else:
        print 'This file is saved on the root folder, which means, souce folder can not be deleted.'
def cur_del():
    listbox.delete(cur_index)#���б���ɾ����
    os.popen('del '+cur_file.encode('GBK'))
    print 'Deleted: '+cur_file
    if_folder_empty(cur_dir)
def working_get():
    global working_title,working_text,working_file,working_dir,working_md5
    working_title=biaoti.get().encode('UTF-8')
    for i in jinzhishixiang:
        working_title.replace(i,'')
    working_title=working_title.decode('UTF-8')
    working_text=t.get(1.0, tk.END)
    if working_title==new_note_title and working_text=='\n':
        working_file=''
        working_dir=''
    else:
        working_file=working_title.replace('>','\\')+'.txt'
        working_dir=get_folder(working_file)
    working_md5=getsignature(working_text.encode('GBK'))
def push(what,where):
    lisa=listbox.get(0,tk.END)
    for i in lisa:
        if i==what:
            return 0
    listbox.insert(where,what)
def save_note(ifpush): #������������
    global working_title
    if cur_index==0 :
        print '�����뿪 �½��ʼ� ����'
        if working_text=='\n':
            print 'û������ ������ʼ�'
        else:
            print '��ʼ�����±ʼǡ���'
            if working_title==new_note_title:
                working_title=strftime("Unsorted>%y-%m-%d_%H%M%S")
                print '�����Զ������˱��⣺'+working_title
            file_save(working_title.replace('>','\\')+'.txt'.encode('GBK'),working_text)#p.s. ����ǰ���⡱�ѱ�������
            if ifpush:
                push(working_title,1)
    else:
        print '�뿪��һ����ͨ�ʼǡ�'
        if working_title<>'' and working_text<>'\n': #�����Ҫɾ���ļ�
            print '������Ҫɾ���ļ���û��һ�����գ�'
            if working_file<>cur_file:#��������ļ�����·��
                print '�����ļ�����·������Ϊ�ƶ�'
                if not os.path.isdir(working_dir):
                    print '�½����ļ��У�'+os.popen('md '+working_dir.encode('GBK')).read()
                print os.popen('move "'+cur_file.encode('GBK')+'" "'+working_file.encode('GBK')+'"').read()
                print "   ��ѯԴ�ļ����Ƿ�Ϊ�ա���"
                if_folder_empty(cur_dir)
                if ifpush: #ͨ���ж�ifpush��ȷ�����Ǵ��ĸ��¼������ģ��ͣ��Ƿ���Ҫ�����б�������Ҫ�����б��ض����ǣ��Ҳ����ǣ��ӡ��˳����¼���������Ϊindex��������⡣
                    if push(working_title,cur_index)==0:
                        print '�б���������ͬ��Ŀ���������롣'
                    else:
                        print '�Ѽ����б��׶ˡ�'
                listbox.delete(cur_index+1)#���б���ɾ��
                print 'ɾ���˾ɵ���Ŀ����'+str(cur_index+1)+'�'
            if cur_md5<>working_md5: #�������Ҫɾ���ļ��������ݱ������ˣ�
                print '��Ȼ��Ҫɾ���ļ������ǻ����������ݡ�����Ϊ���ļ����޸ģ������ļ���'
                file_save(working_file,working_text)#�ͱ���Ҫ����һ�Ρ������ڸ������ļ�·��
        else:#���Ҫɾ���ļ�
            cur_del()
def on_exit_save():# һ����ԭsave�ֿ���Ĳ��ͬ�������������Ҳ��Ӧ���ֶ�now_���Ĳ���
    working_get()
    try:
        save_note(False)
    except:
        print 'A error has occccured.'
    finally: #����finally�����ز�������
        root.quit()#��Ϊ����"WM_DELETE_WINDOW"�����ġ����԰��æ���رմ���
def chose_a_file(event): #ignore event......���������ר��ѡ����listbox�е�һ��֮�󣬶Ը��ֻ��������Ĳ���
    print '�¼�>��ѡ�˶���Ŷ��'
    #scrollbar_l.set((listbox.index(tk.ACTIVE) / listbox.index(tk.END)),0)
    scrollbar_l.config( command = listbox.yview )
    global cur_index,cur_name,cur_file,cur_dir,cur_md5,working_title,working_text,working_file,working_dir,now_index     #ȫ�ֻ������Ķ��� ָ��
    cur_index=listbox.index(tk.ACTIVE)	#�õ� ���Ķ��� ָ��
    now_index=listbox.curselection()[0] #ֻ��һ����������[0]
    #�õ�Ŀǰ������������
    working_get()
    if now_index=='0': #����������ˡ��½��ʼǡ�����Ļ�
        print '���� �½��ʼ� ����'
        now_name=new_note_title #�µ�����
        now_file='' #�ļ�·����Ϊ��
    else:
        now_name=listbox.get(now_index) #������Ʋ���Ҫ����ֹ�����������������Ϊ�б��еĶ����ϸ񾻻���
        now_file=now_name.replace('>','\\')+'.txt'
        print '��ѡ���ˣ�'+now_index
        print 'jumped from '+str(cur_index)+' to '+ str(now_index)
        save_note(True)
    print 'Resetting to next turn...'
    #��ʼ׼����һ��
    cur_file=now_file #����ǰ�ļ�תΪ�����ŵ��ļ�
    print 'Currently opening file: '+str(cur_index)+'. '+cur_file+'('+cur_name+')'
    cur_name=now_name
    cur_index=now_index
    print 'New source folder: ',
    if now_index=='0': #��������� �½��ʼ� ģ��
        cur_dir=''
        print '<Now note> Function, no folder is included.'
    else:
        cur_dir=get_folder(cur_file)#�����cur_fileʵ���Ͼ�����һ����ѡ�е��ļ�����now_file��

    print '======================================'
#������
    biaoti.delete(0, tk.END)#��ձ�����
    biaoti.insert(0, cur_name)#���뵱ǰ�ļ���
    root.title(cur_name+' - '+version)#���Ĵ��ڱ���
    t.delete(1.0, tk.END) #���ֿ����
#   �ļ����� - ��ȡ
    if now_index<>'0': #������ȥ�½��ʼ�
        fila=open(cur_file) #���ļ�
        t.insert(tk.END,fila.read().decode('GBK')) #�����Ǿ��ϻ������Ƕ���GBK�ġ�����
        fila.close() #�ر��ļ�
        cur_md5 = getsignature(t.get(1.0, tk.END).encode('GBK')) #�õ�MD5��
    #else:
        #cur_md5 = '' ���Ҳû��
        #���ֿ����ռ���
    print '�ȴ��û�����...>'


#��ʼ��
biaoti.insert(0,new_note_title)	#�� �½��ʼ� ���� �������
listbox.itemconfig(0, bg='light grey', fg='white') 
listbox.selection_set(0) #ʹ���ΪĬ�ϣ��Ա㷽�� ������ֱ�ӱ༭
#       ���¼��뺯��hook��
listbox.bind('<ButtonRelease-1>',chose_a_file)  #�� ѡ����Ŀ ����¼� �� chose_a_file ���� ������
root.protocol("WM_DELETE_WINDOW", on_exit_save) #�� �رմ��� ����¼� �� on_exit_save ���� �����ϡ�ע�⣬�����������Ĺ�����ʽ��ͬ��
t.focus_set() #ʹ���ֱ༭����õ�����
root.mainloop() #������ѭ��
