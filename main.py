import os
import pycurl


def api(root,filename):
    fullpath = "{}/{}".format(root, filename)
    filename = filename+"c"
    cmd = "luac_mta.exe -e3 -o {} {}".format(fullpath,fullpath)
    print(cmd)
    os.system(cmd)

def compile(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".lua")):
                api(root, name)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    compile('E:/dev/mta-saol/mods/deathmatch/resources/')

