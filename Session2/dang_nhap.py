import getpass
user = "1234"
pass_word = "1234"

u = input("nhap username:")
pw = getpass.getpass("nhap password:")#làm ẩn pass

if user == u:
    if(pass_word == pw):
        print("dang nhap thanh cong")
    else:
        print("sai passs")
else:
    print("sai user name")