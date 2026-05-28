class User: #membuat class bernama user untuk menambahkan data
    def __init__(self, username, password, role):
        self.username = username #menyimpan object ke username
        self.password = password #menyimpan object ke password
        self.role = role #menyimpan object ke role
    
    def to_dict(self):#fungsi mengubah object ke dictionary
        return{
            "username" : self.username,
            "password" : self.password,
            "role" : self.role
        }
    