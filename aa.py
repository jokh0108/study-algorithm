import gkeepapi

keep = gkeepapi.Keep()
success = keep.login('jokh0108', '10qp29wo')

note = keep.createNote('Todo', 'Eat breakfast')
note.pinned = True
note.color = gkeepapi.node.ColorValue.Red
keep.sync()

gnote = keep.all()
print(gnote)