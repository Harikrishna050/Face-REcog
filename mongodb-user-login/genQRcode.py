import qrcode
import datetime
import time


class GenerateQR:
    def QRcodeFunc(self):
        # filename = "myqrcode.png"
        for i in range(120):
            N = 10
            res = '/camera ' + str(datetime.datetime.now())
            print(res)
            img = qrcode.make(res)
            img.save("C:/Users/91637/Documents/LogIn/mongodb-user-login/static/img/myqrcode.png")
            time.sleep(2)

def main():
    genQR = GenerateQR()
    genQR.QRcodeFunc()

if __name__ == "__main__":
    main()