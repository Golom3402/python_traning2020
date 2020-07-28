import jsonpickle
import os.path
import random
import string
from model.contact_model import Contact
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix="", maxlen=10, numeric=False):
    if numeric:
        text = string.digits*10
    else:
        text = string.ascii_lowercase+string.digits + string.ascii_uppercase + string.punctuation + " "*10
    return prefix+"".join([random.choice(text) for i in range(random.randrange(maxlen))])

def random_attribute():
    return random.choice(['', '', '', random_string(maxlen=15)])

testdata = [Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 20), last_name=random_string("last", 20),
                    mobile_tel=random_string(maxlen=10, numeric=True), home_tel=random_string(maxlen=15, numeric=True), work_tel=random_string(maxlen=19, numeric=True))
        for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))