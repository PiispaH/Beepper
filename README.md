# Beepper

Simple interface to create an alert noise on linux, might need to apt install some packages.

### Usage

Has a single parameter for setting the volume.

Example usage in a project:

    from beepper import beep

    for i in seq:
        do_something(i)

    beep(1.5)

    do_something_else()

In the example, beep gets called after the loop. The function `do_something_else` gets called while the beep is still running in the backround.