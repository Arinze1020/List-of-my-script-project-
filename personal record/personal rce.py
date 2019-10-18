class Record:

    def personal(self):

        self.Name = input('Enter your name\n')
        self.Reg_No = int(input('Enter your reg no \n'))
        print(self.Name,'\n',self.Reg_No)

records = Record()

records.personal()