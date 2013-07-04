import random
from time import sleep
#Resources. Feel free to add and remove from these lists as you please.
humanlist = ['Andre', 'Bob', 'Clive', 'Cornelius', 'Darren', 'Elmer', 'Frank', 'Garrett', 'Harald', 'Ignatius', 'Joel', 'Katy', 'Gary', 'Nancy', 'Schlomo', 'Bill']
domainlist = ['ispcp', 'freehost', 'dickhost', 'lelhosting', 'jewhost', 'pomf', 'oyvey', 'monsquaz', 'queerhost', 'olm', 'register', 'neustar', 'on.nimp', 'namecheap', 'bigrock', 'dnsbelgium', 'gandi', 'enom', 'hover']
domainextlist = ['.aq', '.as', '.biz', '.cat', '.com', '.coop', '.info', '.int', '.aq', '.ao', '.am', '.name', '.net', '.org', '.al', '.pro', '.tel', '.travel', '.edu', '.gov', '.mil', '.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.aw', '.ax', '.az', '.bd', '.bf', '.bh', '.bi', '.bj', '.bm', '.bn', '.bt', '.bv', '.bw', '.by', '.bz', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cm', '.cn', '.cs', '.yu', '.cv', '.cx', '.sj', '.bl', '.mf', '.eh', '.um', '.xxx', '.dd', '.dz', '.ec', '.eh', '.er', '.et', '.fj', '.fm', '.fo', '.ga', '.gb', '.gd', '.ge', '.gg', '.gh', '.gm', '.gl', '.gn', '.gp', '.gq', '.gs', '  .gt', '.gu', '.gt', '.gy', '.gw', '.hk', '.hm', '.ht', '.il', '.io', '.iq', '.ir', '.is', '.je', '.jo', '.ke', '.kg', '.ki', '.km', '.kn', '.kp', '.kw', '.ky',  '.kz',  '.la',  '.lb',  '.lc',  '.lk',  '.lr',  '.ls',  '.lt',  '.ly',  '.mg',  '.mh',  '.mk',  '.ml',  '.mm',  '.mo',  '.mp',  '.ms', '.mz',  '.ne',  '.nf',  '.nc',  '.np',  '.nr',  '.nu',  '.om',  '.pg',  '.pk',  '.pn',  '.ps',  '.pw',  '.qa',  '.re',  '.ru',  '.su',  '.rw',  '.sa',  '.sb',  '.sc',  '.sl',  '.sm',  '.so', '.ss', '.sr', '.st', '.sv', '.sx', '.sy', '.sz', '.tc', '.td', '.tf', '.tg', '.tk', '.tl', '.tp', '.tn', '.tt', '.tz', '.ug', '.uz', '.va', '.vc', '.vg', '.vi', '.wf', '.ws', '.xxx', '.ye', '.yt', '.za', '.zm', '.zw']
ailist = ['ACID', 'AM', 'ANDY-SEMPAI', 'ARCTURUS', 'BromIDE', 'BUTCH.EXE', 'CLAPBURGER', 'DARKHOLME', 'FILTERS', 'GOLDBERGSTEIN', 'GUMBY', 'HAPPENING', 'HEATMAN', 'ISABELLA', 'KEBAB', 'KOIZUMI', 'MEEN', 'MONSQUAZ', 'SHODAN', 'singularity', 'LAL', 'VINCENT', 'Windows 3.1', 'Zyzz']
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
    localcli = raw_input("root>") 
    if "quicksniff" in localcli: 
        quicksniff(localcli) #What the fuck is (self) for, sonny jim?
    elif localcli == "ssh": #SSH client
        SSH()
    elif localcli == "help":#help command
        help()
    elif localcli == "sshcrack":#SSH cracking program.
        print "Warning: Only use this program while an SSH connection is active."
        OwnConsole()
    else: 
        print "Invalid command." #Fallback in case you input utter shit.
        OwnConsole()

def help(): #Help command. If you add anything, update this.
    print """List of valid commands:
quicksniff
sshcrack
ssh
"""
    OwnConsole()

#sshcrack (Getting into the mainframe in the first place)

def quicksniff(localcli):
    if localcli == "quicksniff %s" % misip:
        qsping = random.randint(10,100)
        print "Sniffing IP for terminals..."
        print "Location found."
        print "Pinging terminals."
        print "All but (1) offline."
        print "printing results."
        print "--------------------------------------------------------------------------------"
        print "IP                 Domain                  Status            Ping"
        print "%s   %s                     Online                %ims" % (misip, misserv, qsping)
        print "--------------------------------------------------------------------------------"
        OwnConsole()
    else:
        print "ping: Unknown Host."
        OwnConsole()

#And the SSH client. This isn't merged into the console, one, because the raw_input prompt changes and two, I don't want to nest any 'if' commands more than 2 deep, or else it becomes a mess.
def SSH():
    print "sshclient v1.53.6 active. To use, simply input the domain."
    SSHInput = raw_input("SSH>")
    if SSHInput == "%s" % misserv:
        print "Connecting..."
        ServerLoginScreen()
    elif SSHInput == "connect":
        print "Error: No domain specified."
        SSH()
    elif SSHinput == "help":
        print "To connect to a domain, simply type it."
    elif "back" in SSHInput:
        OwnConsole()
    else:
        print "Invalid Command. Type 'back' to go back to the console."
        SSH()

#
#
# Insert more programs here. (Unlikely)
#
#
#

#OWN CONSOLE PROGRAMS GO ABOVE THIS LINE.

#Between Host + Local
def ServerLoginScreen():
    print "Welcome to Terminal A of this mainframe."
    print "Please input your password."
    passattempt = raw_input('>')
    if "sshcrack" in passattempt:
        print "sshcrack working..........................\n...............................\n.........................................................\n.............................\n......................"
        TerminalA()
    elif passattempt == mispassweak:
        print "Password verified."
        print "Loading terminal kernel..."
        print "This terminal is running Archlinux 2013 v1.0.3"
        TerminalA()
    else:
        print "Password invalid."
        print "Warning. Potential threat detected. Connection terminated."
        OwnConsole()
#Between Host Terminals and Sysop Terminal
#Between Sysop Terminal and AI
#REMOTE HOST 1 (Terminal 1)

def TerminalA():
   raw_input
#REMOTE HOST 2 (Terminal 2)

#REMOTE HOST 3 (Terminal 3)

#REMOTE HOST 4 (Terminal 4)

#REMOTE HOST 5 (Terminal 5)

#REMOTE HOST 6 (SYSOP TERMINAL)

#REMOTE HOST 7 (AI CORE)
#Speech will always be the first thing the hacker sees upon breaching the AI core.
def AiSpeech(): #PLEASE PLEASE FUCKING WRITE THIS TO A FILE. IT HURTS MY SOUL TO LOOK AT IT.
    if misboss == "ACID": #AI name
        print ""
 #speech
        coremain()
    elif misboss == "AM": #AI name
        print "" #speech
        coremain()
    elif misboss == "ANDY-SEMPAI": #AI name
        print "" #speech
        coremain()
    elif misboss == "ARCTURUS": #AI name
        print "" #speech
        coremain()
    elif misboss == "BromIDE": #AI name
        print "" #speech
        coremain()
    elif misboss == "BUTCH.EXE": #AI name
        print "" #speech
        coremain()
    elif misboss == "CLAPBURGER": #AI name
        print "" #speech
        coremain()
    elif misboss == "DARKHOLME": #AI name
        print "" #speech
        coremain()
    elif misboss == "FILTERS": #AI name
        print "" #speech
        coremain()
    elif misboss == "GOLDBERGSTEIN": #AI name
        print "" #speech
        coremain()
    elif misboss == "GUMBY": #AI name
        print "" #speech
        coremain()
    elif misboss == "HAPPENING": #AI name
        print "" #speech
        coremain()
    elif misboss == "HEATMAN": #AI name
        print "" #speech
        coremain()
    elif misboss == "ISABELLA": #AI name
        print "" #speech
        coremain()
    elif misboss == "KEBAB": #AI name
        print "" #speech
        coremain()
    elif misboss == "KOIZUMI": #AI name
        print "" #speech
        coremain()
    elif misboss == "MEEN": #AI name
        print "" #speech
        coremain()
    elif misboss == "MONSQUAZ": #AI name
        print "" #speech
        coremain()
    elif misboss == "SHODAN": #AI name
        print "" #speech
        coremain()
    elif misboss == "singularity": #AI name
        print "" #speech
        coremain()
    elif misboss == "LAL": #AI name
        print "" #speech
        coremain()
    elif misboss == "VINCENT": #AI name
        print "" #speech
        coremain()
    elif misboss == "Windows 3.1": #AI name
        print "" #speech
        coremain()
    elif misboss == "Zyzz": #AI name
        print "" #speech
        coremain()
    else:
        print "You shouldn't be seeing this, you whore."
        coremain()

def coremain(): #This'll involve backtracing, probably to the local terminal in artsy-fartsy style..
    print "Welcome to the rice fields motherfucker."

#Everything below here is seen by the player.
print "  #   #     #        #####  #   #  #####  ###  "
print "  #   #    # #      #       #  #   #      #  # "
print "  #   #    # #     #        # #    #      #   #"
print "  #####   #   #   #         ##     #####  #  # "
print "  #   #   #####    #        # #    #      # #  "
print "  #   #  #     #    #       #  #   #      #  # "
print "  #   #  #     #     #####  #   #  #####  #   #"
#Yes, yes. A title would be nice.
print "Original Concept by James Butcher."  # "But muh simplicity" - Every Batch user ever.
print "Shameless Python remake by Bromine." # I prefer Bromine to real names. Then I can appear in IRC and get ERP requests left, right and center.

print "What's your name?",
name = raw_input() # Yes, it would be nice if we had a name to work with.

#Email you receive at the start. Should include a command to re-read the email, but this'd involve turning the print email commands into a function, which I'd probably need Pygame to do properly.
print """You receive an email.
The email reads...

To: %s%i@yahoo.co.uk 
From: %s@smartsecurity.org
--------------------------------------------------
Hey %s, some ass hacked into my server last night and I was wondering if you could get him back for me. Nothing seems to be damaged or modified, but I'm worried about him getting in again and causing some real damage.

One thing he forgot to do was delete my log file, so I have his IP.

His IP is %s, so you might want to try one of your crazy hack tools on his ip, to see if he has anything you can ssh into.

I hope you can do something. I'm asking you because I know you won't tell anyone. If any of my colleagues hear of this, it could spell the end for my business.

Thanks in advance.

%s""" % (name, mailnum, misclient, name, misip, misclient)

print "What would you like to do now?" #IT BEGIIIIIIIIIIIIIIIIIIIIIINS
print "Type 'help' if you don't know what to do." #Refer to help()

OwnConsole() #Hackitalism, ho!
