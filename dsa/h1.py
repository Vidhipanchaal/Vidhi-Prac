
block_list = ['vidhi@gmail.com', 'nir@gmail.com', 'nidhi@gmail.com', 'rudra@gmail.com']

email = 'nir@gmail.com'

if email not in block_list:
    print('its not spam email')
else:
    print("its spam email")