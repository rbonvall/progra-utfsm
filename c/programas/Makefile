CFILES = $(wildcard *.c)
BIN = $(CFILES:.c=)
CC = gcc
CFLAGS = -Wall
LDFLAGS = -lm

all: $(BIN)

%: %.c

clean:
	@rm -vf $(BIN)

.PHONY: all clean

