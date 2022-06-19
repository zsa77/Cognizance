import numpy as np
  
  
def main():
  
    print('Initialised array')
    gfg = np.array([1, 2, 3, 4])
    print(gfg)
  
    print('current shape of the array')
    print(gfg.shape)
      
    print('changing shape to 2,2')
    gfg.shape = (2, 2)
    print(gfg)
  
if __name__ == "__main__":
    main()