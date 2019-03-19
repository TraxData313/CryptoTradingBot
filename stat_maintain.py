import time, datetime

print '-------------------------'
print 'Statistic Maintan BOT 2.0'
print '-------------------------'
time.sleep(3)

# PARAMETERS:
# - How long statistics should be [sec]:
stat_total_time = 604800    # example: 604800 sec = 7 days
# - What the refresh rate should be [sec]:
stat_refresh_rate = 60      # 30 sec


# - What is the product [LTC / ETH / BTC]:
product_LTC = 'LTC'
product_ETH = 'ETH'
product_BTC = 'BTC'
product_file_LTC = 'LTC-EUR.txt'
product_file_ETH = 'ETH-EUR.txt'
product_file_BTC = 'BTC-EUR.txt'
# ---------
# Declaration:
last_price_LTC = 0
current_price_LTC = 0
STATS_LTC = [0]
last_price_ETH = 0
current_price_ETH = 0
STATS_ETH = [0]
last_price_BTC = 0
current_price_BTC = 0
STATS_BTC = [0]
# ---------
# Variables:
# - Enough time for stats to fill trigger [loops]:
stat_ready_loops = stat_total_time / stat_refresh_rate
# - Dummy variable to track loops:
ticker = 1
# - Stat is full triggers:
stat_is_ready_LTC = 0 # 0=notFull / 1=Full
stat_is_ready_ETH = 0 # 0=notFull / 1=Full
stat_is_ready_BTC = 0 # 0=notFull / 1=Full
# ---------
# Create the fileName:
fileName_LTC =  'stat_LTC.txt'
fileName_ETH =  'stat_ETH.txt'
fileName_BTC =  'stat_BTC.txt'
# Create error.log file:
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
appendFile = open('Stat.error.log', 'a') 
appendFile.write('\n\n\nStatistics.error.log started at: ')
appendFile.write(st)
appendFile.write('\n')
appendFile.close()





# - Copy current data LTC:
print 'Copying current data into a  LTC list...'
# Get statistics:
## List parser:
### Parameters:
temp_fileName = fileName_LTC
temp_listName = 'temp_listName'
list_size     = stat_ready_loops # exact # of elements
temp_listName = open(temp_fileName, 'r').readlines()
### Workings:
tick = 0
STATS_LTC = []
while (tick < list_size):
    try:
        temp_float = float(temp_listName[tick].split()[0])
    except:
        pass
    STATS_LTC.append(temp_float)
    tick = tick + 1
# STATS is ready!
time.sleep(0.5)
#print(STATS_LTC) // for test purposes
print 'Done!'
print
## END List Creator: TESTED
time.sleep(1)


# - Copy current data ETH:
print 'Copying current data into an ETH list...'
# Get statistics:
## List parser:
### Parameters:
temp_fileName = fileName_ETH
temp_listName = 'temp_listName'
list_size     = stat_ready_loops # exact # of elements
temp_listName = open(temp_fileName, 'r').readlines()
### Workings:
tick = 0
STATS_ETH = []
while (tick < list_size):
    try:
        temp_float = float(temp_listName[tick].split()[0])
    except:
        pass
    STATS_ETH.append(temp_float)
    tick = tick + 1
# STATS is ready!
time.sleep(0.5)
#print(STATS_ETH) // for test purposes
print 'Done!'
print
## END List Creator: TESTED
time.sleep(1)

# - Copy current data BTC:
print 'Copying current data into a  BTC list...'
# Get statistics:
## List parser:
### Parameters:
temp_fileName = fileName_BTC
temp_listName = 'temp_listName'
list_size     = stat_ready_loops # exact # of elements
temp_listName = open(temp_fileName, 'r').readlines()
### Workings:
tick = 0
STATS_BTC = []
while (tick < list_size):
    try:
        temp_float = float(temp_listName[tick].split()[0])
    except:
        pass
    STATS_BTC.append(temp_float)
    tick = tick + 1
# STATS is ready!
time.sleep(0.5)
print 'Done!'
print
## END List Creator: TESTED
time.sleep(1)






