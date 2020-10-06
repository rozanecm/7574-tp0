#!/bin/bash
# guardo output real y el resperado en dos archivos distintos,
# los cuales seran comparados por diff. De acuerdo al valor de retorno
# del cmd diff, podemos informar si hubo exito o no.
echo 1 | sudo docker run -i --network=7574-tp0_testing_net busybox nc server 12345 > file1
echo "Your Message has been received: b'1'" > file2
diff file1 file2
ret=$?

if [[ $ret -eq 0 ]]; then
    echo "passed."
else
    echo "failed."
fi
rm file1
rm file2
