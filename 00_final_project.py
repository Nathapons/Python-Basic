from tkinter import ttk, Tk, Frame, Button, Label, Entry 
from tkinter import messagebox as msb


class StudentProgram:
    pass


class StudentGradeWinow(StudentProgram):
    
    def __init__(self):
        self.__default_topics_font = ('Arial', 30)
        self.__defaul_detail_font = ('Arial', 22)
        self.__default_treeview_header = ('Arial', 16, 'bold')
        self.__default_treeview = ('Arial', 12)
        self.__treeview_height = 11
        
        self.__program_name = 'Student Grade Program'
        
        self.__entries = []
        
    @staticmethod
    def get_gui_details():
        return [
            {'label': {'title': "Name:", 'font': ('Arial', 22), 'width': 15}, 'entry': {'justify': 'center', 'width': 15, 'font': ('Arial', 22)}},
            {'label': {'title': "Student Id:", 'font': ('Arial', 22), 'width': 15}, 'entry': {'justify': 'center', 'width': 15, 'font': ('Arial', 22)}},
            {'label': {'title': "Score:", 'font': ('Arial', 22), 'width': 15}, 'entry': {'justify': 'center', 'width': 15, 'font': ('Arial', 22)}},
        ]
    
    def create_ui(self):
        window = Tk()
        
        WIDTH = 800
        HEIGHT = 600
        
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width/2) - (WIDTH/2))
        y = int((screen_height/2) - (HEIGHT/1.8))
        
        window.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
        window.title(self.__program_name)
        window.resizable(0, 0)
        
        frame = Frame(window)
        title_label = Label(frame, text=self.__program_name, font=self.__default_topics_font, fg='white', bg='blue')
        frame.pack()
        title_label.grid(row=0, column=0, pady=10, ipadx=10)
        
        sub_frame = Frame(frame)
        sub_frame.grid(row=1, column=0, pady=5)
        for row, data in enumerate(self.get_gui_details()):
            label = Label(
                sub_frame, 
                text=data.get('label', {}).get('title', 'title'), 
                font=data.get('label', {}).get('font', self.__defaul_detail_font)
            )
            entry = Entry(
                sub_frame, 
                justify=data.get('entry', {}).get('justify', 'left'),
                font=data.get('entry', {}).get('font', 20), 
                width=data.get('entry', {}).get('width', 20),
            )
            self.__entries.append(entry)
            
            label.grid(row=row, column=0, padx=5, pady=10)
            entry.grid(row=row, column=1, padx=5, pady=10)
        
        button = Button(frame, text='Submit', font=self.__defaul_detail_font, width=10, command=self.submit_grade)
        button.grid(row=row+1, column=0, ipadx=10, pady=10)
        
        style = ttk.Style()
        style.configure("Treeview.Heading", font=self.__default_treeview_header)
        style.configure("Treeview", font=self.__default_treeview)
        
        headers = ['Name', 'Student ID', 'Score', 'Grade']
        self.treeview = ttk.Treeview(frame, column=headers, show='headings', height=self.__treeview_height)
        for header in headers:
            self.treeview.heading(header, text=header)
            self.treeview.column(header, anchor='center', width=150, minwidth=0)
        self.treeview.grid(row=row+2, column=0)

        window.mainloop()
        
    def submit_grade(self):
        entries = [entry.get() for entry in self.__entries]
        if not all(entries):
            msb.showwarning("Warning", "Some Entry is not fill in!")
        else:
            msb.showinfo("Information", "Complete")
            self.set_blank_entry()
            
            
    def set_blank_entry(self):
        for entry in self.__entries:
            entry.delete('0', 'end')


if __name__ == '__main__':
    student_grade = StudentGradeWinow()
    student_grade.create_ui()
