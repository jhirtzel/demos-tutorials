import pyinputplus as pyin 

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyin.inputYesNo(prompt)
    print(response)
    if response in ['No','no']:
        break

print('Thank you. Have a nice day.')
