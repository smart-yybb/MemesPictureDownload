import requests
import subprocess

if __name__ == '__main__':
    # url = 'https://i.pinimg.com/originals/19/d7/7e/19d77e60f0c43c714ef8bc3a48030ef4.jpg'
    # resp = requests.get(url)
    # print(resp)

    curl = 'curl https://i.pinimg.com/originals/19/d7/7e/19d77e60f0c43c714ef8bc3a48030ef4.jpg -o ./imgs/test.jpg'
    result = subprocess.run(curl, shell=True, stdout=subprocess.PIPE)
    print(result.returncode)