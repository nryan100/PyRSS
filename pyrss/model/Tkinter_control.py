import RSS 
from tkinter import *
from tkinter import colorchooser
import webbrowser
import threading
import time


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)

        func()

    t = threading.Timer(sec, func_wrapper)

    t.start()

    return t


def label_update(rss_display):
    def update():
        rss_display.url_count += 1
        rss_display.text.set(rss_display.title_list[rss_display.url_count])

    return update


class RSS_Display:

    def __init__(self):
        self.root = Tk()
        self.root.title('RSS Display')
        self.root.resizable()
        self.url_count = 0
        self.label()

        thread_id = set_interval(label_update(self), 10)

        self.menu()
        self.root.mainloop()

        thread_id.join()

    def label(self):
        self.text = StringVar()
        self.title_list = RSS.get_titles()
        self.text.set(self.title_list[self.url_count])

        label_1 = Label(self.root, textvariable=self.text)
        label_1.bind("<Button-1>", lambda e: self.callBack("http://rss.cnn.com/rss/cnn_topstories.rss"))
        label_1.pack()


    def background_color(self):
        pass
        # bg_color = colorchooser.askcolor(title='Background painter')
        # self.label(bg=bg_color[1])

    def callBack(self, url):
        webbrowser.open_new(url)

    def title_update(self):
        pass
        # title_list = RSS.get_titles()
        # i=0
        # if i < len(title_list):
        #     return title_list[i]
        # elif i == len(title_list):
        #     i=0
        # self.root.after((500, self.title_update))

    def custom_rss_url(self):
        pass

        def get_input():
            input = input_entry.get()
            print(input)

        window = Tk()
        window.title('delay time')
        label1 = Label(window, text='Delay time(s)')
        label1.grid(row=0, column=0)
        input_entry = Entry(window, width=5, textvariable=time)
        input_entry.grid(row=0, column=2)
        button = Button(window, text='Enter', command=get_input)
        button.grid(row=0, column=3)
        button.configure(command=window.destroy)

    def feed_delay(self):
        def get_input():
            input = input_entry.get()
            print(input)
            return input

        window = Tk()
        window.title('delay time')
        label1 = Label(window, text='Delay time(s)')
        label1.grid(row=0, column=0)
        input_entry = Entry(window, width=5)
        input_entry.grid(row=0, column=2)
        button = Button(window, text='Enter', command=get_input)
        button.grid(row=0, column=3)
        return get_input()
        window.destroy

        window.mainloop()

    def menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)
        file = Menu(menu_bar)
        menu_bar.add_cascade(label='File', menu=file)
        file.add_command(label="Exit", command=self.root.quit)

        view = Menu(menu_bar)
        menu_bar.add_cascade(label='View', menu=view)
        view.add_command(label='Feed delay', command=self.feed_delay)
        view.add_command(label='Background Color', command=self.background_color)


RSS_Display()