print
print
print 'Initiating maintanance algorithm...'
time.sleep(1)
print 'Done!'

while True:

# - get timestamp:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    

# - Get current_price_LTC:
    current_price_LTC = open(product_file_LTC, 'r').read()
    try:
        current_price_LTC = str(current_price_LTC)
    except:
        current_price_LTC = last_price_LTC
        appendFile = open('Stat.error.log', 'a')
        appendFile.write('\n\n')
        appendFile.write(st)
        appendFile.write(' : ERROR while setting current_price_LTC to str handeled ( current_price_LTC = last_price_LTC ). ')
        appendFile.write('\n- Current price_LTC =')
        appendFile.write(current_price_LTC)
        appendFile.close()

# - Get current_price_ETH:
    current_price_ETH = open(product_file_ETH, 'r').read()
    try:
        current_price_ETH = str(current_price_ETH)
    except:
        current_price = last_price
        appendFile = open('Stat.error.log', 'a')
        appendFile.write('\n\n')
        appendFile.write(st)
        appendFile.write(' : ERROR while setting current_price_LTC to str handeled ( current_price_ETH = last_price_ETH ). ')
        appendFile.write('\n- Current price_ETH =')
        appendFile.write(current_price_ETH)
        appendFile.close()

# - Get current_price_BTC:
    current_price_BTC = open(product_file_BTC, 'r').read()
    try:
        current_price_BTC = str(current_price_BTC)
    except:
        current_price_BTC = last_price_BTC
        appendFile = open('Stat.error.log', 'a')
        appendFile.write('\n\n')
        appendFile.write(st)
        appendFile.write(' : ERROR while setting current_price_BTC to str handeled ( current_price_BTC = last_price_LTC ). ')
        appendFile.write('\n- Current price_BTC =')
        appendFile.write(current_price_BTC)
        appendFile.close()



# - Update lists:
    STATS_LTC.pop(0)
    STATS_LTC.append(current_price_LTC)
    STATS_ETH.pop(0)
    STATS_ETH.append(current_price_ETH)
    STATS_BTC.pop(0)
    STATS_BTC.append(current_price_BTC)



    

# - Export statistical data to a file:
    print
    print
    print
    print st
    print 'Maintaining stat file:', fileName_LTC
    # - Dummies for the string:
    i = 0       # <- set i = 0
    text = ''   # <- set text = 0
    # - Build the text string to write to the file:
    while (i < stat_ready_loops):  
        temp_text = str(STATS_LTC[i]) + '\n'
        i = i + 1
        text = text + temp_text
    saveFile = open(fileName_LTC, 'w')   # <- open the file
    saveFile.write(text)             # <- write the string
    saveFile.close()                 # <- close the file



# - Export statistical data to a file:
    print 'Maintaining stat file:', fileName_ETH
    # - Dummies for the string:
    i = 0       # <- set i = 0
    text = ''   # <- set text = 0
    # - Build the text string to write to the file:
    while (i < stat_ready_loops):  
        temp_text = str(STATS_ETH[i]) + '\n'
        i = i + 1
        text = text + temp_text
    saveFile = open(fileName_ETH, 'w')   # <- open the file
    saveFile.write(text)             # <- write the string
    saveFile.close()                 # <- close the file


# - Export statistical data to a file:
    print 'Maintaining stat file:', fileName_BTC
    # - Dummies for the string:
    i = 0       # <- set i = 0
    text = ''   # <- set text = 0
    # - Build the text string to write to the file:
    while (i < stat_ready_loops):  
        temp_text = str(STATS_BTC[i]) + '\n'
        i = i + 1
        text = text + temp_text
    saveFile = open(fileName_BTC, 'w')   # <- open the file
    saveFile.write(text)             # <- write the string
    saveFile.close()                 # <- close the file
    


    last_price_LTC = current_price_LTC
    last_price_ETH = current_price_ETH
    last_price_BTC = current_price_BTC
    time.sleep(stat_refresh_rate)










