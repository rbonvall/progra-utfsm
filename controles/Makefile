all:
	@-for i in $$(ls -d */); do make -C $$i; done
clean:
	@-for i in $$(ls -d */); do make -C $$i clean; done


.PHONY: all clean
