# Trial division (slow_code) vs sieve of Eratosthenes (fast_code)

import timeit

slow_code = """
#Store the products from multiplying each 13-character string in a list
products = []

#Create a function to find the 13-digit products for a given chunk of digits and add those products to the list
def find_products(chunk):
    #To start, calculate the product of the first 13 digits
    product = 1
    for i in range(13):
        product *= int(chunk[i])
    products.append(product)
    
    #Then we divide that product by the first digit, and multiply it by the 14th, and then repeat that pattern until we've got the whole way through the chunk
    for j in range(len(chunk) - 13):
        product = product * int(chunk[13+j]) / int(chunk[j])
        products.append(product)


#Create a function to find all the products for all the chunks
def find_all_products(num):
    # Convert the number into a string and split it into chunks whenever a 0 appears
    num_str = str(num)
    chunks = num_str.split("0")

    # Eliminate any empty chunks (where the 0's were) and any chunks with less than 13 characters
    useful_chunks = [chunk for chunk in chunks if chunk and len(chunk) >= 13]
    
    for chunk in useful_chunks:
        find_products(chunk)
    
    print(f"The largest product of 13 consecutive digits in the given number is {int(max(products))}")


find_all_products(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
"""

fast_code = """
# Create a function to find the 13-digit products for a given chunk of digits and check if it's the highest so far
def find_products(chunk, max_product):
    # To start, calculate the product of the first 13 digits
    product = 1
    for i in range(13):
        product *= int(chunk[i])
    if product > max_product:
        max_product = product

    # Then we divide that product by the first digit, and multiply it by the 14th, and then repeat that pattern until we've got the whole way through the chunk
    for j in range(len(chunk) - 13):
        product = product * int(chunk[13+j]) / int(chunk[j])
        if product > max_product:
            max_product = product
    
    #The function needs to return the value of the maximum product so far
    return max_product


# Create a function to find all the products for all the chunks
def find_all_products(num):
    # Convert the number into a string and split it into chunks whenever a 0 appears
    num_str = str(num)
    chunks = num_str.split("0")

    # Eliminate any empty chunks (where the 0's were) and any chunks with less than 13 characters
    useful_chunks = [chunk for chunk in chunks if chunk and len(chunk) >= 13]

    #Set max_product = 1 so it's got something to start with
    max_product = 1

    #Run the function defined above for each chunk, each time updating max_product with the new maximum product so far
    for chunk in useful_chunks:
        max_product = find_products(chunk, max_product)
        

    print(
        f"The largest product of 13 consecutive digits in the given number is {int(max_product)}")


find_all_products(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
"""

slow_code_time = timeit.timeit(slow_code, number=100)/100
fast_code_time = timeit.timeit(fast_code, number=100)/100

print("The slow code ran in {:.6f}s".format(slow_code_time))
print("The fast code ran in {:.6f}s".format(fast_code_time))

improvement = slow_code_time / fast_code_time

print("The fast code was {:.2f}x faster".format(improvement))
