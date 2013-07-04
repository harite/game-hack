import random
from time import sleep
import site

#Resources. Feel free to add and remove from these lists as you please.
humanlist = ['Andre', 'Bob', 'Clive', 'Cornelius', 'Darren', 'Elmer', 'Frank', 'Garrett', 'Harald', 'Ignatius', 'Joel', 'Katy', 'Gary', 'Nancy', 'Schlomo', 'Billy']
domainlist = ['ispcp', 'freehost', 'dickhost', 'lelhosting', 'jewhost', 'pomf', 'oyvey', 'monsquaz', 'queerhost', 'olm', 'register', 'neustar', 'on.nimp', 'namecheap', 'bigrock', 'dnsbelgium', 'gandi', 'enom', 'hover']
domainextlist = ['.aq', '.as', '.biz', '.cat', '.com', '.coop', '.dk', '.info', '.int', '.aq', '.ao', '.am', '.name', 'nobrain', '.net', '.org', '.al', '.pro', '.tel', '.travel', '.xxx', '.edu', '.gov', '.mil', '.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.aw', '.ax', '.az', '.bd', '.BruteForcerOn', '.bh', '.bi', '.bj', '.bm', '.bn', '.bt', '.bv', '.bw', '.by', '.bz', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cm', '.cn', '.cs', '.yu', '.cv', '.cx', '.sj', '.bl', '.mf', '.eh', '.um', '.xxx', '.dd', '.dz', '.ec', '.eh', '.er', '.et', '.fj', '.fm', '.fo', '.ga', '.gb', '.gd', '.ge', '.gg', '.gh', '.gm', '.gl', '.gn', '.gp', '.gq', '.gs', '  .gt', '.gu', '.gt', '.gy', '.gw', '.hk', '.hm', '.ht', '.il', '.io', '.iq', '.ir', '.is', '.je', '.jo', '.ke', '.kg', '.ki', '.km', '.kn', '.kp', '.kw', '.ky',  '.kz',  '.la',  '.lb',  '.lc',  '.lk',  '.lr',  '.ls',  '.lt',  '.ly',  '.mg',  '.mh',  '.mk',  '.ml',  '.mm',  '.mo',  '.mp',  '.ms', '.mz',  '.ne',  '.nf',  '.nc',  '.np',  '.nr',  '.nu',  '.om',  '.pg',  '.pk',  '.pn',  '.ps',  '.pw',  '.qa',  '.re',  '.ru',  '.su',  '.rw',  '.sa',  '.sb',  '.sc',  '.sl',  '.sm',  '.so', '.ss', '.sr', '.st', '.sv', '.sx', '.sy', '.sz', '.tc', '.td', '.tf', '.tg', '.tk', '.tl', '.tp', '.tn', '.tt', '.tz', '.ug', '.uz', '.va', '.vc', '.vg', '.vi', '.wf', '.ws', '.ye', '.yt', '.za', '.zm', '.zw']
ailist = ['ARCTURUS', 'BromIDE', 'CLAPBURGER', 'SHODAN', 'Windows 3.1', 'GOLDBERGSTEIN', 'AM', 'KIKE', 'ISABELLA', 'KEBAB', 'TOPLAL', 'BUTCH.EXE', 'MEEN', 'MONSQUAZ', 'ANATOLY', 'singularity', ' ACID', 'KORENCHKIN', 'VINCENT', 'Zyzz', 'SAKURANBO', 'DARKHOLME v1.2', 'KOIZUMI', 'HAPPENING', 'FILTERS', 'HEATMAN']
weakpasslist = ['secret', 'password', '1234', 'qwerty', 'fuckyou', 'pizzatrick', 'umad', 'slaphappy', 'innit', 'getout', 'please', 'starwars', 'rosebud', 'debug', 'letmein']
medpasslist = ['4RiF8104', 'nW8f5MUq', 'WuMpUsES', 'znO5420d', 'YMx6k34z', 'xnl59R5w', '7u2n024B', 'Z32f2689', 'm6NsU06p', 'Monsquaz', 'qH0nSZdp', 'ybGRW5FJ', 'aZ9Yl47f', '92566IUe', 'N155BJ3h', 'N155BJ3h']
strongpasslist = ['Oc0ttOJlKjTY5Uc', 'Nx7n49Kx4R6Zl1B', 'LYEYl22m4g68h6J', 'tIwfLIIY35UEBxf', 'RH37T3o3Jh2jK3l', 'DW7t5odj1lO1MbP', 'Mu127D2V5S5ZQ5g', 's4e5FnwY6cQh5N2', 'c46H196h254218S', 'K42S98RQdh3plB8', '5383W2T40k374R3', 'CheckYourPrivileges', 'n2kWEB8zErNvDLX', 'OBB5W5vFCE93h2X', 'PinkArrowsDown', 'GreenArrowsUp']
adminpasslist = ['IWantToJiiiiiiiveAndWatchMonsquazAllDay', 'M0D7V055358L721f1Bq72gUig2T768', 'c085Ty684Cnj21S6sNBZPU1594DqTD', 'YkznXPVrDgSpcOhJsJjXlusEy3txfl', 'br676zOK353h8GtOj56nh151sOOBTf', 'VrIz7MPe2NeQCye4fu4GrTwEkJFKgA', '7y6sDha727r882O9m15Rh2l126WME2', 'ex8567w4529w3iS307183DN3y8JZ2Q', 'qsG53EFZ13Hq44yC1gD1XYnkw1WH9Y', '1h6U2g547XM3O0036EQ227E2v126L5', '28Mt2bWd78c59P0vt836Cf12gm28hv', 'y23O86m0m346z7ql8821n55vw1tSrd', 'c88v15no3u6XO71N72WspL6NQ16048', '8fX5GOsJ44AJ8l8E28KcfUVn25K5QC', 'nY1BlH1u5Nfl3447522fC60I75kG21', 'MiEulAKneMVjCNcmYb8pxQiKM7dnfN']
#Seriously, make any modifcations to the above that you please, just make sure they're consistent.

#Randomises the client, victim, host AI, IP and password each time you start up. Muh innovayshun.
misvictim = random.choice(humanlist) #Chooses username for server
misclient = random.choice(humanlist)  # Chooses random name for client
misdomain = random.choice(domainlist) #Chooses random domain for server
misexten = random.choice(domainextlist) #Chooses random extension for server
mispassweak = random.choice(weakpasslist) #Chooses a random weak password. (For getting to the terminals)
mispassmed = random.choice(medpasslist) #Chooses a random med password. (For going between terminals)
mispassstrong = random.choice(strongpasslist) #Chooses a random strong password (For going between the AI core)
mispassadmin = random.choice(adminpasslist) #Chooses a random admin password (For Sudo-tier shit)
misboss = random.choice(ailist) #Choose the name of the boss nigger
mailnum = random.randint(1,999) #Email Address number.
misip1 = random.randint(1,255) #First integer of IP address
misip2 = random.randint(1,255) #Second integer of IP address
misip3 = random.randint(1,255) #Third integer of IP address
misip4 = random.randint(1,255) #Fourth integer of IP address
misip = "%i.%i.%i.%i" % (misip1, misip2, misip3, misip4) #Merging the IP integers into one string
misserv = "%s@%s%s" % (misvictim, misdomain, misexten) #Merging the username, domain and TLD to one string

#CLASSES R 4 GAYLORDS ID RATHER SMOKE WEED
#This is your own home command line, you stupid shit.
def OwnConsole():
    cli = input("root>")
    if "ping" in cli:
        ping(cli)
    elif cli == "ssh": #SSH client
        SSH()
    elif cli == "help":#help command
        help()
    elif cli == "sshcrack":#SSH cracking program.
        print("Warning: Only use this program while an SSH connection is active.")
        OwnConsole()
    elif cli == "exit":
        quit()
    else:
        print("Invalid command.") #Fallback in case you input utter shit.
        OwnConsole()

def help(): #Help command. If you add anything, update this.
    print ("""List of valid commands:
ping
sshcrack
SSH
""")
    OwnConsole()

#sshcrack (Getting into the mainframe in the first place)

def ping(cli):
    if cli == "ping %s" % misip:
        print("Pinging IP...")
        print("64 bytes from %s (%s): icmp_req=3 ttl=57 time=45.3 ms" % (misserv, misip))
        sleep(1)
        print("64 bytes from %s (%s): icmp_req=3 ttl=57 time=45.3 ms" % (misserv, misip))
        sleep(1)
        print("64 bytes from %s (%s): icmp_req=3 ttl=57 time=45.3 ms" % (misserv, misip))
        sleep(1)
        print("")
        print("Ping statistics for %s:" % (misip))
        print("    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),")
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = 1ms, Maximum = 4ms, Average = 3ms")
        OwnConsole()
    else:
        print ("ping: Unknown Host.")
        OwnConsole()

#And the SSH client. This isn't merged into the console, one, because the raw_input prompt changes and two, I don't want to nest any 'if' commands more than 2 deep, or else it becomes a mess.
def SSH():
    SSHInput = input("SSH>")
    if SSHInput == "connect %s" % misserv:
        print("Connecting...")
        ServerLoginScreen()
    elif SSHInput == "connect":
        print("Error: No IP specified.")
        SSH()
    elif "back" in SSHInput:
        OwnConsole()
    else:
        print("Invalid Command. Type 'back' to go back to the console.")
        SSH()

def quit():
    print("Exiting...")
    sleep(2)
#
#
# Insert more programs here. (Top lel)
#
#
#

#OWN CONSOLE PROGRAMS GO ABOVE THIS LINE.

#REMOTE HOST 1 (Terminal 1)
def ServerLoginScreen():
    print("Welcome to Terminal A of this mainframe.")
    print("Please input your password.")
    passattempt = input('>')
    if "sshcrack" in passattempt:
        print("sshcrack working..........................\n...............................\n.........................................................\n.............................\n......................")
        TerminalA()

    elif passattempt == mispassweak:
        print("Password verified.")
        TerminalA()
    else:
        print("Password invalid.")
        print("Warning. Potential threat detected. Connection terminated.")
        OwnConsole()

def TerminalA():
    print ("\n\nCongrendulates")

#REMOTE HOST 2 (Terminal 2)

#REMOTE HOST 3 (Terminal 3)

#REMOTE HOST 4 (Terminal 4)

#REMOTE HOST 5 (Terminal 5)

#Default error handler - Fall back within the function if possible.
def invalid_command():
    print("You shouldn't be seeing this.")
    OwnConsole()

#Everything below here is seen by the player.
print("")
print("  #   #     #        #####  #   #  #####  ###  ")
print("  #   #    # #      #       #  #   #      #  # ")
print("  #   #    # #     #        # #    #      #   #")
print("  #####   #   #   #         ##     #####  #  # ")
print("  #   #   #####    #        # #    #      # #  ")
print("  #   #  #     #    #       #  #   #      #  # ")
print("  #   #  #     #     #####  #   #  #####  #   #")
#Yes, yes. A title would be nice.
print("")
print("Original Concept by James Butcher.")  # "But muh simplicity" - Every Batch user ever.
print("Shameless Python remake by Bromine.") # I prefer Bromine to real names.
print("")

name = input("What's your name?: ") # Yes, it would be nice if we had a name to work with.

#Email you receive at the start. Should include a command to re-read the email, but this'd involve turning the print email commands into a function, which I'd probably need Pygame to do properly.
print("""You receive an email.
The email reads...""")
print("")
print ("""To: %s%i@yahoo.co.uk
From: %s@faggotsecurity.org
---------------------------------------
Hey %s, some dipshit hacked into my server last night and I was wondering if you could get him back for me. Luckily, none of my files were damaged, but I fear that if he gets in again, he'll do some real damage.

One thing he forgot to do was delete my log file, so I have his IP.

His IP is %s, so you might want to try pinging the ip, to see if he has anything you can SSH into.

I hope you can do something. I'm asking you because I know you won't tell anyone. If any of my colleagues hear of this, it could spell the end for my business.

Thanks in advance.

%s""" % (name, mailnum, misclient, name, misip, misclient))

print("")
print("")
print("What would you like to do now?") #IT BEGIIIIIIIIIIIIIIIIIIIIIINS
print("Type 'help' if you don't know what to do.") #Refer to help()

BruteForcerOn = 0
OwnConsole() #Hackitalism, ho!
