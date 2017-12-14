
class Boxable_Nugs:

    def can_be_boxed(self,nugs):
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

        strNugs = input("How many nugs do you have\n")

        boxable = self.can_be_boxed(int(strNugs))

        print("You have {} nugs, which {} be boxed".format(strNugs, 'can' if boxable else 'can NOT'))
