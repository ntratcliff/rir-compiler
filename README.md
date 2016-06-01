#Rainbow Intermediate Representation
The Rainbow Intermediate Representation is a language designed to represent the [Rainbow](https://github.com/ntratcliff/Rainbow/) programming language before being encoded into a bitmap image.

The RIR language is simple to understand. Each line contains one unencoded Rainbow statement. Statements are encoded into the output image such that they execute procedurally. 

All whitespace characters, all characters following the `;` character, and all empty lines are ignored during compilation.

The following RIR example represents a simple "Hello World!" program in Rainbow.
```
100048  ;set cell 0x00 to value 0x48 (H)
101045  ;set cell 0x01 to value 0x45 (E)
10204C  ;set cell 0x02 to value 0x4C (L)
10304C  ;set cell 0x03 to value 0x4C (L)
10404F  ;set cell 0x04 to value 0x4F (O)
105020  ;set cell 0x05 to value 0x20 ( )
106057  ;set cell 0x06 to value 0x57 (W)
10704F  ;set cell 0x07 to value 0x4F (O)
108052  ;set cell 0x08 to value 0x52 (R)
10904C  ;set cell 0x09 to value 0x4C (L)
10A044  ;set cell 0x0A to value 0x44 (D)
10B021  ;set cell 0x0B to value 0x21 (!)
20010B  ;print values from cell 0x00 to cell 0x0B 
000000  ;exit with status code 0x00
```

#Using the RIR Compiler
The RIR Compiler takes the path to one text file (preferably `.rir`) and outputs a compiled Rainbow program.

###Additional Arguments
`--output` or `-o`: the output file. *e.g.* `python compiler.py foo.rir -o bar.bmp`

`--dim-x` or `-x`: output image width, in pixels. *e.g.* `python compiler.py foo.rir -x 4`

`--dim-y` or `-y`: output image height, in pixels. *e.g.* `python compiler.py foo.rir -y 3`

