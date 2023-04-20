import bcrypt

class Auth():

    def verify_password(passwordSasie, passwordDb):
        return bcrypt.checkpw(passwordSasie, passwordDb)

    def get_user(mail):
        return db.users.find_one({"mail": f"{mail}"})['password']