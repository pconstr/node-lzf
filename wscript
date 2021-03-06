import Options
from os import unlink, symlink, popen
from os.path import exists

srcdir = "."
blddir = "build"
VERSION = "0.1.0"

def set_options(opt):
  opt.tool_options("compiler_cxx")

  opt.add_option('--debug', dest='debug', action='store_true', default=False)

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")

  conf.env.DEFINES = []
  conf.env.USELIB = []
  conf.env.CXXFLAGS = [ '-O2' ]


def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.cxxflags = ["-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE", "-Wall"]
  obj.target = "lzf"
  obj.source = "src/lzf.cc src/lzf/lzf_c.cc src/lzf/lzf_d.cc"
  obj.defines = bld.env.DEFINES
  obj.uselib = bld.env.USELIB