class Loader:

    def __init__(self, pkg, dir):
        dir = "" if dir == "." else dir.replace("/", ".") + "."
        if pkg and pkg != "__main__":
            dir = f"{pkg}.{dir}"
        self.p = dir

    def load(self, name):
        name = name.replace(".", "_")
        return __import__(self.p + name, None, None, (name,)).render
