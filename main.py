import os, crypt, random, sys, time, subprocess

def countLines(filePath):
    """ Counts lines from file """
    file = open(filePath, "r")
    length = 0
    for regel in file:
        length += 1
    file.close()
    return length

def hashPassword(passw):
    """Hashes password with random salt """
    salt = crypt.mksalt(crypt.METHOD_SHA512) #generates salt
    return crypt.crypt(passw, salt) #returns encrypted password

def start(filename):
    """Loops through file and creates users based on data"""
    file = open(filename, "r")
    start_time = time.time()
    length = countLines(filename)

    for i, regel in enumerate(file):
        if len(regel) > 4:
            #Split
            gegevens = regel.strip().split(":")  #Remove white space and after that split :
            #Check for correct splitter
            if len(gegevens) == 1 or len(gegevens) > 2: #check for problems
                sys.stdout.write("\nNot correct file format! Error on line: " + str(i + 1) + "\n")
                sys.stdout.flush()
                break
            #Setup
            password = hashPassword(gegevens[1]);
            process1 = subprocess.Popen(['useradd', '-m', gegevens[0].lower(), '-p', password], stdout=subprocess.PIPE)

            #Run
            output = process1.communicate()[0]

            #Check for errors
            if process1.returncode != 0:
                sys.stdout.write("\n" + str(output) + "\nError on line: " + str(i + 1) + "\n")
                sys.stdout.flush()
                break
            #Generate message
            message = "User with username " + gegevens[0] + " created\n"
            oneoutof = "[" + str(i + 1) + "/" + str(length) + "]"
            percent = str(round(100 / length * (i + 1))) + "%"
            speed = str(round(i / (time.time() - start_time), 2)) + " u/s"
            #Output
            sys.stdout.write("\r" + message + oneoutof + " " + percent + " " + speed)
            sys.stdout.flush()
    file.close()

def main():
    """Main of the file"""
    if len(sys.argv) == 1:
        print("Please specify a file")
    elif not os.path.isfile(sys.argv[1]):
        print("File doesnt exist")
    else:
        start(sys.argv[1])

main()