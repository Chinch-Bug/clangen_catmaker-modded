refraction = 10
rgb = [56, 140, 203]
print(f'"outer": {rgb},')

pupils = [41, 7, 11]
# pupils1 = [v*0.5 for v in rgb]
rgb = [round(rgb[0]*(0.9-refraction*0.015)), round(rgb[1]*(0.9-refraction*0.04)), round(rgb[2]*(0.95-refraction*0.04))]
print(f'"inner": {rgb},')
# pupils2 = [v*0.5 for v in rgb]
# for i in range(3):
#     pupils[i] = round((pupils1[i] + pupils2[i])/2)
    
print(f'"pupil": {pupils}')