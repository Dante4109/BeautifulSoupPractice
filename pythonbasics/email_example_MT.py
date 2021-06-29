import imaplib
import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor


IMAP_SERVER = 'imap.gmail.com'
USERNAME = 'smtpsender4109@gmail.com'
PASSWORD = 'TOSS#2017'


def download_emails(ids):
    client = imaplib.IMAP4_SSL(IMAP_SERVER)
    client.login(USERNAME, PASSWORD)
    client.select()
    for i in ids:
        print(f'Downloading mail id: {i.decode()}')
        _, data = client.fetch(i, '(RFC822)')
        with open(f'emailsMT/{i.decode()}.eml', 'wb') as f:
            f.write(data[0][1])
    client.close()
    print(f'Downloaded {len(ids)} mails!')


start = time.perf_counter()

client = imaplib.IMAP4_SSL(IMAP_SERVER)
client.login(USERNAME, PASSWORD)
client.select()
_, ids = client.search(None, 'ALL')
ids = ids[0].split()
ids = ids[:100]
client.close()

number_of_chunks = 10
chunk_size = 10


with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_chunks) as executor:
    tasks = []
    for i in range(number_of_chunks):
        chunk = ids[i*chunk_size:(i+1)*chunk_size]
        tasks.append(executor.submit(download_emails, chunk))

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
