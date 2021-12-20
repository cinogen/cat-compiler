# Inogen Cat

### A hobby Cat compiler created in Python.

---

cat is a hobby C compiler written in Python 3 that supports a subset of the C11 standard and generates reasonably efficient binaries, including some optimizations. cat also generates helpful compile-time error messages.

This [implementation of a trie](tests/general_tests/trie/trie.c) is an example of what cat can compile today. For a more comprehensive list of features, see the [feature test directory](tests/feature_tests).

## Quickstart

### x86-64 Linux
cat requires only Python 3.6 or later to compile C code. Assembling and linking are done using the GNU binutils and glibc, which you almost certainly already have installed.

To install cat:
```
pip3 install shivyc
```
To create, compile, and run an example program:
```c
$ vim hello.c
$ cat hello.c

#include <stdio.h>
int main() {
  printf("hello, world!\n");
}

$ shivyc hello.c
$ ./out
hello, world!
```
To run the tests:
```
git clone https://github.com/ShivamSarodia/ShivyC.git
cd cat
python3 -m unittest discover
```

### Other Architectures
For the convenience of those not running Linux, the [`docker/`](docker/) directory provides a Dockerfile that sets up an x86-64 Linux Ubuntu environment with everything necessary for cat. To use this, run:
```
git clone https://github.com/ShivamSarodia/ShivyC.git
cd cat
docker build -t shivyc docker/
docker/shell
```
This will open up a shell in an environment with cat installed and ready to use with
```
shivyc any_c_file.c           # to compile a file
python3 -m unittest discover  # to run tests
```
The Docker cat executable will update live with any changes made in your local cat directory.

## Implementation Overview
#### Preprocessor
cat today has a very limited preprocessor that parses out comments and expands `#include` directives. These features are implemented between [`lexer.py`](shivyc/lexer.py) and [`preproc.py`](shivyc/lexer.py).

#### Lexer
The cat lexer is implemented primarily in [`lexer.py`](shivyc/lexer.py). Additionally, [`tokens.py`](shivyc/tokens.py) contains definitions of the token classes used in the lexer and [`token_kinds.py`](shivyc/token_kinds.py) contains instances of recognized keyword and symbol tokens.

#### Parser
The cat parser uses recursive descent techniques for all parsing. It is implented in [`parser/*.py`](shivyc/parser/) and creates a parse tree of nodes defined in [`tree/nodes.py`](shivyc/tree/nodes.py) and [`tree/expr_nodes.py`](shivyc/tree/expr_nodes.py).

#### IL generation
cat traverses the parse tree to generate a flat custom IL (intermediate language). The commands for this IL are in [`il_cmds/*.py`](shivyc/il_cmds/) . Objects used for IL generation are in [`il_gen.py`](shivyc/il_gen.py) , but most of the IL generating code is in the `make_code` function of each tree node in [`tree/*.py`](shivyc/tree/).

#### ASM generation
cat sequentially reads the IL commands, converting each into Intel-format x86-64 assembly code. cat performs register allocation using George and Appel’s iterated register coalescing algorithm (see References below). The general ASM generation functionality is in [`asm_gen.py`](shivyc/asm_gen.py) , but much of the ASM generating code is in the `make_asm` function of each IL command in [`il_cmds/*.py`](shivyc/il_cmds/).
