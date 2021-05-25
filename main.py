from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hamiltonian Cycle Visualizer")
root.geometry('1350x750')
root.resizable(False, False)
canvas = Canvas(root, height=750, width=1350, bg="#99ffbb")
canvas.pack()
frame_top = Frame(canvas, width=1500, height=115, bg="#99ffbb")
frame_top.place(relx=0, rely=0)
Label(frame_top, text="Hamiltonian Cycle Visualization", font=("Brush Script MT", 30, "bold"), justify="center",
      bg="#99ffbb").place(relx=0.45, rely=0.03, anchor='n')
Label(frame_top, text="A Hamiltonian cycle is a closed loop on a graph where every node (vertex) is visited exactly "
                      "once. A loop is just an edge that joins a node to itself; so a Hamiltonian\ncycle is a path "
                      "traveling from a point back to itself, visiting every node en route.",
      font=("Brush Script MT", 18),
      justify="center", bg="#99ffbb").place(relx=0.016, rely=0.495)
Label(canvas, text="Time complexity analysis:", font=("Brush Script MT", 18, "bold"),
      bg="#99ffbb").place(relx=0.89, rely=0.83, anchor='n')
Label(canvas, text="As backtracking and DFS is used ", font=("Brush Script MT", 18),
      bg="#99ffbb").place(relx=0.89, rely=0.87, anchor='n')
Label(canvas, text="in the algorithm the time complexity", font=("Brush Script MT", 18),
      bg="#99ffbb").place(relx=0.89, rely=0.91, anchor='n')
Label(canvas, text="analysis is O(2^n*n^2).", font=("Brush Script MT", 18),
      bg="#99ffbb").place(relx=0.89, rely=0.95, anchor='n')

i = 0
path_str = " "
side_labels = {
    0: "Here we can see the given graph in left and the possible state space tree in the right.",
    1: "Firstly we have considered node A in the stack and will explore the neighbours of A.",
    2: "We considered the first neighbour of A, B and now we will explore neighbours of B.",
    3: "Now C is added into the stack and then we will explore the neighbours of C.",
    4: "We can go to D from C as A and B are already visited.",
    5: "Now we can go to E and then we see that we have traversed through all the vertices in the graph.",
    6: "Now we check if we can go back to the starting vertex, A. We found our first cycle as ABCDEA",
    7: "Now we backtrack to B and explore it's other neighbours which are not visited earlier.",
    8: "We can go to E as we have already travelled through C and others vertices are not possible to traverse to.",
    9: "From E we can go to D and check it's neighbours.",
    10: "After D we can go only to C and we realise that we have traversed through all the vertices.",
    11: "We realise that we can go back to the starting vertex A, so we have our second Hamiltonian cycle as ABEDCA.",
    12: "Now we backtrack to A and explore it's other neighbour C.",
    13: "From C we can now go to B and D but here we choose B first.",
    14: "From B we can only go to the vertex E as there is no other possible path available.",
    15: "Now we check the neighbours of E and we found that we can go to D.",
    16: "As all the vertices were visited we check if we can go back to the starting vertex A, looks like we can't.",
    17: "Now we backtrack to C and explore it's other neighbours.",
    18: "We can visit D from C and then see D's neighbours.",
    19: "From D we can visit E as there is no other possible path available.",
    20: "From E we can go to B and then we realise that all the vertices are traversed.",
    21: "Seems like we can go back to the starting vertex A this we get another Hamiltonian cycle as ACDEBA.",
    22: "Now we backtrack to A and visit the third neighbour of a that is E.",
    23: "From E we can traverse to B and D but firstly we will consider B.",
    24: "Now we visit C as from B we can only visit C.",
    25: "After C we have to visit D as no other possible paths are available.",
    26: "As all the vertices were traversed we check if we can go back to the starting vertex A. Seems like we can't.",
    27: "Now we backtrack to E and explore it's other neighbours.",
    28: "We visit D as the other neighbour B was already visited earlier.",
    29: "From D we can visit C as no other possible path is available.",
    30: "From C we can go to B and we see that all the vertices are traversed.",
    31: "Now we check if we can go back to the starting vertex A, looks like we can. We get our last Hamiltonian "
        "cycle\nas AEDCBA. "
}

