pigmentation = 0
refraction = 0
rgb = [241, 221, 150]
print(f'"outer": {rgb},')

pupils = [0, 0, 0]
pupils1 = [v*0.5 for v in rgb]
rgb = [round(rgb[0]*(0.66-refraction*0.03+(10-pigmentation)*0.018)), round(rgb[1]*(0.45+refraction*0.025+(10-pigmentation)*0.025)), round(rgb[2]*(0.40+refraction*0.020))]
print(f'"inner": {rgb},')
pupils2 = [v*0.5 for v in rgb]
for i in range(3):
    pupils[i] = round((pupils1[i] + pupils2[i])/2)
    
print(f'"pupil": {pupils}')