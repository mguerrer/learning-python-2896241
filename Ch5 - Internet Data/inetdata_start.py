# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request
def main():
    pass # this is a placeholder, do-nothing statement
    weburl = urllib.request.urlopen("http://www.google.com")
    print("Result code:", weburl.getcode()  )
    data = weburl.read()
    print(data)

if __name__ == "__main__":
    main()
