CFILES = $(wildcard *.c)
BIN = $(CFILES:.c=)
CC = gcc
CFLAGS = -Wall

all: $(BIN)

%: %.c
	gcc -Wall $< -o $@

clean:
	rm -v $(BIN)

.PHONY: all clean

