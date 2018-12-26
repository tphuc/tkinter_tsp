from tkinter import *

WIDTH = 800
HEIGHT = 800


class KEYBIND:
    zoomin = "z"
    zoomout = "x"
    up = "w"
    down = "s"
    left = "a"
    right = "d"
    revert = '-'
    deploy = '+'


class MARGIN:
    up = 30
    left = 650


class BODY:
    top1 = HEIGHT//16
    top2 = top1 + MARGIN.up
    top3 = top1 + MARGIN.up*2
    top4 = top1 + MARGIN.up*3
    top5 = top1 + MARGIN.up*4
    middle = HEIGHT//2
    bottom1 = HEIGHT * 6/8
    bottom2 = HEIGHT * 7/8
    buttonwidth = 15
    dropdownwidth = 12


def EuclideanDistance(start, end):
    """ Take 2 tuple as vector and return the Euclide distance between them """
    return ((end[0]-start[0]) ** 2 + (end[1]-start[1]) ** 2) ** 0.5


def SumDistance(vectors):
    sumDist = 0.0
    for i in range(len(vectors) - 1):
        sumDist += EuclideanDistance(vectors[i], vectors[i+1])
    return sumDist


root = Tk()


class Window():
    def __init__(self, root=root):
        self.Nodes = []
        self.originNodes = []
        self.Points = []
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.scaleX, self.scaleY = 5, 5
        self.focusX, self.focusY = self.WIDTH//2, self.HEIGHT//2
        self.zoominrate = 1.3
        self.zoomoutrate = 0.7
        self.moverate = 50
        self.depth = 3
        self.canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(fill=BOTH, expand=1)
        self.display_route = False
        self.linewidth = 0.05
        self.distance = 0
        self.algoSwitch = {}
        ##############################################################
        self.button1 = Button(
            text='Show Route', command=self.enableshowroute, fg='darkblue', width=BODY.buttonwidth)
        self.button1.pack(fill=BOTH, expand=1)
        self.button1.place(x=MARGIN.left, y=BODY.top1)
        ###############################################################
        self.button2 = Button(
            text='Hide Route', command=self.disableshowroute, fg='darkblue', width=BODY.buttonwidth)
        self.button2.pack(fill=BOTH, expand=1)
        self.button2.place(x=MARGIN.left, y=BODY.top2)
        ###############################################################
        self.deploy_button = Button(
            text='Deploy Algorithm', command=self.deployAlgorithm, fg='red', width=BODY.buttonwidth, height=2)
        self.deploy_button.pack(fill=BOTH, expand=1)
        self.deploy_button.place(x=MARGIN.left, y=BODY.top5)
        ################################################################
        self.revert_button = Button(
            text="Revert", command=self.revert, width=BODY.buttonwidth, bd=2)
        self.revert_button.pack(fill=BOTH, expand=1)
        self.revert_button.place(x=MARGIN.left, y=BODY.bottom1)
        ################################################################
        self.distancedisplay = Label(text='total:'+str(self.distance))
        self.distancedisplay.place(x=MARGIN.left, y=BODY.middle)
        ################################################################
        self._setupbind()

    def _drawCoordinate(self):
        self.canvas.create_line(
            0, self.HEIGHT//2, self.WIDTH, self.HEIGHT//2, arrow=LAST, width=1)
        self.canvas.create_line(
            self.WIDTH//2, 0, self.WIDTH//2, self.HEIGHT, arrow=FIRST, width=1)

    def _resetScale(self):
        self.scaleX = 1
        self.scaleY = 1

    def _setupbind(self):
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.keyaction)

    def _tocenter(self):
        for point in self.Points:
            point.x = point.x*self.scaleX
            point.y = point.y*self.scaleY
            point.width *= self.scaleX
        self.linewidth *= self.scaleX//10
        self._resetScale()
        centerx = sum([p.x for p in self.Points], 0)//len(self.Points)
        centery = sum([p.y for p in self.Points], 0)//len(self.Points)
        for point in self.Points:
            point.x += self.focusX - centerx
            point.y += self.focusY - centery
            point.doupdate()

    def enableshowroute(self):
        if not self.display_route:
            self.showroute()
            self.display_route = True

    def disableshowroute(self):
        if self.display_route:
            self.canvas.delete('line')
            self.display_route = False

    def addNodes(self, nodes=[], locations=[], names=[], append=False):

        if not append:
            self.Points = []
            Point.numbers = 0
        if nodes:
            if not self.originNodes:
                self.originNodes = nodes
            self.Nodes = nodes
            for node in nodes:
                self.Points.append(
                    Point(node.name, node.y, node.x, self.canvas))
        else:
            for i in range(len(locations)):
                self.Points.append(
                    Point(names[i], locations[i][1], locations[i][0], self.canvas))
        for point in self.Points:
            point.x += self.WIDTH//2
            point.y += self.HEIGHT//2
            point.y *= -1

    def addAlgoOptions(self, algoswitch):
        self.algoSwitch = algoswitch
        names = list(self.algoSwitch.keys())
        self.algorithm = StringVar(root)
        self.algorithm.set(names[0])
        self.algorithms_dropdown = OptionMenu(
            root, self.algorithm, names[0], *names[1:])
        self.algorithms_dropdown.config(bg='yellow', width=BODY.dropdownwidth)
        self.algorithms_dropdown.place(x=MARGIN.left, y=BODY.top4)

    def plot(self):
        self._tocenter()
        if self.display_route:
            self.showroute()

    def showroute(self):
        for i in range(len(self.Points)-1):
            self.canvas.create_line(
                self.Points[i].x, self.Points[i].y,
                self.Points[i+1].x, self.Points[i+1].y,
                arrow=LAST,
                width=self.linewidth, tags='line')

    def keyaction(self, event):
        if event.char == KEYBIND.zoomin:
            self.scaleX *= self.zoominrate
            self.scaleY *= self.zoominrate
            self.depth += 1
            self.redraw()
        elif event.char == KEYBIND.zoomout:
            self.scaleX *= self.zoomoutrate
            self.scaleY *= self.zoomoutrate
            self.depth -= 1
            self.redraw()
        elif event.char == KEYBIND.up:
            self.focusY += self.moverate
            self.redraw()
        elif event.char == KEYBIND.down:
            self.focusY -= self.moverate
            self.redraw()
        elif event.char == KEYBIND.right:
            self.focusX -= self.moverate
            self.redraw()
        elif event.char == KEYBIND.left:
            self.focusX += self.moverate
            self.redraw()
        elif event.char == KEYBIND.revert:
            self.revert()
        elif event.char == KEYBIND.deploy:
            self.deployAlgorithm()

    def redraw(self, restorezoom=False):
        self.canvas.delete("all")
        if restorezoom:
            self.scaleX = self.zoominrate ** self.depth
            self.scaleY = self.zoominrate ** self.depth
            pass
        self.plot()

    def deployAlgorithm(self):
        func = self.algoSwitch.get(
            self.algorithm.get(), lambda: print("Function not found!"))
        self.Nodes = func(self.Nodes)
        self.addNodes(self.Nodes)
        self.distance = round(SumDistance(
            [point.loc for point in self.Points]), 6)
        self.distancedisplay.config(text="total: "+str(self.distance))
        self.redraw(restorezoom=True)

    def revert(self):
        self.addNodes(self.originNodes)
        self.redraw(restorezoom=True)

    def run(self):
        self.canvas.delete("all")
        self.plot()
        mainloop()


class Point():
    numbers = 0

    def __init__(self, name, y, x, canvas):
        Point.numbers += 1
        self.r = 1
        self.x = x
        self.y = y
        self.loc = x, y
        self.name = name
        self.x1, self.y1 = self.x+self.r, self.y+self.r
        self.x2, self.y2 = self.x-self.r, self.y-self.r
        self.width = 0.1
        self.canvas = canvas
        self.color = 'black'
        if Point.numbers == 1:
            self.color = 'blue'
            self.width *= 2
        self.oval = self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, width=self.width,
            fill='black', outline=self.color)
        self.canvas.tag_bind(self.oval, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.oval, "<Leave>", self.on_leave)
        self.namedisplay = None

    def doupdate(self):
        self.x1, self.y1 = self.x+self.r, self.y+self.r
        self.x2, self.y2 = self.x-self.r, self.y-self.r
        self._redraw()
        self.canvas.tag_bind(self.oval, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.oval, "<Leave>", self.on_leave)

    def _redraw(self):
        self.oval = self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, width=self.width,
            fill='black', outline=self.color)

    def on_enter(self, event):
        self.namedisplay = self.canvas.create_text(
            self.x, self.y-20, text=self.name, tags='displaycity')
        self.canvas.tag_bind(self.namedisplay, "<Enter>", self.on_leave)

    def on_leave(self, event):
        self.canvas.delete(self.namedisplay)
