import sys
import os.path
import struct

def read( pathfilename, verbose=False ):
    f = open( pathfilename, 'rb' )
    f.read(7)
    reclink = str(struct.unpack('i',f.read(4))[0])
    int1 = struct.unpack('d',f.read(8))[0]
    int2 = struct.unpack('d',f.read(8))[0]
    int3 = struct.unpack('d',f.read(8))[0]
    int4 = struct.unpack('d',f.read(8))[0]
    levname = b''.join(struct.unpack('51c',f.read(51))).split(b'\x00')[0]
    lgr = b''.join(struct.unpack('16c',f.read(16))).split(b'\x00')[0]
    ground = b''.join(struct.unpack('10c',f.read(10))).split(b'\x00')[0]
    sky = b''.join(struct.unpack('10c',f.read(10))).split(b'\x00')[0]

    if verbose:
        print ( 'Reclink: ' + reclink )
        print ( 'Integrity 1: ' + str(int1) )
        print ( 'Integrity 2: ' + str(int2) )
        print ( 'Integrity 3: ' + str(int3) )
        print ( 'Integrity 4: ' + str(int4) )
        print ( b'Level name: ' + levname )
        print ( b'LGR:' + lgr )
        print ( b'Ground: ' + ground )
        print ( b'Sky: ' + sky )

    polys = []
    n_polys = int(struct.unpack('d',f.read(8))[0])
    for p in range(n_polys):
        grass = struct.unpack('i',f.read(4))[0]
        # skip grass polygons
        if grass != 1:
            poly = []
            vs = int(struct.unpack('i',f.read(4))[0])
            for v in range(vs):
                x = struct.unpack('d',f.read(8))[0]
                y = struct.unpack('d',f.read(8))[0]
                poly.append( [x,y] )
            polys.append( poly )
    if verbose:
        print()
        print('%d polygons:' % n_polys)
        for i, poly in enumerate(polys):
            print('%dnd polygon has %s vertex:' % (i+1, len(poly)) )
            for vx in poly:
                print(vx)
            print()
            
    objs = []
    n_objs = int(struct.unpack('d',f.read(8))[0])
    for o in range(n_objs):
        x = struct.unpack('d',f.read(8))[0]
        y = struct.unpack('d',f.read(8))[0]
        objtype = struct.unpack('i',f.read(4))[0]
        
        #if otype == 1: ostr += 'flower(1) '
        #elif otype == 2: ostr += 'apple(2) '
        #elif otype == 3: ostr += 'killer(3) '
        #elif otype == 4: ostr += 'start(4) '
        #else: ostr += 'errortype(' + str(otype) + ') '
        
        #ostr += 'gravity='
        gravity = struct.unpack('i',f.read(4))[0]
        #if gravity == 0: ostr += 'normal(0) '
        #elif gravity == 1: ostr += 'up(1) '
        #elif gravity == 2: ostr += 'down(2) '
        #elif gravity == 3: ostr += 'left(3) '
        #elif gravity == 4: ostr += 'right(4) '
        #else: ostr += 'errorvalue(' + str(gravity) + ') '
        animation = struct.unpack('i',f.read(4))[0]
        
        # skip animation
        objs.append([x, y, objtype, gravity])

    if verbose:
        print('%d objects:' % n_objs)
        for obj in objs:
            print(obj)
    f.close()
    
    return reclink, int1, int2, int3, int4, levname, lgr, ground, sky, polys, objs
    
if __name__ == '__main__':
    read('ai.lev', True)

