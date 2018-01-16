import random
import string

class MakeRigs:
    MINER_ARR = ['GTX-1070Ti','GTX-1070Ti','GTX-1070Ti','GTX-1070Ti','GTX-1070Ti','GTX-1080','GTX-1060','AMD 1600X']
    ALGO = ['Equihash','NeoScript','Cryponight','Lyra2REv2']
    RIG_DESCR = ['Dedicated to alt coins and stuff. Unstable, something something technical jargon.',
                    'Some description'
                    'State Employee Retirement Fund',
                    '',
                    'Personal Computer']

    def __init__(self,rigCount,minerCount,isRandom):
        
        self.rigs = {}
        for i in range(0,rigCount):
            thisMinerCount = minerCount
            if isRandom:
                thisMinerCount = random.randint(1,minerCount)
            
            tempMiners = {}
            hashRate = 0.0
            rigStatus = 0 #0 ok, 1 warn, 2 trouble
            for j in range(0,thisMinerCount):
                minerId = 'MinerId_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
                minerHash = round(random.uniform(150, 600),2)
                hashRate += minerHash
                minerStatus = random.randint(0,3)
                if minerStatus > rigStatus:
                    rigStatus = minerStatus
                tempMiners[minerId] = {
                    'type':MakeRigs.MINER_ARR[random.randint(0,len(MakeRigs.MINER_ARR)-1)],
                    'hashRate': round(minerHash, 2),
                    'algorithm': MakeRigs.ALGO[random.randint(0,len(MakeRigs.ALGO)-1)],
                    'status':minerStatus,
                    'temp': round(random.uniform(40, 80),1),
                    'watts': round(random.uniform(50, 150),1)
                }
            
            rigId = 'RigId_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
            self.rigs[rigId] = {
                'name':'Example Rig ' + str(i + 1),
                'description':'',#MakeRigs.RIG_DESCR[( (i+1) % len(MakeRigs.RIG_DESCR) ) - 1],
                'hashRate':round(hashRate, 2),
                'uptime':str(random.randint(0,20)) +'d ' + str(random.randint(0,23)) + 'h ' + str(random.randint(0,59)) + 'm',
                'miners':tempMiners
            }

#temp=MakeRigs(2,2)
#print(temp.rigs)

'''
            rigs = {
            "Rig1ID":{
                "name":"Example Rig",
                "description":"Dedicated to alt coins and stuff. Unstable, something something technical jargon.",
                "miners": {
                    "miner1ID":{
                        'type': 'GTX-1070Ti'
                    },
                    "miner2ID":{
                        'type': 'GTX-1070Ti'
                    },
                    "miner3ID":{
                        'type': 'GTX-1070Ti'
                    },
                    "miner4ID":{
                        'type': 'GTX-1070Ti'
                    }
                }
            },
            "Rig2":{
                "name":"Another Example Rig",
                "description":"State employees retirement fund",
                "miners":  {
                    "miner1ID":{
                        'type': 'GTX-1080'
                    },
                    "miner2ID":{
                        'type': 'GTX-1070Ti'
                    },
                    "miner3ID":{
                        'type': 'GTX-1070Ti'
                    }
                }
            },
            "Rig3":{
                "name":"Personal Computer",
                "description":"",
                "miners": {
                    "miner1ID":{
                        'type': 'GTX-1080'
                    },
                    "miner2ID":{
                        'type': 'GTX-1070Ti'
                    }
                }['AMD 1600X','GTX-1050Ti']
            },
            "Rig4":{
                "name":"PS3",
                "description":"Why not?",
                "miners": ['Cell microprocessor','NV47']
            }
        }'''