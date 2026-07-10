
from calibration import calibrate
from inference import infer

def main():
    print("Starting calibration...")
    ears,mars,pucs,moes=calibrate()
    print("Starting inference...")
    infer(ears,mars,pucs,moes)

if __name__=="__main__":
    main()
