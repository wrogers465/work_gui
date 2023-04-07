import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Work Assistant")

        #EMAIL COMPONENTS FRAME
        email_frm = tk.Frame(self)
        ice_email_btn = tk.Button(email_frm, text="ICE Email", command=None)

        #EMAIL COMPONENTS PLACEMENT
        email_frm.grid()
        ice_email_btn.grid()


def main():
    root = MainWindow()
    root.mainloop()


if __name__ == '__main__':
    main()