import qrcode
import datetime
import time,os

# for i in range(120):
#     N = 10
#     res = '/camera ' + str(datetime.datetime.now())
#     print(res)
#     img = qrcode.make(res)
#     img.save("myqrcode.png")
#     time.sleep(2)

def main():
    filepath = os.path.join("static/img", "filename")
    print(filepath)


if __name__ == "__main__":
    main()