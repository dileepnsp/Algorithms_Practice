import sys
def main():
    # print command line arguments
    for arg in sys.argv[1:]:
        print(arg)
    #arcpy.env.workspace = r"C:\Users\cdileepkumar\Documents\01 Project\ArcGIS\TunnelSchematic\20190613_LATEST_DB\ITPT1_PROD_20190606.gdb"
    #expression = "LK_ID_NUM = 97204"

if __name__ == "__main__":
    main()