image_ = Image.open("images/" + str(i) + ".png")
resized = image_.resize((1000, 550), Image.ANTIALIAS)
test = ImageTk.PhotoImage(resized)
lbl = Label(canvas, image=test, height=550, width=1000)
lbl.place(relx=0.018, rely=0.16)
frame_right = Frame(canvas, height=500, width=328, bg="#99ffbb")
frame_right.place(relx=0.76, rely=0.135)
output = Label(frame_right, text=path_str, font=("Brush Script MT", 20, "bold"), bg="#99ffbb")
Label(frame_right, text="Enter the adjacency matrix", font=("Brush Script MT", 20, "bold"), bg="#99ffbb").place(
    relx=0.5, rely=0.02, anchor='n')
matrix_entry = Text(frame_right, font=15)
matrix_entry.place(relx=0.05, rely=0.1, height=100, width=290)
submit = Button(frame_right, text=" Submit ", command=lambda: submit_commands(), font=("Brush Script MT", 15))
submit.place(relx=0.5, rely=0.31, anchor='n')
Label(frame_right, text="Output:", font=("Brush Script MT", 17, "bold"), bg="#99ffbb").place(relx=0.05, rely=0.43,
                                                                                             anchor='w')
side_label = Label(canvas, text=side_labels[i], bg="#99ffbb", font=("Brush Script MT", 17, "bold"))
side_label.place(relx=0.02, rely=0.9)


def submit_commands():
    global path_str
    path_str = " "
    HamiltonianCycle()
    if len(path_str.strip()) == 0:
        output.configure(text="No Possible Solutions")
        output.place(relx=0.5, rely=0.5, anchor='n')
    else:
        output.configure(text=path_str)
        output.place(relx=0.5, rely=0.43, anchor='n')


def HamiltonianCycle():
    strr = matrix_entry.get("1.0", "end")
    matrix = []
    mat = strr.strip().split("\n")
    for i in mat:
        matr = [int(item) for item in i.split()]
        matrix.append(matr)
    # print(matrix)
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                if (j, i) not in edges:
                    edges.append((i, j))
    # print(edges)
    N = len(matrix)
    # build a graph from the given edges
    adjList = Graph(edges, N)
    # starting node
    start = 0
    # add starting node to the path
    path = [start]
    # mark the start node as visited
    visited = [False] * N
    visited[start] = True
    Hamiltonian(adjList, start, visited, path, N, edges)


def Graph(edges, N):
    # A list of lists to represent an adjacency list
    adjList = [[] for _ in range(N)]
    # add edges to the undirected graph
    for (src, dest) in edges:
        adjList[src].append(dest)
        adjList[dest].append(src)
    return adjList


def Hamiltonian(adjList, v, visited, path, N, edges):
    global path_str
    # if all the vertices are visited, then the Hamiltonian path exists
    if len(path) == N:
        v1 = path[N - 1]
        v2 = path[0]
        if (v1, v2) in edges or (v2, v1) in edges:
            global path_str
            path_str = path_str + "\n" + "["
            for i in range(len(path)):
                if i <= len(path) - 2:
                    path_str = path_str + chr(65 + path[i]) + ", "
                else:
                    path_str = path_str + chr(65 + path[i]) + ", " + chr(65 + v2) + "]"
        return
    # Check if every edge starting from vertex `v` leads to a solution or not
    for w in adjList[v]:
        # process only unvisited vertices as the Hamiltonian
        # path visit each vertex exactly once
        if not visited[w]:
            visited[w] = True
            path.append(w)
            # check if adding vertex `w` to the path leads to the solution or not
            Hamiltonian(adjList, w, visited, path, N, edges)
            # backtrack
            visited[w] = False
            path.pop()


# output.configure(text=path_str)
# print(path_str)
def next_click():
    global i, test, image_
    if i < 31:
        i = i + 1
    image_ = Image.open("images/" + str(i) + ".png")
    resized = image_.resize((1000, 550), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(resized)
    lbl.configure(image=test)
    side_label.configure(text=side_labels[i])
    # print(i)


def prev_click():
    global i, test, image_
    if i > 0:
        i = i - 1
    image_ = Image.open("images/" + str(i) + ".png")
    resized = image_.resize((1000, 550), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(resized)
    lbl.configure(image=test)
    side_label.configure(text=side_labels[i])
    # print(i)


next_btn = Button(canvas, text="Next", command=next_click, font=("Brush Script MT", 17))
prev_btn = Button(canvas, text="Prev", command=prev_click, font=("Brush Script MT", 17))
next_btn.place(relx=0.704, rely=0.89, anchor='sw', width=70, height=35)
prev_btn.place(relx=0.023, rely=0.89, anchor='sw', width=70, height=35)
root.mainloop()
