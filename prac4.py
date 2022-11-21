#prac4
'''adhishankar_68={'company': 'UBISOFT MUMBAI','role': 'Game designer/animator/developer','salary': '5-6 LPA','empid': 'xyz123','location': 'ubisoft mumbai powai'}
print(adhishankar_68)

temp_info=adhishankar_68.copy()
print(adhishankar_68)

adhishankar_68['plan b']='Rockstar north'
print(adhishankar_68)

ROLE=(adhishankar_68['role'])
if ROLE=='software developer':
    print("present")
else:
    print("not present")

city=(adhishankar_68['location'])
if city=='ubisoft mumbai powai':
    print("present")
else:
    print("not present")

print(adhishankar_68)


state=[]
capital=[]
dicts={}
n=int(input("enter the number of elents for dictionary"))
for i in range (n):
    sta=input("enter state name:")
    state.append(sta)
    cap=input("enter its capital:")
    capital.append(cap)
for i in range (len(state)) :
    dicts[state[i]] = capital[i]
print(dicts)

temp2=temp_info.copy()
temp_info.clear()
print("temp2=",temp2)
print("temp_info=",temp_info)

print(len(adhishankar_68.keys()))'''
