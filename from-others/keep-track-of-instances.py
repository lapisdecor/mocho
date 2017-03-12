"""
This is as an example of how to keep track of class
instances. It was shared by someone at #python on freenode
but I can't remember his nickname.
"""


class KeepTrackOfMyInstances:
    my_instances = []

    def __init__(self, name):
        self.name = name
        self.my_instances.append(self)

    def __repr__(self):
        return f'An instance named {self.name}'

i1 = KeepTrackOfMyInstances('one')
i2 = KeepTrackOfMyInstances('two')

print(i1)
print(i2)
print(KeepTrackOfMyInstances.my_instances)

# An instance named one
# An instance named two
# [An instance named one, An instance named two]
