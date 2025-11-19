
def timark(f):
    
    import time

    def wrap():
        start = time.time()
        f()
        end = time.time()
        print('time = {}'.format(end - start))
    return wrap

@timark
def req():
    import requests
    wep = requests.get('http://ya.ru')

req()
