# TraceOpenedFiles
The Python version of lsof. It's for Windows. But it's not designed to be the same as lsof.

It is designed to monitor the file usage of a selected process.

## Parameters Available

| Option | Values | Meaning |
|:------:|:------:|:-------:|
| -pid   | [PID integer] | Indicate the target pid. |
| -file  | string | Choose the filepath of the program to run. |
| -name  | string | Choose the process to catch by name. |
| -persist | [Present/Absent] | Determine whether to monitor targets forever. |
| -sleeplength | float | Set the time length of sleeping between list checks. Set to "preset" will use *0.1* as the value.|
