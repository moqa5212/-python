class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def __init__(self):
        self.dad = Parent()

    def altered(self):
        print("CHILD")
        self.dad.altered()
        print("CHILD")
        super(Child, self).altered()



dad = Parent()
son = Child()

dad.altered()
son.altered()
