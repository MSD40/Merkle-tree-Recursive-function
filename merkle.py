import hashlib

# Define a function called merkle
def merkle(data, initial=True):
    
    # If initial is True, perform the initial setup
    if initial == True:
        for i in range(0, len(data)):
            # Calculate the SHA-256 hash of the transaction and append it to the data
            data.append(hashlib.sha256(str(i).encode()).hexdigest())
            # Remove the first element from the data (FIFO)
            data.pop(0)
        # Recursively call the merkle function with initial set to False
        merkle(data, False)

    # If there is only one element in the data, return it as a list
    if len(data) == 1:
        return [data]

    # If the length of data is odd, duplicate the last element
    if len(data) % 2 != 0:
        data.append(data[-1])

    new_data = []
    # Iterate through the data in pairs and concatenate their hashes
    for i in range(0, len(data), 2):
        concatenated_hash = hashlib.sha256(str((data[i] + data[i + 1])).encode()).hexdigest()
        new_data.append(concatenated_hash)

    # Return the current data as a list and recursively call merkle with the new_data
    return [data] + merkle(new_data, False)

    # merkel_root = merkle(data)[-1]
# NoTX=int(input("pls enter the number of transactions : "))
# # NoTX : number of transactions
# data=[]
# for i in range(0,NoTX) :
    
#     data.append(i)
# print(merkle(data))