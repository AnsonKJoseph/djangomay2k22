class Course:
    def __init__(self,**kwargs):
        self.c_id=kwargs.get("c_id")
        self.c_name=kwargs.get("c_name")
        self.c_fee=kwargs.get("c_fee")
    def print_course(self):
        print(self.c_id,self.c_name,self.c_fee)
