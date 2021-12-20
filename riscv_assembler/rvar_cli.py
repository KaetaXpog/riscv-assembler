#!/usr/bin/env python3
import argparse
import convert

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="RISC-V assembler")
    parser.add_argument('filename',help='file to be assembled')
    parser.add_argument('-o','--ofname',help='output file name')
    args=parser.parse_args()

    cnv=convert.AssemblyConverter()
    cnv.convert_ret(args.filename)
    if args.ofname:
        cnv.write_to_file(args.ofname)
    else:
        print(cnv.instructions)