import os
import sys, json
import traceback, logging, logging.handlers
import time
from struct import *
import struct 

print 'glb test 0.1'
print 'writes a simple glb file with a triangle'


jsonobj ={
    "accessors":{
        "accessor_21":{
            "bufferView":"bufferView_29",
            "byteOffset":0,
            "byteStride":0,
            "componentType":5123,
            "count":3,
            "type":"SCALAR"
        },
        "accessor_23":{
            "bufferView":"bufferView_30",
            "byteOffset":0,
            "byteStride":12,
            "componentType":5126,
            "count":3,
            "max":[ 0.5, 0.5, 0.5 ],
            "min":[ -0.5, -0.5, -0.5 ],
            "type":"VEC3"
        },
        "accessor_25":{
            "bufferView":"bufferView_30",
            "byteOffset":36,
            "byteStride":12,
            "componentType":5126,
            "count":3,
            "max":[ 1, 1, 1 ],
            "min":[ -1, -1, -1 ],
            "type":"VEC3"
        }
    },
    "animations":{
    },
    "asset":{
        "generator":"collada2gltf@774bd4fe67703fbf60f9c02f3ba79632f246e9b6",
        "premultipliedAlpha":True,
        "profile":{
            "api":"WebGL",
            "version":"1.0.2"
        },
        "version":"1.0"
    },
    "bufferViews":{
        "bufferView_29":{
            "buffer":"binary_glTF",
            "byteLength":6,
            "byteOffset":0,
            "target":34963
        },
        "bufferView_30":{
            "buffer":"binary_glTF",
            "byteLength":72,
            "byteOffset":6,
            "target":34962
        }
    },
    "buffers":{
        "binary_glTF":{
            "type":"arraybuffer",
            "byteLength":13790,
            "uri":"data:,"
        }
    },
    "meshes":{
        "Geometry-mesh002":{
            "name":"Mesh",
            "primitives":[
                {
                    "attributes":{
                        "NORMAL":"accessor_25",
                        "POSITION":"accessor_23",
#                          "TEXCOORD_0":"accessor_27"
                    },
                    "indices":"accessor_21",
#                          "material":"Effect-Texture",
                    "mode":4
                }
            ]
        }
    },
    "nodes":{
        "Geometry-mesh002Node":{
            "children":[
            ],
            "matrix":[ 
                1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1
            ],
            "meshes":[
                "Geometry-mesh002"
            ],
            "name":"Mesh"
        },
        "node_3":{
            "children":[
                "Geometry-mesh002Node"
            ],
            "matrix":[
                1, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0,0 , 0, 0, 1
            ],
            "name":"Y_UP_Transform"
        }
        
    },
    "scene":"defaultScene",
        "scenes":{
            "defaultScene":{
                "nodes":[
                    "node_3"
                ]
        }
    },
    "extensionsUsed":[
        "KHR_binary_glTF"
    ]
}

jsonstr = json.dumps(jsonobj)

print jsonstr

with open('c:/tests/x3d2/x3d2/src/assets/test_e.glb', 'wb+') as f:
    # head
    f.write('glTF')
    f.write(struct.pack('i',1))

    jsonlength=sys.getsizeof(jsonstr) 
    length =20+jsonlength+78
    f.write(struct.pack('i',length)) #filelength
    f.write(struct.pack('i',jsonlength)) #contentlength
    f.write(struct.pack('i',0)) #contentformat


    # json
    f.write( jsonstr)

    # geometry data
    indices = [0,1,2]
    positions = [0.0,0.0,0.0,   0.0, 1.0, 0.0,   1.0, 1.0, 0.0]
    normals = [0.0,0.0,1.0,   0.0, 0.0, 1.0,   0.0, 0.0, 1.0]

    for b in indices:
       f.write(struct.pack('h', int(b)))
    for b in positions:
       f.write(struct.pack('f', float(b)))
    for b in normals:
       f.write(struct.pack('f', float(b)))

