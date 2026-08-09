refraction = 0
rgb = [214, 223, 220]
print(f'"outer": {rgb},')

pupils = [0, 0, 0]
pupils1 = [v*0.5 for v in rgb]
rgb = [round(rgb[0]*(0.85-refraction*0.015)), round(rgb[1]*(0.9-refraction*0.04)), round(rgb[2]*(0.95))]
print(f'"inner": {rgb},')
pupils2 = [v*0.5 for v in rgb]
for i in range(3):
    pupils[i] = round((pupils1[i] + pupils2[i])/2)
    
print(f'"pupil": {pupils}')