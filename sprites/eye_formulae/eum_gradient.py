lightest = [119, 108, 100]
darkest = [36, 31, 27]

for i in range(6):
    print([int(lightest[0]+(darkest[0]-lightest[0])/6*i),
    int(lightest[1]+(darkest[1]-lightest[1])/6*i),
    int(lightest[2]+(darkest[2]-lightest[2])/6*i)])
print(darkest)
