# Author Hunter Mahoney/Erika Tix
# Created 4/9/19  Updated 4/10/19
# Test file to connect MongoDB Atlas and Pycharm

import MenuCreations
import AdminLogin


def main():

    client = AdminLogin.loginDatabase()

    MenuCreations.loginSignup(client)

if __name__ == '__main__':
    main()








