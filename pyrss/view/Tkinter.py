from tkinter import *


def backGound_color(selection):

    colors = {
        'green':  root.config(bg = 'green'),
        'red':   root.config(bg = 'red'),
        'blue':   root.config(bg = 'yellow')
    }
    return colors
def test():
    print('it finally worked')


def get_rssSource():
    url = ""
    try:
        window = Tk()
        # ask the user to provide RSS feed url
        window.quit()
        window.mainloop()
         # I think this will close the window after input has been taken
       #return parse_RSS(url)

    except:
        pass

def changeRate():

   try:
    window =Tk()


    window.mainloop()

   except:


    return  # in here call change the rate(s) in the RSS class and hopefully it works

root = Tk()
root.title('RSS Display')
root.resizable()

menu_bar = Menu(root)
root.config(menu = menu_bar)


fileMenu = Menu(menu_bar)
viewMenu = Menu(menu_bar)
menu_bar.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label="Exit", command = root.quit)

menu_bar.add_cascade(label = "View", menu = viewMenu)
color = Menu(viewMenu)
rss_source = Menu(viewMenu)
changeRate = Menu(viewMenu)
viewMenu.add_cascade(label = "color", menu = color)
color.add_command(label = 'green', command = root.config(bg = 'green'))
color.add_command(label = 'blue', command = backGound_color('blue'))
color.add_command(label = 'red', command = backGound_color('red'))
viewMenu.add_cascade(label = "RSS source", menu = rss_source)
viewMenu.add_command(label = "changeRate(s)", command= changeRate)


root.mainloop()
