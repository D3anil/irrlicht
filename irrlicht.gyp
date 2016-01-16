{
  'targets': [
    {
      'target_name': '01.HelloWorld',
      'type': 'executable',
      'sources': [
        'examples/01.HelloWorld/main.cpp',
      ],
      'include_dirs': [
        'include',
        '/usr/X11R6/include',
      ],
      'link_settings': {
        'libraries': [
          '--verbose',
          '-L../lib/Linux',
          '-L/usr/X11R6/lib',
          '-lm',
          '-lGL',
          '-lXxf86vm',
          '-lXext',
          '-lX11',
          '-lXcursor',
          '-lIrrlicht',
        ],

# LDFLAGS += -Llib/Linux -lIrrlicht
# LDFLAGS += -L/usr/X11R6/lib$(LIBSELECT) -lGL -lXxf86vm -lXext -lX11 -lXcursor

      },
    },
  ],
}
