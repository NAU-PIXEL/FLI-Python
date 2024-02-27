obj-m		:= fliusb.o

KDIR		?= /lib/modules/$(shell uname -r)/build
PWD		:= $(shell pwd)

EXTRA_CFLAGS		+= -O2 -Wall

EXTRA_CFLAGS		+= -DDEBUG	# enable debug messages
#EXTRA_CFLAGS		+= -DASYNCWRITE	# enable asynchronous writes
EXTRA_CFLAGS		+= -DSGREAD	# enable scatter-gather reads

all: module cleanup

module:
	$(MAKE) -C $(KDIR) M=$(shell pwd) modules

cleanup:
	rm -f *.o .*.cmd *.mod.c; rm -rf .tmp_versions

clean: cleanup
	rm -f *.ko test

install: module cleanup
	mkdir -p /lib/modules/$(shell uname -r)/misc
	cp fliusb.ko /lib/modules/$(shell uname -r)/misc
	depmod -a
	modprobe fliusb