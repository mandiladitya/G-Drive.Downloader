import sys
# Enter Sharing URL
url=input()
# Extract ID from URL
idurl=url[32:-17]
new=url[:25]+"uc?id="+idurl+"&export=download"
print("--------------")
print(new)
