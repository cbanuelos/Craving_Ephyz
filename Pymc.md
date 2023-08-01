To install a specific version of pymc: conda install -c conda-forge pymc=4.4.0  

For errors like unsupported tapi file type '!tapi-tbd' in YAML file '/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib/libSystem.tbd' for architecture x86_64:

Stack overflow comment:
If your $PATH is set up so that Anaconda's ld has higher preference over the system linker, this will explain it:
$ which -a ld
/blah/anaconda3/bin/ld
/usr/bin/ld
If that's the case, reorder your PATH to put anaconda's directory after /usr/bin. Then, which ld should point to the system ld, and you should be good to go.

Run the following: export PATH="/usr/bin:/bin:/usr/sbin:/sbin:/Users/cristybanuelos/opt/anaconda3/bin:/Users/cristybanuelos/opt/anaconda3/condabin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/Library/TeX/texbin:/Library/Apple/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin"
