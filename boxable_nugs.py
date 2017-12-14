
class BoxableNugs:

    @staticmethod
    def can_be_boxed(self, nugs):
        """Given a number of Nugs, returns true if they will all fit in MickyD's box sizes with no remainers.
        Box sizes are 20, 9 and 6"""
        if nugs == 0:
            return True

        if nugs < 0:
            return False

        if self.can_be_boxed(nugs - 20):
            return self.can_be_boxed(nugs - 20)

        if self.can_be_boxed(nugs - 9):
            return self.can_be_boxed(nugs -9)

        if self.can_be_boxed(nugs - 6):
            return self.can_be_boxed(nugs - 6)

        return False

    def run(self):

        str_nugs = input("How many nugs do you have\n")

        boxable = self.can_be_boxed(int(str_nugs))

        print("You have {} nugs, which {} be boxed".format(str_nugs, 'can' if boxable else 'can NOT'))
