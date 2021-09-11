from Pendrill import Pendrill
from PendrillMainGUI import PendrillMainGUI
from CodeInjectionGUI import CodeInGUI
def main():
    pen = Pendrill("temp")
    gui = PendrillMainGUI(pen)
    # gui.top.mainloop()
    # url = "http://natas15.natas.labs.overthewire.org"
    # password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
    # gui.urlEntry.insert(0, url)
    # gui.authUsernameEntry.insert(0, "natas15")
    # gui.authPasswordEntry.insert(0, password)

main()
