

from tkinter import *
from tkinter import messagebox


import mysql.connector



class Login:

    def __init__(self):

        self.conn=mysql.connector.connect(host='localhost', user='root', password='', database='tinder2')
        self.mycursor=self.conn.cursor()


        self.root=Tk()

        self.root.title('BG-finder')
        self.root.minsize(250,350)
        self.root.maxsize(250,350)


        self.email_label=Label(self.root, text='Enter email')
        #label keyword to display respective text and in braces it has self.root and the content of the box
        self.email_label.pack()

        self.email_input=Entry(self.root)#to enter email in the white box
        self.email_input.pack()

        self.password_label=Label(self.root, text='Enter password')
        self.password_label.pack()

        self.password_input=Entry(self.root)
        self.password_input.pack()

        self.button=Button(self.root, text='Login', command=lambda  :self.perform())#adding login button....command=lambda to create another function perform ()
        self.button.pack()

        self.result=Label(self.root, text='', fg='Red')#fg is foreground i.e font color
        self.result.pack()


        self.new_user=Label(self.root, text="""Not a Member? Create account -->""")
        self.new_user.pack()

        self.button_new_user=Button(self.root, text='I wanna create an account', command=lambda :self.create())
        self.button_new_user.pack()
        self.root.mainloop()



    def perform(self):

        email=self.email_input.get()
        password=self.password_input.get()
        #the attributes are fetched from the box and put in the variables email and passqword resp.

        self.mycursor.execute("""SELECT * FROM `users` WHERE  `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
        #entry to database from vairables to database


        user_list=self.mycursor.fetchall() #since read op



        if len(user_list)>0:
            self.result.configure(text='Welcome')#configure keyword helps to change the result label to welcome on correct login
            self.current_user_id=user_list[0][0]
            self.root3=Tk()#after welcome this box opens

            self.root3.maxsize(600, 600)
            self.root3.minsize(600, 600)

            self.user_menu_options = Label(self.root3, text="""
            ----How would u like to proceed?--------
                1.Enter 1 to view all users
                2.Enter 2 to view all proposals
                3.Enter 3 to view all requests
                4.Enter 4 to view all matches
                5.Enter anything else to logout""")
            self.user_menu_options.pack()

            self.option_entry = Entry(self.root3)#for entering the option
            self.option_entry.pack()

            self.option_enter_button=Button(self.root3, text='Enter', command=lambda :self.Enter_option())#enter button
            self.option_enter_button.pack()

            self.back_button=Button(self.root3, text='Quit', command=lambda :self.close_login_box())#to go back from the login dialog box to previous
            self.back_button.pack()



            self.root3.mainloop()

        else:
            self.result.configure(text='Incorrect Credentials')


    def close_login_box(self):#to close login box
        self.root3.destroy()




    def create(self):

        self.root1=Tk()

        self.root1.title('Create Account')

        self.root1.maxsize(400,400)
        self.root1.minsize(400,400)

        self.name_label_new = Label(self.root1, text='Enter name')
        self.name_label_new.pack()

        self.name_input_new = Entry(self.root1)
        self.name_input_new.pack()

        self.email_label_new = Label(self.root1, text='Enter email')
        self.email_label_new.pack()

        self.email_input_new = Entry(self.root1)
        self.email_input_new.pack()

        self.password_label_new = Label(self.root1, text='Enter password')
        self.password_label_new.pack()

        self.password_input_new = Entry(self.root1)
        self.password_input_new.pack()

        self.gender_label_new = Label(self.root1, text='Enter gender')
        self.gender_label_new.pack()

        self.gender_input_new = Entry(self.root1)
        self.gender_input_new.pack()

        self.age_label_new = Label(self.root1, text='Enter age')
        self.age_label_new.pack()

        self.age_input_new = Entry(self.root1)
        self.age_input_new.pack()

        self.city_label_new = Label(self.root1, text='Enter city')
        self.city_label_new.pack()

        self.city_input_new = Entry(self.root1)
        self.city_input_new.pack()

        self.button_create_new = Button(self.root1, text='Create my account now', command=lambda: self.insert())
        self.button_create_new.pack()

        self.root1.mainloop()

    def insert(self):
        name=self.name_input_new.get()
        email =self.email_input_new.get()
        password = self.password_input_new.get()
        gender = self.gender_input_new.get()
        age= self.age_input_new.get()
        city=self.city_input_new.get()


        self.mycursor.execute(""" INSERT INTO `users` (`user_id`, `name`, `email`, `password`,`gender`, `age`, `city`) VALUES (NULL, '{}','{}','{}','{}','{}','{}')""".format(name,email,password,gender,age,city))
        self.conn.commit()
        messagebox.showinfo("Create my account now", "Account Created Successfully!!")
        self.close_insert_box()


    def close_insert_box(self):# to destroy create account now  box
        self.root1.destroy()


    def Enter_option(self):
        entered_option = self.option_entry.get()

        if entered_option == '1':#to view all users
            self.mycursor.execute(
                """SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))
            all_users_list = self.mycursor.fetchall()

            self.option_1=Tk()#to show all users in a seperate dialog box
            self.option_1.title('View All Users')
            self.option_1.maxsize(400,400)
            self.option_1.minsize(400,400)

            for i in all_users_list:
                self.show_users= Label(self.option_1, text=(i[0],i[1],i[4],i[5],i[6]))
                self.show_users.pack()
            self.id_to_propose=Label(self.option_1, text='Enter the user id of the user whom u wanna propose')
            self.id_to_propose.pack()
            self.entry_for_propose=Entry(self.option_1)
            self.entry_for_propose.pack()
            self.proposal_entry_button=Button(self.option_1, text='Enter', command=lambda :self.Entry_for_proposal_button())
            self.proposal_entry_button.pack()

            self.all_users_back=Button(self.option_1, text='Go Back', command=lambda :self.close_all_users())
            self.all_users_back.pack()
            self.option_1.mainloop()




        if entered_option == '2':#to view all proposals

            self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`juliet_id` WHERE p.`romeo_id` LIKE '{}'""".format(
                    self.current_user_id))
            self.proposed_user_list = self.mycursor.fetchall()

            self.option_2=Tk()
            self.option_2.title('View Proposals')
            self.option_2.maxsize(300,300)
            self.option_2.minsize(300, 300)
            for i in self.proposed_user_list:
                self.show_proposals=Label(self.option_2, text=(i[4],i[7],i[8],i[9]))
                self.show_proposals.pack()
                self.line1=Label(self.option_2, text='------------------------------')
                self.line1.pack()

            self.all_proposals_back = Button(self.option_2, text='Go Back', command=lambda: self.close_all_proposals())
            self.all_proposals_back.pack()

            self.option_2.mainloop()

        if entered_option == '3':#to view all requests
            self.mycursor.execute(
                """SELECT * FROM `proposals` p JOIN `users` u ON u.`user_id`=p.`romeo_id` WHERE p.`juliet_id` LIKE '{}'""".format(
            self.current_user_id))
            self.proposed_request_list = self.mycursor.fetchall()

            self.option_3=Tk()
            self.option_3.title('View Requests')
            self.option_3.maxsize(300,300)
            self.option_3.minsize(300,300)


            for i in self.proposed_request_list:
                self.show_requests = Label(self.option_3, text=(i[4], i[7], i[8], i[9]))
                self.show_requests.pack()
                self.line2 = Label(self.option_3, text='------------------------------')
                self.line2.pack()

            self.all_requests_back = Button(self.option_3, text='Go Back', command=lambda: self.close_all_requests())
            self.all_requests_back.pack()


            self.option_3.mainloop()

        if entered_option == '4':
            self.mycursor.execute(
                """SELECT * FROM `proposals` p
                    JOIN `users` u ON u.`user_id`=p.`juliet_id`
                    WHERE `juliet_id` IN
                    (SELECT `romeo_id` FROM `proposals` WHERE `juliet_id` LIKE '{}') AND `romeo_id` LIKE '{}'""".format(self.current_user_id, self.current_user_id))
            self.matches_list = self.mycursor.fetchall()

            self.option_4=Tk()
            self.option_4.title('Matches Found')
            self.option_4.maxsize(400, 400)
            self.option_4.minsize(400, 400)

            for i in self.matches_list:
                self.show_matches = Label(self.option_4, text=(i[4], i[7], i[8], i[9]))
                self.show_matches.pack()
                self.line3 = Label(self.option_4, text='------------------------------')
                self.line3.pack()

            self.all_matches_back = Button(self.option_4, text='Go Back', command=lambda: self.close_all_matches())
            self.all_matches_back.pack()


            self.option_4.mainloop()

        if entered_option == '5':
            self.current_user_id=0
            #self.Logged_out=Label(self.root3, text='Logged Out!')
            #self.Logged_out.pack()
            messagebox.showinfo("", "Logged Out Successfully!!")
            self.close_login_box()

    def close_all_users(self):
        self.option_1.destroy()

    def close_all_proposals(self):
        self.option_2.destroy()

    def close_all_requests(self):
        self.option_3.destroy()

    def close_all_matches(self):
        self.option_4.destroy()


    def Entry_for_proposal_button(self):
        self.juliet_id=self.entry_for_propose.get()

        self.mycursor.execute("""SELECT `juliet_id` FROM `proposals` WHERE `romeo_id` LIKE '{}' AND `juliet_id` LIKE '{}'""".format(self.current_user_id,self.juliet_id))
        proposed_already = self.mycursor.fetchall()
        for i in proposed_already:
            self.notify_if_already_proposed=Label(self.option_1, text='Already Proposed', fg='Red')
            self.notify_if_already_proposed.pack()
            break
        else:
            self.propose(self.current_user_id, self.juliet_id)

    def propose(self, romeo_id, juliet_id):

        self.mycursor.execute("""INSERT INTO `proposals`(`proposal_id`,`romeo_id`,`juliet_id`) VALUES (NULL,'{}','{}')""".format(romeo_id,juliet_id))
        self.conn.commit()
        self.Proposal_Successful=Label(self.root3, text='Proposals Successfully Sent. Fingers Crossed!!', fg='Red')
        self.Proposal_Successful.pack()







obj1=Login()