from datetime import datetime

def main():
    id = input("TikTok ID : ")
    if id.isnumeric() is False:
        print("[ERR] Something is wrong")
        return
    id = bin(int(id))[2:][0:31]
    if len(id) != 31:
        print("[ERR] Something is wrong")
        return
    print("Date : {}".format(datetime.fromtimestamp(int(id, 2))))

if __name__ == "__main__":
    main()