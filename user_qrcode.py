
import qrcode

user_name = input("enter name and telephon number ")


img = qrcode.make(user_name)


img.save("qecodeman.png")