{
  'variables': {},
  'targets': [
    {
      'target_name': 'bson-cpp',
      'type': 'static_library',
      'include_dirs': [ 
        'src',
        '.',
      ],
      'direct_dependent_settings': {
        'include_dirs': [ 
          'src',
          '.',
        ],
        'libraries': [ 
          # '-lboost_thread-mt', # needed for boost::spirit in util/json.cpp
        ],
      },
      'sources': [
        'src/bsonobj.cpp',
        'src/oid.cpp',
        'src/util/json.cpp',
        'lib/base64.cpp',
        'lib/md5.c',
        'lib/nonce.cpp'
      ],
    },
  ],
}

# BSONHEADERS = src/*.h
# BSONSOURCES = src/bsonobj.cpp src/oid.cpp
# 
# UTILHEADERS = src/util/*.h
# UTILSOURCES = src/util/json.cpp
# 
# LIBHEADERS = lib/atomic_int.h lib/base64.h lib/md5.h lib/nonce.h
# LIBSOURCES = lib/base64.cpp lib/md5.c lib/nonce.cpp