def main():
    import math
    radii = [5, 2, 4, 3, 1]
    pi = math.pi
    index = 0
    
    for i in radii:
        area = pi * i**2
        print("Radius is: ", radii[index], "Area is: ", area)
        index += 1
   
   
main()